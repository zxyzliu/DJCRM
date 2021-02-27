from django.urls import path
from .views import (
    lead_list, lead_detail, lead_create, lead_update, lead_delete,
    LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView
)

app_name = 'leads'
urlpatterns = [
    path('', LeadListView.as_view(), name='allList'),
    path('create/', LeadCreateView.as_view(), name='create'),
    path('<int:pk>/', LeadDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', lead_delete, name='delete')
]
