from flask import Flask
from flask import request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

access_token = 'pjt2mwWgtnIgFEwE3layGPf13RN8jBGatv7Wh7OvJgbuL8E5HB1NlTh3ha0uqiysFLt2SwR/D535+2nIoh3lyUa8AGocShVb4Y/iXpBrTjKFBFUGydqJcqC3YsYnJfEnjzes3NutRK9k93nzF0f9FAdB04t89/1O/w1cDnyilFU='
secret = '862f1acca7a513d40e0828e00dd129ce'

line_bot_api = LineBotApi(access_token)
handler = WebhookHandler(secret)

@app.route("/callback", methods=['POST'])
def callback():

    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))


if __name__ == '__main__':
    app.run()
