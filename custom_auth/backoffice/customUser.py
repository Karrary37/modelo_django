from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from import_export import resources

from core.rabbit.consumer import RabbitmqConsumer, minha_callback
from core.rabbit.publisher import RabbitmqPublisher, publicar_mensagem_rabbitmq
from core.tasks import celery_teste
from custom_auth.models import UserProfile
from django.contrib import admin


# from import_export.admin import ImportExportModelAdmin


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
        print('ppppppppp')
        celery_teste.delay(1)
        print('nnnnnnnnnn')

    @admin.action(
        description='Teste no Publisher RabbitMQ',
    )
    def test_rabbitmq_publisher(self, request, queryset):
        rabbitmq_publisher = RabbitmqPublisher()
        rabbitmq_publisher.send_message({"ola": "mundo"})

    @admin.action(
        description='Teste no Publisher RabbitMQ 2',
    )
    def test_rabbitmq_publisher(self, request, queryset):
        publicar_mensagem_rabbitmq()
    @admin.action(
        description='Teste no Consumer RabbitMQ',
    )
    def test_rabbitmq_consumer(self, request, queryset):
        rabitmq_consumer = RabbitmqConsumer()
        rabitmq_consumer.start()

    actions = [celery_test, test_rabbitmq_publisher, test_rabbitmq_consumer]
