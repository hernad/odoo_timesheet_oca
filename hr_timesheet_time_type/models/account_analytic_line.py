
from odoo import fields, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    time_type_id = fields.Many2one(
        comodel_name="project.time.type",
        string="Time Type",
    )
    time_type_name = fields.Char(
        related="time_type_id.name",
        string="Time Type Name",
    )
