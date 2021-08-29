from django.urls import path
import core.views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('sites/',v.sites, name='sites'),
    path('site/<int:site_id>/', v.site,name='site'),
    path('contact/', v.Contact.as_view(), name='contact'),
    path('aboutus/', v.about, name='about'),
    path('faq/',v.faq,name='faq'),
    path('service/<int:service_id>/',v.service,name='service'),
    path('subscribe/',v.subscribe,name='subscribe'),
    path('test/', v.test, name='test'),
]
