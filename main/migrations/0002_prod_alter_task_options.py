# Generated by Django 4.0.3 on 2022-03-29 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=50, verbose_name='Наименование товара')),
                ('prod_price', models.IntegerField(verbose_name='Цена')),
                ('prod_task', models.TextField(verbose_name='Описание товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
    ]
