
from django.urls import path
from .views import ListPostView, DetailedPostView


urlpatterns = [ 

        path('', ListPostView.as_view(), name='home_page')

        ]


