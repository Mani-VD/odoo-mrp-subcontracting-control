# -*- coding: utf-8 -*-
{
    'name': 'Industrial Job-Work & Wastage Tracker',
    'version': '1.0',
    'summary': 'Manage subcontractor wastage tolerance and vendor stock value.',
    'description': """
        Customized for Coimbatore/Tiruppur Manufacturing:
        - Adds Wastage Tolerance % to BoM.
        - Blocks validation of subcontractor receipts exceeding tolerance.
        - Provides a real-time report of inventory value sitting at vendor locations.
    """,
    'category': 'Manufacturing',
    'author': 'V Manikandan',  # Your name for the portfolio
    'website': 'https://yourportfolio.com', # Replace with your LinkedIn or GitHub
    'depends': [
        'base', 
        'mrp', 
        'purchase',
        'stock', 
        'mrp_subcontracting'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/mrp_bom_view.xml',
        'views/stock_picking_view.xml',
        'views/report_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}