# Generated by Django 4.0.5 on 2022-08-31 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myworkcategory',
            name='image',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MyWorkImage',
        ),
    ]