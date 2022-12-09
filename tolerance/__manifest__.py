{
    'name': 'Tolerance',
    'version':'16.0.1.0.0',
    'category':'Tolerance',
    'sequence':'1',
    'depends': [
        'base','contacts','sale','purchase'
    ],
    'data':[
        'views/tolerance_fields.xml',
        'views/tolerance_sale_order_line.xml',
        'views/tolerance_purchase_order_lines.xml'

    ],
    'installable': True,

}