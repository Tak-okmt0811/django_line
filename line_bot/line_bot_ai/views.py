from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Data #from line_bot_ai.models import Data
from django.utils import timezone #DateTimeField用timezone

from utils import message_creater
from line_bot_ai.line_message import LineMessage

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        print("プリント")
        print(request)
        data = request['events'][0]

        #各lineユーザー情報の保存
        user_id = data['source']['userId']
        text = data['message']['text']

        reply_token = data['replyToken']
        # 呼び出すキーワードによってテンプレートメッセージを変える
        if text == 'メニュー':
            line_message = LineMessage(message_creater.create_single_text_message(text)) 
        elif text == 'Plan A':
            #-db save の記載----
            #1.user_id , 2.text , 3.date
            # sample=Data(user_id="xyz",text="test",date=timezone.now())
            save_data = Data(user_id = user_id , text = text , date=timezone.now()) 
            save_data.save()
            # sample.save()
            # Data.objects.all()
            #------------------
            line_message = LineMessage(message_creater.confirm_message(text))

        line_message.reply(reply_token)
        return HttpResponse("ok")

