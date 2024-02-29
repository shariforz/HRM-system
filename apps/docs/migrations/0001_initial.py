# Generated by Django 4.1.5 on 2024-02-29 13:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('corecode', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocBulkUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_uploaded', models.DateTimeField(auto_now=True)),
                ('csv_file', models.FileField(upload_to='docs/bulkupload/')),
            ],
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_status', models.CharField(choices=[('active', 'Действующий'), ('inactive', 'Архив')], default='active', max_length=10, verbose_name='Статус')),
                ('serial', models.CharField(max_length=200, verbose_name='Серия')),
                ('number', models.CharField(max_length=200, verbose_name='Номер №')),
                ('date_of_issue', models.DateField(default=django.utils.timezone.now, verbose_name='Дата выдачи')),
                ('date_of_preparing', models.DateField(default=django.utils.timezone.now, verbose_name='Начать оформить до')),
                ('date_of_expiry', models.DateField(default=django.utils.timezone.now, verbose_name='Действует до')),
                ('issued_authority', models.CharField(max_length=200, verbose_name='Кем выдан')),
                ('address', models.TextField(blank=True, verbose_name='Адрес в РФ')),
                ('others', models.TextField(blank=True, verbose_name='Другие')),
                ('scanned_doc', models.FileField(blank=True, upload_to='docs/uploads/', verbose_name='Загрузить файл')),
                ('doc_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corecode.documenttype', verbose_name='Тип документа')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee', verbose_name='Сотрудник')),
            ],
            options={
                'ordering': ['current_status'],
            },
        ),
    ]
