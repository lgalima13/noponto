# Generated by Django 3.2.3 on 2021-05-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatopf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contatopf',
            name='email',
        ),
        migrations.AddField(
            model_name='precadastro',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
