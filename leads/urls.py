from django.urls import path
from .views import lead_list, lead_detail, lead_create, lead_update, lead_delete

urlpatterns = [
    path('', lead_list, name='allList'),
    path('create/', lead_create, name='create'),
    path('<int:pk>/', lead_detail, name='detail'),
    path('<int:pk>/update/', lead_update, name='edit'),
    path('<int:pk>/delete/', lead_delete, name='delete')
]