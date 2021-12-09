# Generated by Django 3.2.9 on 2021-12-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_postmodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='postmodel',
            name='category',
            field=models.ManyToManyField(to='blog.Category'),
        ),
    ]
