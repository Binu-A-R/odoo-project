{
    'name': 'Pos session wise discount limit',
    'version': '16.0.1.0.0',
    'category': 'Pos session wise discount limit',
    'sequence': '1',
    'depends': [
        'base', 'point_of_sale'
    ],
    'data': [
        'views/config_setting_pos__discount_limit.xml'

    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_category_discount_limit/static/src/js/pos_extend.js'
        ],
    },
    'installable': True,
    'application': True
}
