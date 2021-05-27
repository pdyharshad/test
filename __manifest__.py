# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hotel Management',
    'version': '0.1',
    'summary': 'Simple Hotel Management functions',
    'description': """This module is for training purpose on Hotel mangement
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hotel.xml',
        'views/order.xml'
    ],
    'installable': True,
    'auto_install': False
}
