from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", views.index),
    path("retrieve/", views.retrieve),
    path("create/", views.create),
    path("do_create/", views.do_create),
    path("update/<int:id>/", views.update),
    path("do_update/", views.do_update),
    path("delete/<int:id>/", views.delete),
    path("do_delete/", views.do_delete),
]
