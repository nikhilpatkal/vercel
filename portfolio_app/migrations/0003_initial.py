# Generated by Django 4.2.6 on 2023-10-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portfolio_app', '0002_delete_backend_lang_delete_card_delete_core_lang_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='backend_lang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backend_img', models.ImageField(upload_to='static/')),
                ('backend_title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_img', models.ImageField(upload_to='static/')),
                ('card_title', models.TextField()),
                ('card_info', models.TextField()),
                ('card_button_text', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='core_lang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('core_img', models.ImageField(upload_to='static/')),
                ('core_title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='front_lang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_img', models.ImageField(upload_to='static/')),
                ('front_title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='hero_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_img', models.ImageField(upload_to='static/')),
            ],
        ),
        migrations.CreateModel(
            name='hero_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_info_first', models.TextField()),
                ('hero_info_secound', models.TextField()),
                ('hero_info_third', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='serviec_heading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_info', models.TextField()),
            ],
        ),
    ]