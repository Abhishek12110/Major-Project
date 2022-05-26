"""bakery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,include
# from froala_editor import views
from shop import views
from django.conf import settings
from django.conf.urls.static import static
from shop.views import detailpage,searchpage,checkoutpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('bread/', views.breadpage,name="breadpage"),
    path('about/', views.aboutpage,name="aboutpage"),
    path('cake/', views.cakepage,name="cakepage"),
    path('cookies/', views.cookiespage,name="cookiespage"),
    path('pastries/', views.pastriespage,name="pastriespage"),
    path('blog/', views.blogpage,name="blogpage"),
    path('cart/', views.cartpage,name="cartpage"),
    path('search',searchpage.as_view(),name="searchpage"),
    path('login/', views.loginpage,name="loginpage"),
    path('logout', views.logout,name="logout"),
    path('register/', views.registerpage,name="registerpage"),
    path('orders/', views.orderspage,name="orderspage"),
    path('checkout/', checkoutpage.as_view(),name="checkoutpage"),
    path('contactus/', views.contactuspage,name="contactuspage"),
    path('detail/<int:id>/',detailpage.as_view(),name="detailpage"),
    # path('froala_editor/',include('froala_editor.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
