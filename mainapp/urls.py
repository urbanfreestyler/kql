from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name="services"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contacts/', views.contacts, name="contacts"),
    path('about/', views.about, name="about"),

    path('services/<int:id>/', views.services_more, name="services_more"),

    path('application/', views.application, name="application"),

    #UZ
    path('uz/', views.uz_index, name='uz_index'),
    path('uz/services/', views.uz_services, name="uz_services"),
    path('uz/portfolio/', views.uz_portfolio, name="uz_portfolio"),
    path('uz/contacts/', views.uz_contacts, name="uz_contacts"),
    path('uz/about/', views.uz_about, name="uz_about"),

    path('uz/services/<int:id>/', views.uz_services_more, name="uz_services_more"),


    #EN
    path('en/', views.en_index, name='en_index'),
    path('en/services/', views.en_services, name="en_services"),
    path('en/portfolio/', views.en_portfolio, name="en_portfolio"),
    path('en/contacts/', views.en_contacts, name="en_contacts"),
    path('en/about/', views.en_about, name="en_about"),

    path('en/services/<int:id>/', views.en_services_more, name="en_services_more"),
]