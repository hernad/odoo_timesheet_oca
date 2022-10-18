# -*- coding: utf-8 -*-

from odoo import models, fields


# class hr_timesheet_work_type(models.Model):
#     _name = 'hr_timesheet_work_type.hr_timesheet_work_type'
#     _description = 'hr_timesheet_work_type.hr_timesheet_work_type'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    work_type = fields.Selection(
        [
           ('standard', 'Standard'),
           ('night', 'Night'),
           ('terrain', 'Terrain')
        ],
        string='Work Type',
        default='standard',
        required=True,
    )

