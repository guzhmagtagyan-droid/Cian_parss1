# Configuration settings for Flask app

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your_secret_key_here'

# Paths
class Paths:
    CIAN_PARSER_PATH = '/path/to/cian/parser/'
    DOWNLOADER_PATH = '/path/to/downloader/'
    WATERMARK_REMOVER_PATH = '/path/to/watermark/remover/'
    INPAINTING_PATH = '/path/to/inpainting/'
    OUTPUT_PATH = '/path/to/output/'

# Logging settings
class Logging:
    LOG_LEVEL = 'DEBUG'
    LOG_FILE = 'app.log'

