import os

BACKEND_API_URL = os.getenv(
    'BACKEND_API_URL',
    'http://test_backend:8000/'
)
BACKEND_API_ENDPOINT = 'py/eval'
