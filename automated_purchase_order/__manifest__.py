{
    'name': 'automated_purchase_order',
    'version': '16.0.1.0.0',
    'category': 'Automated Purchase Order',
    'summary': 'Creating a purchase order from Product views',
    'sequence': 1,
    'depends': [
        'base', 'purchase'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/btn_po.xml',
        'wizards/create_po.xml',
    ],
    'installable': True,
    'Application': True
}