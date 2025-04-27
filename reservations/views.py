from rest_framework import generics
from .models import (
    Property, CancellationPolicy, SpecialOffer, GroupReservation, Reservation,
    ReservationDiscount, ReservationInvoice, ReservationPayment, ReservationNotification,
    ReservationReminder, ReservationExtension, ReservationModification, ReservationSupportTicket,
    ReservationOccupancy, RevenueReport, UserActivity, UserNotificationPreferences
)
from .serializers import (
    PropertySerializer, CancellationPolicySerializer, SpecialOfferSerializer, GroupReservationSerializer,
    ReservationSerializer, ReservationDiscountSerializer, ReservationInvoiceSerializer,
    ReservationPaymentSerializer, ReservationNotificationSerializer, ReservationReminderSerializer,
    ReservationExtensionSerializer, ReservationModificationSerializer, ReservationSupportTicketSerializer,
    ReservationOccupancySerializer, RevenueReportSerializer, UserActivitySerializer,
    UserNotificationPreferencesSerializer
)

# CRUD dla Property
class PropertyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

# CRUD dla SpecialOffer
class SpecialOfferListCreateAPIView(generics.ListCreateAPIView):
    queryset = SpecialOffer.objects.all()
    serializer_class = SpecialOfferSerializer

class SpecialOfferDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpecialOffer.objects.all()
    serializer_class = SpecialOfferSerializer

# CRUD dla Reservation
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

# Inne endpointy analogicznie... (rozszerz, remind, modify, support)


