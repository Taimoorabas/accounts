# Generated by Django 4.0.5 on 2022-09-28 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_subproduct_total_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subproduct',
            old_name='Total_Stock',
            new_name='Total_S',
        ),
    ]
