from odoo import api, models, fields, _
import datetime as dt

from datetime import datetime, date, time
import datetime
from datetime import timedelta


class sales_inherit(models.Model):
    _inherit = 'purchase.order'

    booking_date = fields.Date(String="Booking Date")
    duration = fields.Integer(STring="Validity Duration")

    @api.onchange('booking_date')
    def duration_set(self):
        for rec in self:
            if rec.booking_date:
                date = fields.Date.from_string(rec.booking_date)
                rec.duration = (date - fields.date.today()).days


class discounts(models.Model):
    _inherit = 'purchase.order.line'
    # _rec_name = 'discount_type'

    discount = fields.Float(string='Discount %')
    price_after = fields.Float(String = "Price After Discount")

    @api.onchange('discount')
    def total_set(self):
        for rec in self:
            # total = rec.price_subtotal
            dis = rec.discount/100
            rec.price_after = rec.price_subtotal*dis
            # rec.price_subtotal = rec.discount / 100 * rec.price_subtotal
class product_template_inherit(models.Model):
    _inherit = 'product.template'

    repair_condition = fields.Selection([('','')], string="Repair Condition")