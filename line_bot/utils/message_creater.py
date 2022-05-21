uri="https://efd1-60-66-46-106.jp.ngrok.io"
image01 = uri + "/media/media/img1.JPG"
image02 = uri + "/media/media/img2.png"
menu01 =  uri + "/media/media/menu01.jpg"
menu02 =  uri + "/media/media/menu02.jpg"
menu03 =  uri + "/media/media/menu03.jpg"

#メッセージ（ボタンテンプレート ）==============================================
def template_button_message(message): #message
    message = [ 
                {
                "type": "template",
                "altText": "this is a carousel template",
                "template": {
                    "type": "carousel",
                    "columns": [
                        {
                            "thumbnailImageUrl": menu01,
                            "imageBackgroundColor": "#FFFFFF",
                            "title": "this is title01",
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
                            "thumbnailImageUrl": menu02,
                            "imageBackgroundColor": "#000000",
                            "title": "this is title02",
                            "text": "description",
                            "defaultAction": {
                                "type": "uri",
                                "label": "View detail",
                                "uri": "https://www.shimay.uno/nekoguruma/archives/620"
                            },
                            "actions": [
                                {
                                    "type": "postback",
                                    "label": "Plan X ",
                                    "data": "action=buy&itemid=222"
                                },
                                {
                                    "type": "postback",
                                    "label": "Plan Y",
                                    "data": "action=add&itemid=222"
                                },
                                {
                                    "type": "uri",
                                    "label": "Plan Z",
                                    "uri": "https://www.shimay.uno/nekoguruma/archives/620"
                                }
                            ]
                        },
                        {
                            "thumbnailImageUrl": menu03,
                            "imageBackgroundColor": "#FFFFFF",
                            "title": "this is title03",
                            "text": "description",
                            "defaultAction": {
                                "type": "uri",
                                "label": "View detail",
                                "uri": "https://www.shimay.uno/nekoguruma/archives/620"
                            },
                            "actions": [
                                {
                                    "type": "postback",
                                    "label": "Plan Σ",
                                    "data": "action=buy&itemid=111"
                                },
                                {
                                    "type": "postback",
                                    "label": "Plan Γ",
                                    "data": "action=add&itemid=111"
                                },
                                {
                                    "type": "uri",
                                    "label": "Plan β",
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
                    "text": "Yes"
                },
                {
                    "type": "message",
                    "label": "No",
                    "text": "No"
                }
            ]
        }
        }
    ]
    return message

#テストメッセージ（おうむ返し）==============================================
def single_message(message):
    message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
    return message


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