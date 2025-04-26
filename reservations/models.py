from django.db import models
from django.conf import settings

class Property(models.Model):
    # uproszczony model nieruchomości
    title = models.CharField(max_length=200)
    address = models.TextField()

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Oczekuje'),
        ('confirmed', 'Potwierdzona'),
        ('cancelled', 'Anulowana'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

class CancellationPolicy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    refundable_until = models.DurationField()

class ReservationInvoice(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    issued_at = models.DateTimeField(auto_now_add=True)
