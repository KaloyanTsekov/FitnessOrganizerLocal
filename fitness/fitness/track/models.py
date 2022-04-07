from django.contrib.auth import get_user_model
from django.db import models
from fitness.accounts.models import Profile, User
from fitness.common.validators import validate_number_cannot_be_below_zero


UserModel = get_user_model()


class Results(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    BMI = models.FloatField(default=0)

    height = models.IntegerField(
        validators=(
            validate_number_cannot_be_below_zero,)
    )

    weight = models.FloatField(
        validators=(
            validate_number_cannot_be_below_zero,)
    )

    chest_size = models.IntegerField(
        validators=(
            validate_number_cannot_be_below_zero,)
    )
    biceps_size = models.FloatField(
        validators=(
            validate_number_cannot_be_below_zero,
        )
    )
    waist_size = models.IntegerField(
        validators=(
            validate_number_cannot_be_below_zero,)
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
