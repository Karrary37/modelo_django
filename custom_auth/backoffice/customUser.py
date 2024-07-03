from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from import_export import resources

from core.rabbit.publisher import RabbitMQPublisher
from core.tasks import celery_teste
from custom_auth.models import UserProfile


class UserResource(resources.ModelResource):
    class Meta:
        model = UserProfile
        fields = (
            'id',
            'identifier',
            'name',
            'email',
        )
        import_id_fields = ['id']


class CustomUserAdmin(UserAdmin):
    resource_class = UserResource

    # override the default sort column
    ordering = ('name',)
    # if you want the date they joined or other columns displayed in the list,
    # override list_display too
    search_fields = (
        'identifier',
        'name',
        'email',
    )
    list_display = (
        'identifier',
        'name',
        'email',
    )

    fieldsets = (
        (None, {'fields': ('identifier', 'password')}),
        (
            _('Personal info'),
            {
                'fields': (
                    'name',
                    'email',
                )
            },
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            },
        ),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            },
        ),
    )

    @admin.action(
        description='Teste no Celery',
    )
    def celery_test(self, request, queryset):
        celery_teste.delay(1)

    @admin.action(
        description='Publisher RabbitMQ',
    )
    def test_rabbitmq_publisher(self, request, queryset):
        publisher = RabbitMQPublisher()

        publisher.connect()
        publisher.declare_exchange(
            exchange_name="data_exchange"
        )

        message = {"teste": "teste"}
        publisher.publish_message(
            exchange_name="data_exchange",
            routing_key="",
            message=message
        )

    actions = [celery_test, test_rabbitmq_publisher]
