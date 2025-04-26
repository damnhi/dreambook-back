from django.urls import path
from .views import ReservationListCreateAPIView, ReservationDetailAPIView, CancelReservationAPIView

urlpatterns = [
    path('', ReservationListCreateAPIView.as_view(), name='reservation-list-create'),
    path('<int:pk>/', ReservationDetailAPIView.as_view(), name='reservation-detail'),
    path('<int:pk>/cancel/', CancelReservationAPIView.as_view(), name='reservation-cancel'),
]
