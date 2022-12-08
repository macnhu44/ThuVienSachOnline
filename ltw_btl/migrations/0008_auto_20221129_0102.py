# Generated by Django 3.2.13 on 2022-11-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ltw_btl', '0007_alter_customer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, choices=[('Sách Giáo Khoa', 'Sách Giáo Khoa'), ('Tiểu Thuyết', 'Tiểu Thuyết'), ('Truyện Tranh', 'Truyện Tranh')], default='sgk', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='number_of_pages',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='release_date',
            field=models.DateTimeField(blank=True, max_length=200),
        ),
    ]