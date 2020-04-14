# Generated by Django 3.0.2 on 2020-03-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('body', models.TextField()),
                ('Image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]