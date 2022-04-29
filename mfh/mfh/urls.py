from django.contrib import admin
from django.urls import path, include

from mfh.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('budget_app/', include('mfh.budget_app.urls')),
]
