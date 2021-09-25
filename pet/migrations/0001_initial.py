# Generated by Django 3.2.7 on 2021-09-24 19:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=70)),
                ('name_pet', models.CharField(blank=True, max_length=70, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('published', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('adoption', models.BooleanField(default=False)),
                ('picture', models.ImageField(blank=True, upload_to='pets')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]