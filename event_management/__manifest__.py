{
    'name': 'Events Management',
    'version': '16.0.4.0.0',
    'category': 'Event Management',
    'sequence': '1',
    'summary': 'Managing online events and booking events',
    'description': 'Managing online events and booking events',
    'depends': [
        'base', 'mail', 'account_payment', 'website',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/event_views.xml',
        'views/event_booking.xml',
        'views/event_service.xml',
        'data/event_type_data.xml',
        'data/scheduled_action.xml',
        'data/event_service_data.xml',
        'data/event_website.xml',
        'views/catering.xml',
        'data/sequence.xml',
        'views/catering_menu.xml',
        'data/catering_menu_data.xml',
        'wizards/event_reporting.xml',
        'report/report_event.xml',
        'report/report_templete.xml',
        'views/website_template.xml'

    ],
    'assets': {
        'web.assets_backend': [
            'event_management/static/src/js/action_manager.js',
            'event_management/static/src/js/catering.js',

        ],
    },


'installable': True,
'application': True

}
