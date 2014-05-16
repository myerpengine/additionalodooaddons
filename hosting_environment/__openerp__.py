# -*- coding: utf-8 -*-
{
    'name': 'Hosting Environment Configuration',
    'version': '1.0',
    'category': '',
    "sequence": 35,
    'complexity': "easy",
    'category': 'Hidden',
    'description': """
        Apply some changes to OpenERP's configuration to make it work better in hosting environment.
    """,
    'author': 'InfiniDev',
    'website': '',
    'depends': ["mail"],
    'init_xml': [],
    'update_xml': [
        "view.xml",
        "data.xml",
    ],
    'demo_xml': [],
    'test': [
    ],
    'qweb' : [
        "static/src/xml/hosting.xml",
    ],
    'installable': True,
    'auto_install': True,
}
