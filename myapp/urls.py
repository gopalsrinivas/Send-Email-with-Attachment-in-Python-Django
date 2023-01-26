from django.urls import path
from myapp.views import EmailAttachementView

urlpatterns = [
    path("send_email/", EmailAttachementView.as_view(), name='emailattachment'),
]
