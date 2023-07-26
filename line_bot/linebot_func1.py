import os
from flask import Flask
from flask import request, abort
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction
from linebot import LineBotApi, WebhookHandler
# from linebot.v3.webhook import WebhookHandler
from linebot.exceptions import InvalidSignatureError
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
    print('body: ', body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == "@傳送文字":
        try:
            message = TextSendMessage(
                text = "我是Line Bot，你好\n"
            )
            line_bot_api.reply_message(event.reply_token, message)
        
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "發生錯誤!!"))
    
    elif mtext == "@傳送圖片":
        try:
            message = ImageSendMessage(
                original_content_url = "https://onepage.nownews.com/sites/default/files/styles/thematic_content_img/public/2020-05/02_6.jpg?h=bd907a81&itok=3M7ec1X0",
                preview_image_url = "https://onepage.nownews.com/sites/default/files/styles/thematic_content_img/public/2020-05/02_6.jpg?h=bd907a81&itok=3M7ec1X0L"
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            error_message = ImageSendMessage(
                original_content_url = "https://techvig.net/wp-content/uploads/2020/11/Outlook-Error.jpeg",
                preview_image_url = "https://techvig.net/wp-content/uploads/2020/11/Outlook-Error.jpeg"
            )
            line_bot_api.reply_message(event.reply_token, error_message)
    
    elif mtext == "@傳送貼圖":
        try:
            message = StickerSendMessage(
                package_id  = "446",
                sticker_id  = "2027"
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "發生錯誤!!"))
    
    elif mtext == "@多項傳送":
        try:
            message = [
                StickerSendMessage(
                    package_id = "789",
                    sticker_id = "10881"
                ),
                TextSendMessage(
                    text = "Hi!!!!!!!!"
                ),
                ImageSendMessage(
                    original_content_url = "https://storage.googleapis.com/image.blocktempo.com/2020/10/meme-cultures-origin-17-years-old-4chan-3-750x375.png",
                    preview_image_url = "https://storage.googleapis.com/image.blocktempo.com/2020/10/meme-cultures-origin-17-years-old-4chan-3-750x375.png"
                )
            ]
            line_bot_api.reply_message(event.reply_token, message)
        
        except:
            line_bot_api.reply_message(reply_token, TextSendMessage(text = "發生錯誤!!"))
    
    elif mtext == "@傳送位置":
        try:
            message = LocationSendMessage(
                title = "101",
                address = "台北市信義路五段7號",
                latitude=25.034207, 
                longitude=121.564590  
            )
            line_bot_api.reply_message(event.reply_token, message)
        
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "發生錯誤!!"))
    
    elif mtext == "@快速選單":
        try:
            message = TextSendMessage(
                text = '請選擇喜歡歌曲',
                quick_reply = QuickReply(
                    items = [
                        QuickReplyButton(action=MessageAction(label="日文歌", text="https://www.youtube.com/watch?v=2A5JmSI2VsM&t=4612s")),
                        QuickReplyButton(action=MessageAction(label="洗腦歌", text="https://www.youtube.com/watch?v=8L2ds1XxrvA")),
                        QuickReplyButton(action=MessageAction(label="中文歌", text="https://www.youtube.com/watch?v=3HsIaWuNeX0&t=122s")),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "發生錯誤!!"))
            




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3333)