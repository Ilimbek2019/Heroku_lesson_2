from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about')
]

"""
'home':   http://localhost:8888/
'about':  http://localhost:8888/about/
"""