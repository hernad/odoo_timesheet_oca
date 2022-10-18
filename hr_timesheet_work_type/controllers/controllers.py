# -*- coding: utf-8 -*-
# from odoo import http


# class HrTimesheetWorkType(http.Controller):
#     @http.route('/hr_timesheet_work_type/hr_timesheet_work_type', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_timesheet_work_type/hr_timesheet_work_type/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_timesheet_work_type.listing', {
#             'root': '/hr_timesheet_work_type/hr_timesheet_work_type',
#             'objects': http.request.env['hr_timesheet_work_type.hr_timesheet_work_type'].search([]),
#         })

#     @http.route('/hr_timesheet_work_type/hr_timesheet_work_type/objects/<model("hr_timesheet_work_type.hr_timesheet_work_type"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_timesheet_work_type.object', {
#             'object': obj
#         })
