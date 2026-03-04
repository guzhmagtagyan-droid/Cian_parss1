# Configuration Settings for the Application

# App Secrets
SECRET_KEY = 'your-secret-key'

# Database Configuration
DATABASE = {
    'host': 'localhost',
    'port': 5432,
    'user': 'appuser',
    'password': 'your-password',
    'dbname': 'app_db'
}

# API Configuration
API_BASE_URL = 'https://api.yourservice.com'
API_TIMEOUT = 30  # seconds

# Logging Configuration
LOG_LEVEL = 'DEBUG'
LOG_FILE = 'app.log'

# Other Settings
ENABLE_FEATURE_X = True
MAX_RETRIES = 5
