# Generated by Django 4.0.3 on 2022-04-07 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import fitness.common.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('BMI', models.FloatField(default=0)),
                ('height', models.IntegerField(validators=[fitness.common.validators.validate_number_cannot_be_below_zero])),
                ('weight', models.FloatField(validators=[fitness.common.validators.validate_number_cannot_be_below_zero])),
                ('chest_size', models.IntegerField(validators=[fitness.common.validators.validate_number_cannot_be_below_zero])),
                ('biceps_size', models.FloatField(validators=[fitness.common.validators.validate_number_cannot_be_below_zero])),
                ('waist_size', models.IntegerField(validators=[fitness.common.validators.validate_number_cannot_be_below_zero])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
