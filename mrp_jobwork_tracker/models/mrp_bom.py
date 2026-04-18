from odoo import models, fields

class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    # Tolerance percentage (e.g., 2.0 for 2%)
    wastage_tolerance = fields.Float(string="Wastage Tolerance (%)", default=0.0)