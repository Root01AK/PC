"""
URL configuration for newpc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pcapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('mission/',views.mission,name='mission'),
    path('vission/',views.vission,name='vission'),
    path('casesummery/',views.casesummery,name='casesummery'),
    path('contramgmt/',views.contramgmt,name='contramgmt'),
    path('leasebtrac/',views.leasebtrac,name='leasebtrac'),
    path('legaldoc/',views.legaldoc,name='legaldoc'),
    path('legaltraining/',views.legaltraining,name='legaltraining'),
    path('trainingcompani/',views.trainingcompani,name='trainingcompani'),
    path('legalaudit/',views.legalaudit,name='legalaudit'),
    path('team/',views.team,name='team'),
    path('sanjay/',views.sanjay,name='sanjay'),
    path('jatin/',views.jatin, name='jatin'),
    path('ezhil/',views.ezhil,name='ezhil'),
    path('udaya/',views.udaya,name='udaya'),
    path('uma/',views.uma,name='uma'),
    path('privacypolicy/', views.privacypolicy,name='privacypolicy'),
    path('terms/',views.terms,name='terms'),
    path('contact/',views.contact,name='contact'),
    path('leaseabtrac/',views.leaseabtrac,name='leaseabtrac'),
    path('success/',views.success,name='success'),
    path('event/',views.event,name='event'),
    path('one/',views.one,name='one'),
    path('book_appointment/', views.book_appointment, name='book_appointment')
]
