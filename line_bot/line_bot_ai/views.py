from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from utils import message_creater
from line_bot_ai.line_message import LineMessage

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        print(request)
        data = request['events'][0]
        print(data)
        message = data['message']
        print(message)
        reply_token = data['replyToken']
        print(reply_token)
        line_message = LineMessage(message_creater.create_single_text_message(message['text']))
        print(line_message)
        line_message.reply(reply_token)
        print('終了')
        return HttpResponse("ok")

