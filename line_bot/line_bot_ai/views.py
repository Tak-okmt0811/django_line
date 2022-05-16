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
        data = request['events'][0]
        message = data['message']
        print('プリント')
        print(message['text'])
        reply_token = data['replyToken']
        # 呼び出すキーワードによってテンプレートメッセージを変える
        if message['text'] == 'メニュー':
            line_message = LineMessage(message_creater.create_single_text_message(message['text'])) 
        elif message['text'] == 'Plan A':
            line_message = LineMessage(message_creater.confirm_message(message['text']))


        line_message.reply(reply_token)
        return HttpResponse("ok")

