# -*- coding: utf-8 -*-
# from odoo import http


# class CaseStudy(http.Controller):
#     @http.route('/case_study/case_study', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/case_study/case_study/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('case_study.listing', {
#             'root': '/case_study/case_study',
#             'objects': http.request.env['case_study.case_study'].search([]),
#         })

#     @http.route('/case_study/case_study/objects/<model("case_study.case_study"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('case_study.object', {
#             'object': obj
#         })

