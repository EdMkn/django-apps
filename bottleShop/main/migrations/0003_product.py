# Generated by Django 5.2.3 on 2025-06-28 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_brand_color_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='product_imgs/')),
                ('slug', models.CharField(max_length=400)),
                ('detail', models.TextField()),
                ('specs', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.brand')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.color')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.size')),
            ],
        ),
    ]
