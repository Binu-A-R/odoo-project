{
    'name': 'Product Owner',
    'version': '16.0.1.0.0',
    'category': 'Product Owner',
    'sequence': '1',
    'depends': [
        'base', 'point_of_sale'
    ],
    'data': [
        'views/product_owner_views.xml'

    ],
    'assets': {
        'point_of_sale.assets': [
            'product_owner/static/src/js/receipt.js',
            'product_owner/static/src/xml/pos_receipt.xml',
        ],
    },
    'installable': True,
    'application': True
}
