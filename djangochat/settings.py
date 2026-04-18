import os

# Security settings
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'default_secret_key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# Static files (CSS, JavaScript, Images)
# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Add additional security settings as required
# ...