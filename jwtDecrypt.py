import os
import jwt
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'tcrc_back_end.settings'
application = get_wsgi_application()
from django.conf import settings



token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNDIxNjI3NywiaWF0IjoxNzE0MTI5ODc3LCJqdGkiOiIwMzAxMzkwZjIyNzc0N2EyYjllNGYyZjBmNDlmZTYzOCIsInVzZXJfaWQiOjJ9.rx0cVPFy-jMRL5AAHqmez5TmwCDffR1ze3_K4vruh0k'
secret_key = settings.SECRET_KEY

# Decode the token
decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])

# Print the claims
for key, value in decoded_token.items():
    print(f'{key}: {value}')