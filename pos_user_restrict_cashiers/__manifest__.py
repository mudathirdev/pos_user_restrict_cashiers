# -*- coding: utf-8 -*-
{
    'name': "POS User Restrict Cashir",
    
    'summary': """
       Restrict user to see only allowed cashiers""",
    
    'description': """
        Restrict user to see only allowed cashiers
    """,
    'author': "Smart Tech",
    'category': 'POS',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'security/group.xml',
        'views/views.xml',
    ],
    'license': 'OPL-1',
    'images': ['static/description/icon.png'],
    
}
