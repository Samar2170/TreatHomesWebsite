from django.urls import path
import tests.views as v


urlpatterns = [
    path('', v.home, name='home'),
]