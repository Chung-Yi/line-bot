import os
from flask import Flask
from flask import request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from dotenv import load_dotenv

app = Flask(__name__)


load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")
secret = os.getenv("CHANNEL_SECRET")

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
