uri="https://f3da-60-66-43-108.jp.ngrok.io"
image01 = uri + "/media/media/img1.JPG"
image02 = uri + "/media/media/img2.png"

#メッセージ（ボタンテンプレート ）==============================================
def create_single_text_message(message): #message
    #if message == 'メニュー':
    message = [ 
                {
                "type": "template",
                "altText": "this is a carousel template",
                "template": {
                    "type": "carousel",
                    "columns": [
                        {
                            "thumbnailImageUrl": image01,
                            "imageBackgroundColor": "#FFFFFF",
                            "title": "MENU1",
                            "text": "description",
                            "defaultAction": {
                                "type": "uri",
                                "label": "View detail",
                                "uri": "https://www.shimay.uno/nekoguruma/archives/620"
                            },
                            "actions": [
                                {
                                    "type": "message",
                                    "label": "Plan A",
                                    "text": "Plan A"
                                },
                                {
                                    "type": "message",
                                    "label": "Plan B",
                                    "text": "Plan B"
                                },
                                {
                                    "type": "message",
                                    "label": "Plan C",
                                    "text": "Plan C"
                                }
                            ]
                        },
                        {
                            "thumbnailImageUrl": image01,
                            "imageBackgroundColor": "#000000",
                            "title": "this is menu",
                            "text": "description",
                            "defaultAction": {
                                "type": "uri",
                                "label": "View detail",
                                "uri": "https://www.shimay.uno/nekoguruma/archives/620"
                            },
                            "actions": [
                                {
                                    "type": "postback",
                                    "label": "Plan A ",
                                    "data": "action=buy&itemid=222"
                                },
                                {
                                    "type": "postback",
                                    "label": "Plan B",
                                    "data": "action=add&itemid=222"
                                },
                                {
                                    "type": "uri",
                                    "label": "Plan C",
                                    "uri": "https://www.shimay.uno/nekoguruma/archives/620"
                                }
                            ]
                        },
                        {
                            "thumbnailImageUrl": image01,
                            "imageBackgroundColor": "#FFFFFF",
                            "title": "this is menu",
                            "text": "description",
                            "defaultAction": {
                                "type": "uri",
                                "label": "View detail",
                                "uri": "https://www.shimay.uno/nekoguruma/archives/620"
                            },
                            "actions": [
                                {
                                    "type": "postback",
                                    "label": "Buy",
                                    "data": "action=buy&itemid=111"
                                },
                                {
                                    "type": "postback",
                                    "label": "Add to cart",
                                    "data": "action=add&itemid=111"
                                },
                                {
                                    "type": "uri",
                                    "label": "View detail",
                                    "uri": "https://www.shimay.uno/nekoguruma/archives/620"
                                }
                            ]
                        },
                    ],
                    "imageAspectRatio": "rectangle",
                    "imageSize": "cover"
                }
                }
            ]
    return message

def confirm_message(message):
    message = [
        {
        "type": "template",
        "altText": "this is a confirm template",
        "template": {
            "type": "confirm",
            "text": "Are you sure?",
            "actions": [
                {
                    "type": "message",
                    "label": "Yes",
                    "text": "yes"
                },
                {
                    "type": "message",
                    "label": "No",
                    "text": "no"
                }
            ]
        }
        }
    ]
    return message

#テストメッセージ（おうむ返し）==============================================
# def single_message(message):
#     # if message == 'こんにちは':
#     #     message = 'こんちゃす'
#     test_message = [
#                 {
#                     'type': 'text',
#                     'text': message
#                 }
#             ]
#     return test_message


#動画カルーセルテンプレート==============================================
# def movie_message():
#     test_message = [
#         {
#             "type": "video",
#             "originalContentUrl": "https://example.com/original.mp4",
#             "previewImageUrl": "https://example.com/preview.jpg",
#             "trackingId": "track-id"
#         }
#     ]