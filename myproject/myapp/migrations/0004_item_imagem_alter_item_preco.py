# Generated by Django 4.2.1 on 2024-02-06 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_item_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='imagem',
            field=models.ImageField(null=True, upload_to='item_images/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]