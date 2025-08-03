from django.urls import path
from .views import ticket_list, ticket_create, ticket_update

urlpatterns = [
    path('', ticket_list, name='ticket_list'),
    path('ticket/new/', ticket_create, name='ticket_create'),
    path('ticket/<int:pk>/edit/', ticket_update, name='ticket_update'),
]
