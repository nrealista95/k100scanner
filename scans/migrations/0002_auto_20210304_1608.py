# Generated by Django 3.0.5 on 2021-03-04 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='app_icon',
            field=models.ImageField(max_length=80, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='scan',
            name='app_name',
            field=models.CharField(default='app_name', max_length=50),
        ),
        migrations.CreateModel(
            name='NewScan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apk_file', models.FileField(null=True, upload_to='')),
                ('tool_selected', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
