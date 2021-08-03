# Generated by Django 3.2.4 on 2021-07-31 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='Title')),
                ('price', models.CharField(max_length=127, verbose_name='Price')),
                ('sale', models.CharField(blank=True, max_length=127, null=True, verbose_name='Sale price')),
                ('short_description', models.CharField(max_length=127, verbose_name='Short Description')),
                ('description', models.TextField(verbose_name='Description')),
                ('seller', models.CharField(max_length=127, verbose_name='Seller')),
                ('image', models.ImageField(upload_to='order_images', verbose_name='Image')),
                ('image1', models.ImageField(upload_to='order_images', verbose_name='Image')),
                ('image2', models.ImageField(upload_to='order_images', verbose_name='Image')),
                ('image3', models.ImageField(upload_to='order_images', verbose_name='Image')),
                ('image4', models.ImageField(upload_to='order_images', verbose_name='Image')),
                ('image5', models.ImageField(upload_to='order_images', verbose_name='Image')),
                ('image6', models.ImageField(upload_to='order_images', verbose_name='Image')),
                ('image7', models.ImageField(upload_to='order_images', verbose_name='Image')),
                ('image8', models.ImageField(upload_to='order_images', verbose_name='Image')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Is published')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Order_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=127, verbose_name='FullName')),
                ('email', models.EmailField(max_length=127, verbose_name='E-mail')),
                ('rating', models.IntegerField(verbose_name='Rating')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Is published')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='shop.order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Order comment',
                'verbose_name_plural': 'Order comments',
                'ordering': ('-created_at',),
            },
        ),
    ]