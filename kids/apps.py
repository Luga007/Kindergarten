from django.apps import AppConfig
from django.apps import AppConfig


class PeopleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kids    '

    def ready(self):
        import kids.signals



class KidsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kids'
