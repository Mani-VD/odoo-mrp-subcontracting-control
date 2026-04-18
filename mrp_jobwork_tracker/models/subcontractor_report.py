from odoo import models, fields, api, _,tools


class SubcontractorStockReport(models.Model):
    _name = 'subcontractor.stock.report'
    _auto = False # This tells Odoo it's a PostgreSQL view, not a table

    product_id = fields.Many2one('product.product', string="Product", readonly=True)
    location_id = fields.Many2one('stock.location', string="Vendor", readonly=True)
    quantity = fields.Float(string="Quantity at Vendor", readonly=True)
    total_value = fields.Float(string="Inventory Value", readonly=True)

    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        print("auto trig")
        self._cr.execute("""
           CREATE OR REPLACE VIEW subcontractor_stock_report AS (
                SELECT 
                    min(sq.id) as id,
                    sq.product_id,
                    sq.location_id,
                    sum(sq.quantity) as quantity,
                    sum(sq.quantity * pt.list_price) as total_value
                FROM stock_quant sq
                JOIN stock_location sl ON sq.location_id = sl.id
                JOIN product_product pp ON sq.product_id = pp.id
                JOIN product_template pt ON pp.product_tmpl_id = pt.id
                WHERE sq.quantity != 0 
                  AND (sl.usage = 'supplier' OR sl.complete_name ILIKE '%Subcontracting%')
                GROUP BY sq.product_id, sq.location_id
            )
        """)
