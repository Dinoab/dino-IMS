# Generated by Django 4.2.6 on 2023-10-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_issueitem_issued_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issueitem',
            name='issued_amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]