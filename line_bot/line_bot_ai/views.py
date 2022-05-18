from re import I
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Menu,Id,Plan #Data #from line_bot_ai.models import Data
from django.utils import timezone #DateTimeField用timezone

from utils import message_creater
from line_bot_ai.line_message import LineMessage

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        # print("プリント")
        # print(request)
        data = request['events'][0]

        #各lineユーザー情報の保存
        user_Id = data['source']['userId']
        text = data['message']['text']

        reply_token = data['replyToken']
  
        if text == 'メニュー':
            line_message = LineMessage(message_creater.create_single_text_message(text)) 

        elif Menu.objects.filter(name = text).first(): #テンプレートで選択した項目が一つでもあると実行 (yes/No)
            # ex)Plan A入力
            line_message = LineMessage(message_creater.confirm_message(text)) # メッセージの送信

            # 【dBの処理】 入力値の保存ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

            # ① dB上のid有無の判定
            id = Id.objects.filter(user_id = user_Id, status=0).first() 
            print(id) #->True o None 
            if not id: 
                id = Id(user_id = user_Id) #なければ 変数order に格納
                id.save()

            # ② Plan の注文有無の判定
            menu = Menu.objects.filter(name=text).first() #Plan A
            
            plan = Plan.objects.filter(order=id, plan__name=text).first()
            if not plan: #なければ数量１で作成
                plan = Plan(order=id, plan=menu ,amount=1)
            else:
                plan.amount +=1 #複数回押すとその分カウント 
            plan.save()
        
        #ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

        elif text == 'yes':
            #集計結果の確認画面表示処理
            line_message = LineMessage(message_creater.single_message('注文を受け付けた。'))

        # elif text == 'Plan A':
        #-db save の記載----
            #1.user_id , 2.text , 3.date
            # save_data = Data(user_id = user_Id , text = text , date=timezone.now()) 
            # save_data.save()
            # Data.objects.all()
            #------------------
            

        line_message.reply(reply_token)
        return HttpResponse("ok")

