# -*- coding: utf-8 -*-
{
    'name': "hr_timesheet_work_type",

    'summary': """
        account_analytic_line work_type""",

    'description': """
        Timesheet's work type (standard, night, terrain)
    """,

    'author': "bring.out.ba",
    'website': "https://github.com/hernad",
    'license': "LGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Timesheet',
    'version': '1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_timesheet'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}
