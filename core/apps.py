from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'auth'
    verbose_name = '1. USUÁRIOS'


class CoreConfig(AppConfig):
    name = '$client'
    verbose_name = '2. CORE'
