# Input-Schema (system-agnostisch)

Zwei logische Tabellen, ein Join über die Bestellnummer. Der Skill mappt beliebige Export-Spalten auf dieses Schema, bevor gerechnet wird.

## Retouren-Positionen (eine Zeile je retournierte Position)

Pflicht: `return_number`, `sales_order_number`, `return_date`, `product_number`, `quantity_returned`, `return_reason` (roh, wird normalisiert).

Optional (schaltet Analysen frei): `variant_size`/`variant_color` (Größen-Läufer, Bracketing), `product_name`, `customer_number` (Serien-Retournierer), `payment_method`, `channel`, `return_type` (kundenretoure | nicht_abgeholt | annahme_verweigert), `refund_amount`/`refund_type` (Gamma-Quote, Recovery-Rate), `refund_date` (SLA), `delivered_date` (Wardrobing-Fenster), `condition` (A/B/entsorgt, Wertverlust real), `batch` (Chargen exakt), `reason_note` (Freitext-Clustering).

## Verkaufs-Positionen (Nenner, gleicher Zeitraum plus Rückgabefenster nach vorn)

Pflicht: `sales_order_number`, `order_date`, `product_number`, `quantity`, `net_revenue`.
Optional: `customer_number`, `payment_method`, `channel`, `variant_size`, `variant_color`, `unit_price`, `unit_cost` (Deckungsbeitrag nach Retouren).

## Kanonische Retourengründe

`zu_klein`, `zu_gross`, `passform_schnitt`, `farbe_optik_gefaellt_nicht`, `nicht_wie_beschrieben`, `qualitaet_defekt`, `transportschaden`, `falscher_artikel`, `zu_spaet_geliefert`, `reue_nicht_benoetigt`, `nicht_abgeholt_annahme_verweigert`, `sonstiges_unbekannt`.

Die Normalisierungstabelle im Script deckt deutsche ERP-Exporte und die Shopify-GraphQL-Enums (SIZE_TOO_SMALL, NOT_AS_DESCRIBED, ...) ab. Unbekannte Rohwerte landen in `sonstiges_unbekannt` und werden im Report als Mapping-Lücke ausgewiesen.

## System-Hinweise

- **Xentral:** Berichte-Export oder API (`/api/v1/returns`). Grund hängt an der Position, Größe/Farbe stecken in der Variante. Passt direkt.
- **Shopify:** kein nativer Retouren-CSV-Export; GraphQL-Abzug oder App-Export (Loop, Returnless). Gründe aus dem ReturnReason-Enum.
- **WooCommerce:** nativ nur Refunds ohne Gründe; Gründe erst mit RMA-Plugin. Ohne `reason` läuft die Rumpf-Analyse (Quoten, Kosten), der Report weist das aus.
