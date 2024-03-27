# -*- coding: utf-8 -*-

from odoo import models, fields

class Employee(models.Model):
    _name = 'case_study.employee'
    _description = 'Case Study - Sample Employee Model'

    # Basic fields
    name = fields.Char(string='Name', required=True)
    work_phone = fields.Char(string='Work Phone')
    work_email = fields.Char(string='Work Email')

