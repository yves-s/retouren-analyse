#!/usr/bin/env python3
"""Erzeugt synthetische Demo-Daten im Stil eines ERP-Berichte-Exports (eine Zeile
je Position). Deterministisch (fester Seed), mit eingebauten, findbaren Mustern:

1. Groessen-Laeufer: "Hoodie Classic" faellt klein aus (zu_klein-Haeufung)
2. Chargen-Problem: "Sneaker Socken 3er-Pack" Defekt-Spike im April 2026
3. Foto-Mismatch: "Sommerkleid Print" nicht_wie_beschrieben/Farbe-Haeufung
4. Serien-Retournierer: Kundin K-10442 (Bracketing, fast alles geht zurueck)
5. Nicht abgeholte Sendungen: ~2,5 % der Bestellungen, stark Rechnungskauf-lastig
"""

import csv
import random
from datetime import datetime, timedelta

random.seed(19)

START = datetime(2026, 1, 1)
DAYS = 181  # Bestellungen Jan bis Jun 2026

# Datenstand des Exports. Retouren, die spaeter eintreffen wuerden, existieren noch nicht.
# Dadurch sind die juengsten Bestell-Kohorten echt unvollstaendig, genau wie in der Praxis,
# und ihre Quote sieht faelschlich besser aus.
CUTOFF = datetime(2026, 7, 5)

SIZES = ["XS", "S", "M", "L", "XL"]
COLORS = ["Schwarz", "Weiss", "Navy", "Oliv"]

# code, name, preis, stueckkosten, retourenwahrscheinlichkeit, verkaufsgewicht, farben
# Der Zip-Hoodie ist der Bestseller mit unauffaelliger Quote: er taucht in keiner
# Top-Quoten-Liste auf, kostet aber durch Volumen und Preis am meisten. Genau das
# ist Muster "teuer trotz normaler Quote".
STYLES = [
    ("HOOD-CL", "Hoodie Classic", 69.90, 21.0, 0.30, 1.0, 4),
    ("HOOD-ZP", "Zip-Hoodie Heavy", 89.90, 28.0, 0.11, 2.5, 2),
    # Duenne Marge (30 Prozent): kippt schon bei normaler Retourenquote ins Minus.
    # Das ist Muster "verdient brutto, nach Retouren nichts mehr".
    ("JKT-RN", "Regenjacke Tech", 119.90, 84.00, 0.25, 1.0, 2),
    ("TEE-BAS", "T-Shirt Basic", 29.90, 7.5, 0.14, 1.2, 4),
    ("TEE-OVS", "T-Shirt Oversized", 34.90, 9.0, 0.16, 1.0, 4),
    ("KLEID-PR", "Sommerkleid Print", 79.90, 24.0, 0.24, 1.0, 4),
    ("JOG-CL", "Jogger Classic", 64.90, 19.5, 0.18, 1.0, 4),
    ("SOCK-3P", "Sneaker Socken 3er-Pack", 19.90, 4.8, 0.05, 1.0, 4),
    ("CAP-LG", "Cap Logo", 24.90, 6.0, 0.04, 0.8, 4),
]
STYLE_WEIGHTS = [s[5] for s in STYLES]

# Anteil der Retouren, bei denen im ERP kein brauchbarer Grund erfasst wurde.
# Realistisch und im Report ein eigener Befund, weil sich dahinter Faelle verstecken.
P_KEIN_GRUND = 0.14

PAYMENTS = [("Rechnungskauf", 0.30), ("PayPal", 0.32), ("Kreditkarte", 0.22), ("Vorkasse", 0.16)]
CHANNELS = [("Eigener Shop", 0.62), ("Amazon", 0.26), ("Zalando", 0.12)]

REASONS_BASE = [
    ("Zu klein", 0.16), ("Zu gross", 0.15), ("Gefaellt nicht", 0.27),
    ("Entspricht nicht dem Foto", 0.07), ("Mangelhafte Qualitaet", 0.07),
    ("Beschaedigt angekommen", 0.05), ("Falscher Artikel", 0.04),
    ("Nicht mehr benoetigt", 0.13), ("Zu spaet geliefert", 0.06),
]


def pick(weighted):
    r = random.random()
    acc = 0.0
    for value, w in weighted:
        acc += w
        if r <= acc:
            return value
    return weighted[-1][0]


