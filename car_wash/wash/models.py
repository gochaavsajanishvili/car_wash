from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.functional import cached_property


class CarWash(models.Model):
    location = models.OneToOneField(to='Location', related_name='car_wash', on_delete=models.CASCADE)

    open_time = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(23)])
    close_time = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(23)])
    title = models.CharField(max_length=255)

    @cached_property
    def work_time(self):
        return f'{self.open_time} - {self.close_time}'

    def __str__(self):
        return f'{self.title} {self.work_time}'


class Garage(models.Model):
    car_wash = models.ForeignKey(to='CarWash', related_name='garages', on_delete=models.CASCADE)
    occupied = models.BooleanField(default=False)

    # def __str__(self):
    #     return f'Garage {}'


class WashPrice(models.Model):
    car_wash = models.ForeignKey(to='CarWash', on_delete=models.CASCADE)
    wash_type = models.ForeignKey(to='WashType', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=2)


class WashType(models.Model):
    car_washes = models.ManyToManyField(to='CarWash', through='WashPrice', related_name='wash_types')
    title = models.CharField(max_length=255)


class Washer(models.Model):
    car_wash = models.ForeignKey(to='CarWash', on_delete=models.CASCADE)

    full_name = models.CharField(max_length=255)
    wash_speed = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(200)])


class Location(models.Model):
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f'Location: {self.latitude} {self.longitude}'
