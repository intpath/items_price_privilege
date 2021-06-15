# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class items_price_privilege(models.Model):
#     _name = 'items_price_privilege.items_price_privilege'
#     _description = 'items_price_privilege.items_price_privilege'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
