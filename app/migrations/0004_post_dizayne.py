# Generated by Django 4.2.4 on 2023-08-11 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_category_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_Dizayne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('info', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
    ]
