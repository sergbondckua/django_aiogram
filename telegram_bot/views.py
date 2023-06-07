import json

from asgiref.sync import async_to_sync
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from telegram_bot.webhook import proceed_update


class IndexView(View):
    """View for index"""

    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"success": True, "code": 200})


class WebhookTelegramView(View):
    """
    A class representing a webhook view for handling incoming Telegram messages
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request: HttpRequest) -> HttpResponse:
        async_to_sync(proceed_update)(json.loads(request.body))
        return HttpResponse(status=200)

    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({"code": 204, "status": "No content"})
