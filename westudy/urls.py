from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view() ,name='home'),
    path('events/', views.EventsView.as_view(), name='events'),
    path('event_detail/<int:id>/', views.EventDetailView.as_view(), name='event_detail'),
]