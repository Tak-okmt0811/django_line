#メッセージ（ボタンテンプレート ）
def create_single_text_message(message):
    if message == 'ありがとう':
        message = 'どういたしまして！'
    

    test_message = [
                {
                "type": "template",
                "altText": "This is a buttons template",
                "template": {
                    "type": "buttons",
                    "thumbnailImageUrl": "https://www.shimay.uno/nekoguruma/wp-content/uploads/sites/2/2018/03/20171124_194201-508x339.jpg",
                    "imageAspectRatio": "rectangle",
                    "imageSize": "cover",
                    "imageBackgroundColor": "#FFFFFF",
                    "title": "Menu",
                    "text": "Please select",
                    "defaultAction": {
                        "type": "uri",
                        "label": "View detail",
                        "uri": "https://www.shimay.uno/nekoguruma/archives/620"
                    },
                    "actions": [
                        {
                            "type": "postback",
                            "label": "Buy",
                            "data": "action=buy&itemid=123"
                        },
                        {
                            "type": "postback",
                            "label": "Add to cart",
                            "data": "action=add&itemid=123"
                        },
                        {
                            "type": "uri",
                            "label": "View detail",
                            "uri": "https://www.shimay.uno/nekoguruma/archives/620"
                        }
                    ]
                }
                }
            ]
    return test_message


#テストメッセージ（おうむ返し）
# def create_single_text_message(message):
#     if message == 'ありがとう':
#         message = 'どういたしまして！'
#     test_message = [
#                 {
#                     'type': 'text',
#                     'text': message
#                 }
#             ]
#     return test_message