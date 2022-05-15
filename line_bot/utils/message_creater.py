uri="https://070f-60-66-42-32.jp.ngrok.io/media/media/img1.JPG"

#テストメッセージ（おうむ返し）==============================================
def single_message(message):
    # if message == 'こんにちは':
    #     message = 'こんちゃす'
    test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]
    return test_message

#メッセージ（ボタンテンプレート ）==============================================
def create_single_text_message(message):
    # if message == 'おはよう':
    test_message = [
                {
                "type": "template",
                "altText": "this is a carousel template",
                "template": {
                    "type": "carousel",
                    "columns": [
                        {
                            "thumbnailImageUrl": uri,
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
                        {
                            "thumbnailImageUrl": uri,
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
                                    "label": "Buy",
                                    "data": "action=buy&itemid=222"
                                },
                                {
                                    "type": "postback",
                                    "label": "Add to cart",
                                    "data": "action=add&itemid=222"
                                },
                                {
                                    "type": "uri",
                                    "label": "View detail",
                                    "uri": "https://www.shimay.uno/nekoguruma/archives/620"
                                }
                            ]
                        },
                        {
                            "thumbnailImageUrl": uri,
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
    return test_message

#画像カルーセルテンプレート==============================================
def img_message(message):
    test_message = [
        {
        "type": "template",
        "altText": "this is a carousel template",
        "template": {
            "type": "carousel",
            "columns": [
                {
                    "thumbnailImageUrl": uri,
                    "imageBackgroundColor": "#FFFFFF",
                    "title": "this is menu",
                    "text": "description",
                    "defaultAction": {
                        "type": "uri",
                        "label": "View detail",
                        "uri": "http://example.com/page/123"
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
                            "uri": "http://example.com/page/111"
                        }
                    ]
                },
                {
                    "thumbnailImageUrl": uri,
                    "imageBackgroundColor": "#000000",
                    "title": "this is menu",
                    "text": "description",
                    "defaultAction": {
                        "type": "uri",
                        "label": "View detail",
                        "uri": "http://example.com/page/222"
                    },
                    "actions": [
                        {
                            "type": "postback",
                            "label": "Buy",
                            "data": "action=buy&itemid=222"
                        },
                        {
                            "type": "postback",
                            "label": "Add to cart",
                            "data": "action=add&itemid=222"
                        },
                        {
                            "type": "uri",
                            "label": "View detail",
                            "uri": "http://example.com/page/222"
                        }
                    ]
                }
            ],
            "imageAspectRatio": "rectangle",
            "imageSize": "cover"
        }
        }]


#動画カルーセルテンプレート==============================================
def movie_message():
    test_message = [
        {
            "type": "video",
            "originalContentUrl": "https://example.com/original.mp4",
            "previewImageUrl": "https://example.com/preview.jpg",
            "trackingId": "track-id"
        }
    ]