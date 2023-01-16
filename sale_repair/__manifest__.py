{
    'name': 'Repair stock',
    'version': '16.0.1.0.0',
    'category': 'Repair',
    'sequence': '1',
    'depends': [
        'base', 'stock','sale', 'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/sale_repair.xml',
        'views/sale_boolean.xml',
        'data/sequence.xml'

    ],
    'installable': True,
    'application': True
}