def gen():
    sales, returns = [], []
    return_no = 4200
    serial_customer = "K-10442"

    for i in range(5200):
        order_no = f"AB-2026-{10000 + i}"
        order_date = START + timedelta(days=random.randrange(DAYS))
        customer = serial_customer if random.random() < 0.004 else f"K-{random.randrange(10000, 19999)}"
        payment = pick(PAYMENTS)
        channel = pick(CHANNELS)
        n_positions = random.choices([1, 2, 3], weights=[62, 28, 10])[0]

        # Bracketing: Serien-Kundin bestellt fast immer zwei Groessen desselben Artikels
        bracketing = customer == serial_customer or random.random() < 0.06

        order_positions = []
        for _ in range(n_positions):
            code, name, price, cost, ret_p, _w, n_colors = random.choices(
                STYLES, weights=STYLE_WEIGHTS)[0]
            color = random.choice(COLORS[:n_colors])
            sizes = random.sample(SIZES, 2) if bracketing else [random.choice(SIZES)]
            for size in sizes:
                sku = f"{code}-{size}-{color[:3].upper()}"
                qty = 1
                order_positions.append({
                    "sales_order_number": order_no,
                    "order_date": order_date.strftime("%Y-%m-%d"),
                    "channel": channel, "customer_number": customer,
                    "payment_method": payment, "product_number": sku,
                    "product_name": name, "variant_size": size, "variant_color": color,
                    "quantity": qty, "unit_price": price,
                    "net_revenue": round(price * qty, 2), "unit_cost": cost,
                })
        sales.extend(order_positions)

        # --- Muster 5: nicht abgeholte Sendung (ganze Bestellung), Rechnungskauf-lastig
        p_nonpickup = 0.055 if payment == "Rechnungskauf" else 0.008
        if random.random() < p_nonpickup:
            rdate = order_date + timedelta(days=random.randrange(12, 22))
            if rdate <= CUTOFF:
                return_no += 1
                for pos in order_positions:
                    returns.append(_ret(return_no, rdate, pos, "", "Sonstiges", "nicht_abgeholt"))
            continue

        # --- normale Retouren je Position
        for pos in order_positions:
            style = pos["product_name"]
            base_p = next(s[4] for s in STYLES if s[1] == style)
            p = base_p
            if customer == serial_customer:
                p = 0.85
            if random.random() >= p:
                continue
            # Latenz breit gestreut: die meisten Retouren kommen schnell, ein Teil spaet
            rdate = order_date + timedelta(days=random.choices(
                [random.randrange(4, 20), random.randrange(20, 45), random.randrange(45, 75)],
                weights=[55, 30, 15])[0])
            if rdate > CUTOFF:
                continue  # diese Retoure ist zum Datenstand noch nicht eingetroffen
            return_no += 1

            # Muster 1: Hoodie Classic faellt klein aus
            if style == "Hoodie Classic" and random.random() < 0.62:
                reason = "Zu klein"
            # Muster 3: Sommerkleid Print sieht anders aus als das Foto
            elif style == "Sommerkleid Print" and random.random() < 0.55:
                reason = random.choice(["Entspricht nicht dem Foto", "Farbe weicht ab"])
            # Muster 2: Chargen-Defekt Socken im April
            elif style == "Sneaker Socken 3er-Pack" and rdate.month == 4:
                reason = "Mangelhafte Qualitaet"
            else:
                reason = pick(REASONS_BASE)
            # Muster 6: bei einem Teil der Retouren wurde kein Grund erfasst
            if random.random() < P_KEIN_GRUND:
                reason = ""
            returns.append(_ret(return_no, rdate, pos, reason, _cat(reason), "kundenretoure"))

    # Chargen-Spike verstaerken: zusaetzliche Defekt-Retouren Socken im April
    april_orders = [s for s in sales if s["product_name"] == "Sneaker Socken 3er-Pack"
                    and s["order_date"] >= "2026-03-10" and s["order_date"] <= "2026-04-20"]
    for pos in random.sample(april_orders, min(28, len(april_orders))):
        return_no += 1
        rdate = datetime.strptime(pos["order_date"], "%Y-%m-%d") + timedelta(days=random.randrange(5, 20))
        if rdate.month != 4:
            rdate = datetime(2026, 4, random.randrange(3, 28))
        returns.append(_ret(return_no, rdate, pos, "Mangelhafte Qualitaet", "Gutschrift", "kundenretoure"))

    return sales, returns


def _cat(reason):
    return {"Mangelhafte Qualitaet": "Gutschrift", "Beschaedigt angekommen": "Ersatzlieferung",
            "Falscher Artikel": "Ersatzlieferung"}.get(reason, "Gutschrift")


def _ret(no, rdate, pos, reason, category, rtype):
    if hasattr(rdate, "strftime"):
        rdate = rdate.strftime("%Y-%m-%d")
    return {
        "return_number": f"RT-2026-{no}",
        "return_date": rdate,
        "status": "freigegeben", "progress": "eingegangen",
        "sales_order_number": pos["sales_order_number"],
        "channel": pos["channel"], "customer_number": pos["customer_number"],
        "payment_method": pos["payment_method"],
        "product_number": pos["product_number"], "product_name": pos["product_name"],
        "variant_size": pos["variant_size"], "variant_color": pos["variant_color"],
        "quantity_returned": pos["quantity"],
        "return_reason": reason, "return_reason_category": category,
        "refund_amount": pos["net_revenue"], "return_type": rtype,
    }


def write(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    sales, returns = gen()
    write("demo/verkaeufe.csv", sales)
    write("demo/retouren.csv", returns)
    print(f"OK: {len(sales)} Verkaufs-Positionen, {len(returns)} Retouren-Positionen")
