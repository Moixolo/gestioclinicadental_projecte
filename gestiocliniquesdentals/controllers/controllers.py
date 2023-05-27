# -*- coding: utf-8 -*-
# from odoo import http


# class Gestiocliniquesdentals(http.Controller):
#     @http.route('/gestiocliniquesdentals/gestiocliniquesdentals', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestiocliniquesdentals/gestiocliniquesdentals/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestiocliniquesdentals.listing', {
#             'root': '/gestiocliniquesdentals/gestiocliniquesdentals',
#             'objects': http.request.env['gestiocliniquesdentals.gestiocliniquesdentals'].search([]),
#         })

#     @http.route('/gestiocliniquesdentals/gestiocliniquesdentals/objects/<model("gestiocliniquesdentals.gestiocliniquesdentals"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestiocliniquesdentals.object', {
#             'object': obj
#         })
