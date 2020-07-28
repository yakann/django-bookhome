# Generated by Django 3.0.8 on 2020-07-28 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Publishers',
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('genre', models.CharField(max_length=255)),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.Genres')),
            ],
            options={
                'db_table': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('total_pages', models.IntegerField(null=True)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=2, null=True)),
                ('isbn', models.CharField(max_length=13, null=True)),
                ('published_date', models.DateField(null=True)),
                ('publisher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.Publishers')),
            ],
            options={
                'db_table': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Book_Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.Books')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.Genres')),
            ],
            options={
                'db_table': 'Book_Genres',
            },
        ),
        migrations.CreateModel(
            name='Book_Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.Authors')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.Books')),
            ],
            options={
                'db_table': 'Book_Authors',
            },
        ),
    ]
