# Generated by Django 3.2.4 on 2021-07-31 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=127, verbose_name='FullName')),
                ('email', models.EmailField(max_length=127, verbose_name='E-mail')),
                ('subject', models.CharField(max_length=127, verbose_name='Subject')),
                ('phone', models.CharField(max_length=127, verbose_name='Phone')),
                ('message', models.TextField(help_text='You can send your mesaage from here', verbose_name='Message')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ('-created_at',),
            },
        ),
    ]
