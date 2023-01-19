{
    'name': 'Contact creation from Survey',
    'version': '16.0.1.0.0',
    'category': 'Contact creation from Survey',
    'sequence': '1',
    'depends': [
        'base', 'survey'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/contact_creation.xml'

    ],
    'installable': True,
    'application': True
}