logger_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'std_format': {
            'format': '{asctime} - {levelname} - {name} - {message}',
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'std_format'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'filename': 'server.log',
            'formatter': 'std_format',
            'maxBytes': 10485760,
            'backupCount': 40,
            
        }
    },
    'loggers': {
        'server_logger': {
            'level': 'INFO',
            'handlers': ['file']
        },
        'maths_logger': {
            'level': 'WARNING',
            'handlers': ['file']
        },
        'parser_logger': {
            'level': 'WARNING',
            'handlers': ['file']
        }
        
    },
    
}
