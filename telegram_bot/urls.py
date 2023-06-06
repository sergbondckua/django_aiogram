from django.urls import path
from telegram_bot import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("webhook/tg/", views.WebhookTelegramView.as_view(), name="webhook"),
]

app_name = "telegram_bot"
