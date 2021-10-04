from django.db import models
from mainapp.students.studentModel import student
import enum
"""Transport Model"""
class transport(models.Model):
    transport_id = models.AutoField(primary_key=True)
    route_name = models.CharField(max_length=500, null=True, blank=True)
    number_of_vehicle = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    route_fare = models.BigIntegerField(null=True, blank=True)
    def __str__(self):
        return self.route_name


class SchoolBus(models.Model):
    bus_no = models.CharField(max_length=10, null=True, blank=True, unique=True)
    total_seats = models.IntegerField(null=True, blank=True)
    seats_available = models.BigIntegerField(null=True, blank=True)


class ReservationStatus(enum.Enum):
    Active = "Active"
    Inactive = "Inactive"

    @classmethod
    def choices(cls):
        return [(i, i.value) for i in cls]


status = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
)


class busReservation(models.Model):
    reservation_id = models.CharField(max_length=15, null=True)
    student = models.ForeignKey(student, on_delete=models.DO_NOTHING)
    bus = models.ForeignKey(SchoolBus, on_delete=models.DO_NOTHING)
    status =  models.CharField(max_length=10, blank=True, choices = status)
    