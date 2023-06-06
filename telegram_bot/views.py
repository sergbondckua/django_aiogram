import json
import logging

from asgiref.sync import async_to_sync
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from telegram_bot.webhook import proceed_update

logging.basicConfig(level=logging.DEBUG)


class IndexView(View):
    """View for index"""

    def get(self, request):
        return JsonResponse({"success": True, "code": 200})


class WebhookTelegramView(View):
    """Web hooks view for Telegram"""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request: HttpRequest):
        async_to_sync(proceed_update)(json.loads(request.body))
        return HttpResponse(status=200)

    def get(self, request: HttpRequest):
        return JsonResponse({"code": 204, "status": "No content"})
