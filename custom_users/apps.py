from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_users'

# myproject/apps.py
from wagtail.users.apps import WagtailUsersAppConfig


class CustomUsersAppConfig(WagtailUsersAppConfig):
    user_viewset = "custom_users.viewsets.UserViewSet"