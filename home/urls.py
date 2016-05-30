from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'send_contact_mail/$', views.send_contact_mail, name='send_contact_mail'),
    url(r'faq/$', views.faq, name='faq'),
    url(r'our_team/$', views.our_team, name='our_team'),
]
