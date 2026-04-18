from odoo import models, fields, api, _
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    wastage_approved = fields.Boolean(string="Wastage Approved", default=False, copy=False)

    def button_validate(self):
        for picking in self:
            # Check for incoming receipts from subcontractors
            if picking.picking_type_code == 'incoming' and picking.location_id.usage == 'supplier':
                for line in picking.move_ids: # Using move_ids is cleaner in v18
                    # Find the BoM for the finished product
                    bom = self.env['mrp.bom']._bom_find(line.product_id)[line.product_id]
                    
                    if bom and bom.type == 'subcontract' and bom.wastage_tolerance > 0:
                        # Odoo 18 field names:
                        # product_uom_qty is the Demand
                        # quantity is the Actual Done quantity
                        expected_qty = line.product_uom_qty
                        received_qty = line.quantity 
                        
                        if expected_qty > 0:
                            variance_pct = ((expected_qty - received_qty) / expected_qty) * 100
                            
                            if variance_pct > bom.wastage_tolerance and not picking.wastage_approved:
                                raise UserError(_(
                                    "High Wastage Detected! The variance is %.2f%%, but the allowed limit is %.2f%%. "
                                    "Please get approval from the Production Manager before validating."
                                ) % (variance_pct, bom.wastage_tolerance))
                            
        return super(StockPicking, self).button_validate()

    def action_approve_wastage(self):
        for record in self:
            if self.env.user.has_group('mrp.group_mrp_manager'):
                record.wastage_approved = True
            else:
                raise UserError(_("Only a Manufacturing Manager can approve high wastage."))