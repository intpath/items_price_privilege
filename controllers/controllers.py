# -*- coding: utf-8 -*-
# from odoo import http


# class ItemsPricePrivilege(http.Controller):
#     @http.route('/items_price_privilege/items_price_privilege/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/items_price_privilege/items_price_privilege/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('items_price_privilege.listing', {
#             'root': '/items_price_privilege/items_price_privilege',
#             'objects': http.request.env['items_price_privilege.items_price_privilege'].search([]),
#         })

#     @http.route('/items_price_privilege/items_price_privilege/objects/<model("items_price_privilege.items_price_privilege"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('items_price_privilege.object', {
#             'object': obj
#         })
