# Generated by Django 4.1.7 on 2024-05-11 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('unique_id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True, unique=True)),
                ('identifier', models.CharField(max_length=80, unique=True, verbose_name='Identificador')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Telefone')),
                ('cpf', models.CharField(blank=True, max_length=30, null=True, verbose_name='CPF')),
                ('is_premium', models.BooleanField(default=False, verbose_name='Assinatura ativa?')),
                ('device_id', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Device ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Identificação do endereço')),
                ('postal_code', models.CharField(blank=True, max_length=12, null=True, verbose_name='CEP')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Endereço')),
                ('address_neighborhood', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro')),
                ('address_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Número')),
                ('address_complement', models.CharField(blank=True, max_length=50, null=True, verbose_name='Complemento')),
                ('city', models.CharField(blank=True, max_length=40, null=True, verbose_name='Cidade')),
                ('state', models.CharField(blank=True, max_length=2, null=True, verbose_name='Estado')),
                ('is_principal', models.BooleanField(default=False, verbose_name='Endereço principal?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_address', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Usuário - Endereço',
                'verbose_name_plural': 'Usuários - Endereços',
            },
        ),
    ]
