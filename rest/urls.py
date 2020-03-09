

from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('fitnes/<int:servise_id>', views.get_rest )
    
]
