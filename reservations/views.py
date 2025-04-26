# views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class CancelReservationAPIView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_update(self, serializer):
        serializer.save(status='cancelled')
