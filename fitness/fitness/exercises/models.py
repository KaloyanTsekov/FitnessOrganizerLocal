from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from fitness.common.validators import validate_only_letters_numbers_space, validate_number_cannot_be_below_zero


class Video(models.Model):
    MAX_LENGTH = 25
    MIN_LENGTH = 3
    LEGS = 'Legs'
    ARMS = 'Arms'
    SHOULDERS = 'Shoulders'
    CHEST = 'Chest'
    BACK = 'Back'
    ABS = 'ABS'
    CATEGORIES = [(x, x) for x in (ABS, ARMS, BACK, CHEST, LEGS, SHOULDERS,)]

    name = models.CharField(
        max_length=25,
        validators=(
            MinLengthValidator(MIN_LENGTH),
            validate_only_letters_numbers_space,)
        )
    youtube_link = models.URLField()

    category = models.CharField(
        max_length=max(len(x) for x, _ in CATEGORIES),
        choices=CATEGORIES,
    )
    def __str__(self):
        return f"{self.name} "

UserModel = get_user_model()


class Workout(models.Model):
    MAX_LENGTH_TEXT = 200
    MAX_LENGTH = 25
    MIN_LENGTH = 3
    LEGS = 'Legs'
    ARMS = 'Arms'
    SHOULDERS = 'Shoulders'
    CHEST = 'Chest'
    BACK = 'Back'
    ABS = 'ABS'
    CATEGORIES = [(x, x) for x in (ABS, ARMS, BACK, CHEST, LEGS, SHOULDERS,)]

    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'
    DAYS = [(x, x) for x in (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY,)]

    name = models.CharField(
        max_length=MAX_LENGTH,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        )
    )

    day = models.CharField(
        max_length=max(len(x) for x, _ in DAYS),
        choices=DAYS,
    )

    category = models.CharField(
        max_length=max(len(x) for x, _ in CATEGORIES),
        choices=CATEGORIES,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.name} "


class Exercise(models.Model):
    MAX_LENGTH = 25
    name = models.CharField(
        max_length=MAX_LENGTH
    )
    weight = models.IntegerField(
        validators=(
            validate_number_cannot_be_below_zero,)
    )
    series = models.IntegerField(
        validators=(
            validate_number_cannot_be_below_zero,)
    )
    reps = models.IntegerField(
        validators=(
            validate_number_cannot_be_below_zero,)
    )
    training = models.ForeignKey('Workout', on_delete=models.CASCADE)
