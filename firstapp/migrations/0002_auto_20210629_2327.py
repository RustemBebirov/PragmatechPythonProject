# Generated by Django 3.2.4 on 2021-06-29 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='Title')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Is published')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('title', '-created_at'),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=127, verbose_name='FullName')),
                ('email', models.EmailField(max_length=127, verbose_name='E-mail')),
                ('subject', models.CharField(max_length=127, verbose_name='Subject')),
                ('phone', models.IntegerField(verbose_name='Phone')),
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
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='Title')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Is published')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ('title', '-created_at'),
            },
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('title', '-created_at'), 'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='created_ad',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='updated_ad',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Is published'),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=160, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blog_images', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='short_description',
            field=models.CharField(max_length=127, verbose_name='Short description'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=127, verbose_name='Title'),
        ),
        migrations.CreateModel(
            name='Blog_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='firstapp.blog', verbose_name='Blog')),
                ('parrent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_comment', to='firstapp.blog_comment', verbose_name='Parent Comment')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(to='firstapp.Tag', verbose_name='Tag'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='firstapp.blog_category'),
        ),
    ]