{
    'name': 'Approval Block',
    'version': '16.0.1.0.0',
    'category': 'Approval',
    'sequence': '1',
    'depends': [
        'base', 'purchase'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/approval_block_approval.xml',
        'views/approval_block_po.xml',
        'data/approval_data.xml'
    ],
    'installable': True,
    'application': True

}