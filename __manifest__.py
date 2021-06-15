# -*- coding: utf-8 -*-
{
    'name': "Items price privilege",

    'summary': """
        This module will remove the item price fields from users who are not 
        authorized to see those fields.
        """,

    'description': """
        This module will remove the item price fields from users who are not 
        authorized to see those fields.
    """,

    'author': "Int-Path",
    'website': "http://www.int-path.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Privileges',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','stock_account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/product_template.xml',
        'security/security.xml',
        'views/menu_items.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
