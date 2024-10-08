##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _compute_sale_checkbook(self):
        super()._compute_sale_checkbook()
        for order in self.filtered(lambda x: x.type_id and x.type_id.sale_checkbook_id):
            order.sale_checkbook_id = order.type_id.sale_checkbook_id

    @api.onchange('type_id')
    def _onchange_sale_checkbook_id(self):
        if self.type_id and self.type_id.sale_checkbook_id:
            self.sale_checkbook_id = self.type_id.sale_checkbook_id

    def write(self, vals):
        """A sale checkbook could have a different order sequence, so we could
        need to change it accordingly"""
        if self.env.user.has_group('l10n_ar_sale.use_sale_checkbook') and vals.get('sale_checkbook_id'):
            sale_checkbook = self.env['sale.checkbook'].browse(vals['sale_checkbook_id'])
            if sale_checkbook.sequence_id:
                for record in self:
                    if record.sale_checkbook_id != sale_checkbook and (
                        record.state in {"draft", "sent"}
                        and record.type_id.sequence_id != sale_checkbook.sequence_id
                    ):
                        new_vals = vals.copy()
                        new_vals["name"] = sale_checkbook.sequence_id._next() or _('New')
                        super(SaleOrder, record).write(new_vals)
                    else:
                        super(SaleOrder, record).write(vals)
                return True
        return super().write(vals)
