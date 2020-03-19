# SendGrid

W BUDOWIE 

### Konfiguracja

W **settings.py** dodajemy:

```python
SENDGRID_API_KEY = config('SENDGRID_API')

SENDGRID_SANDBOX_MODE_IN_DEBUG = False

EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"

DEFAULT_EMAIL_ADRESS = config('DEFAULT_EMAIL')
```

- W **views.py** :
 - importujemy
    from django.core.mail import send_mail
