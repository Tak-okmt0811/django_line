uri="https://7865-60-66-60-248.jp.ngrok.io"
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
                                    "type": "message",
                                    "label": "Plan X",
                                    "text": "Plan X"
                                },
                                {
                                    "type": "message",
                                    "label": "Plan Y",
                                    "text": "Plan Y"
                                },
                                {
                                    "type": "message",
                                    "label": "Plan Z",
                                    "text": "Plan Z"
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
                                    "type": "message",
                                    "label": "Plan Σ",
                                    "text": "Plan Σ"
                                },
                                {
                                    "type": "message",
                                    "label": "Plan Γ",
                                    "text": "Plan Γ"
                                },
                                {
                                    "type": "message",
                                    "label": "Plan β",
                                    "text": "Plan β"
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


#template_messageのアクションでタップでurlへ移動
# {
# "type": "uri",
# "label": "Plan β",
# "uri": "https://www.shimay.uno/nekoguruma/archives/620"
# }