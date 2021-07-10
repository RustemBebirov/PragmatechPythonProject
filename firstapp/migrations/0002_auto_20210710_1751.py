# Generated by Django 3.2.4 on 2021-07-10 13:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='order_images', verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='image6',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='order_images', verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='image7',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='order_images', verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='image8',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='order_images', verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=160, unique_for_date='created_at', verbose_name='Slug'),
        ),
    ]