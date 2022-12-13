{
    'name': 'Tolerance',
    'version':'16.0.1.0.0',
    'category':'Tolerance',
    'sequence':'1',
    'depends': [
        'base','contacts','sale','purchase','stock'
    ],
    'data':[
        'security/ir.model.access.csv',
        'wizards/warning_wizard.xml',
        'views/tolerance_fields.xml',
        'views/tolerance_sale_order_line.xml',
        'views/tolerance_purchase_order_lines.xml',
        'views/tolerance_stock.xml',

    ],
    'installable': True,
    'application':True
}