{
    'name': "Latest Events Snippet",
    'version': '16.0.1.0.0',
    'summary': 'Snippet',
    'description': 'Snippet',
    'sequence': '1',
    'category': 'Latest events ',
    'depends': [
        'base', 'website', 'event_management'
    ],
    'data': [
        'views/snippet.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            '/event_management_snippet/static/src/xml/carousel.xml',
            '/event_management_snippet/static/src/js/snippet.js',
        ]

    },
    'installable': True,
    'application': True
}
