# Generated by Django 3.1.6 on 2023-09-26 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.TextField()),
                ('url', models.TextField()),
                ('image_url', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('domain', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='UserUtmParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uid', models.CharField(max_length=255)),
                ('ctime', models.DateTimeField()),
                ('utm_campaign', models.CharField(blank=True, max_length=255, null=True)),
                ('utm_content', models.CharField(blank=True, max_length=255, null=True)),
                ('utm_medium', models.CharField(blank=True, max_length=255, null=True)),
                ('utm_source', models.CharField(blank=True, max_length=255, null=True)),
                ('client_ip_address', models.TextField(blank=True, null=True)),
                ('client_user_agent', models.TextField(blank=True, null=True)),
                ('source_url', models.TextField(blank=True, null=True)),
                ('utm_term', models.TextField(blank=True, null=True)),
                ('fbclid', models.TextField(blank=True, null=True)),
                ('gclid', models.TextField(blank=True, null=True)),
                ('gbraid', models.TextField(blank=True, null=True)),
                ('wbraid', models.TextField(blank=True, null=True)),
                ('irclickid', models.TextField(blank=True, null=True)),
                ('blogsource', models.CharField(blank=True, max_length=255, null=True)),
                ('ttclid', models.TextField(blank=True, null=True)),
                ('sccid', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductClick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uid', models.CharField(max_length=255)),
                ('click_source', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='clicks', to='product.product')),
            ],
        ),
    ]
