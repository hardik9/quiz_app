# Generated by Django 2.2.6 on 2019-11-12 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrueFalseQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('answer', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=5)),
            ],
        ),
    ]
