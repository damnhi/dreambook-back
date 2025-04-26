from rest_framework import serializers
from .models import Reservation, ReservationInvoice

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class ReservationInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationInvoice
        fields = '__all__'
