{
    'name': 'Product Grade',
    'version': '16.0.1.0.0',
    'category': 'Product Grade',
    'sequence': '1',
    'depends': [
        'base', 'point_of_sale'
    ],
    'data': [
        'views/product_grade.xml'

    ],
    'assets': {
        'point_of_sale.assets': [
            'product_grade/static/src/js/receipt.js',
            'product_grade/static/src/xml/pos_receipt.xml',
        ],
    },
    'installable': True,
    'application': True
}
