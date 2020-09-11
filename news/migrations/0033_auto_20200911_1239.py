# Generated by Django 3.1 on 2020-09-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0032_auto_20200909_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='image_p',
            field=models.ImageField(blank=True, db_index=True, null=True, upload_to='media/articles', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='post',
            field=models.TextField(db_index=True, verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='tags',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='posts', to='news.Tag'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(db_index=True, max_length=120, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='status',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Видимость статьи'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, db_index=True, max_length=500, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, db_index=True, null=True, verbose_name='Дата Рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, db_index=True, max_length=30, verbose_name='Местоположение'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_avatar',
            field=models.ImageField(blank=True, db_index=True, default='media/avatar/default_img.png', null=True, upload_to='media/avatar', verbose_name='Аватар Профиля'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tittle',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]