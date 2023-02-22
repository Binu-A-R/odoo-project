{
    'name': 'Automated Sale Order',
    'version': '16.0.1.0.0',
    'summary': 'Creating a sale order from product view',
    'category': 'Automated Sale Order',
    'sequence': 1,
    'depends': [
        'base', 'sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/btn_so.xml',
        'wizards/create_so.xml'
    ],
    'installable': True,
    'application': True
}
