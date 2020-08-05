# Generated by Django 3.0.8 on 2020-08-05 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='isbn',
            field=models.CharField(default=None, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='published_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='books',
            name='total_pages',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
