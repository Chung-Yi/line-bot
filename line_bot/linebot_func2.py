import os
from flask import Flask
from flask import request, abort
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, AudioSendMessage, messages
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models.send_messages import VideoSendMessage
from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")
secret = os.getenv("CHANNEL_SECRET")


line_bot_api = LineBotApi(access_token)
handler = WebhookHandler(secret)

baseurl = 'https://c2ef-61-228-222-149.ngrok.io/static/'

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
    mtext = event.message.text
    if mtext == "@傳送聲音":
        try:
            message = AudioSendMessage(original_content_url=baseurl + 'mario.m4a', duration=20000)
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "發生錯誤!!"))
    
    elif mtext == "@傳送影片":
        try:
            message = VideoSendMessage(original_content_url=baseurl + 'robot.mp4', preview_image_url=baseurl + 'robot.jpg')
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "發生錯誤!!"))


if __name__ == '__main__':
    app.run()