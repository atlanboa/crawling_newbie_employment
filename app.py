# -*- coding: utf-8 -*-

from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import chat_with_my_bot
import make_block

SLACK_TOKEN = 'xoxb-691797361766-689184678356-0H4RfMhRMctD17vM3qd4awhn'
SLACK_SIGNING_SECRET = '56c25316dd82cc632339a6dc295701d3'

app = Flask(__name__)
# /listening 으로 슬랙 이벤트를 받습니다.
slack_events_adaptor = SlackEventAdapter(SLACK_SIGNING_SECRET, "/listening", app)
slack_web_client = WebClient(token=SLACK_TOKEN)


# 챗봇이 멘션을 받았을 경우 (이벤트 처리 부분)
@slack_events_adaptor.on("app_mention")
def app_mentioned(event_data):
    channel = event_data["event"]["channel"]
    text = event_data["event"]["text"]

    # chat_with_my_bot._chat_with_mybot()

    if text == '<@UL9K54M32>':
        keywords = '안녕나는 챗봇이얌~~!! 취업정보를 알려주는 봇이얌 ^_^'
    else:
        keywords = chat_with_my_bot._chat_with_mybot(text)

    if type(keywords) == str:
        slack_web_client.chat_postMessage(
            channel=channel,
            text=keywords
        )
    else:
        slack_web_client.chat_postMessage(
            channel=channel,
            blocks=make_block.make_block(keywords)
        )


# # 링크 만들기
# slack_web_client.chat_postMessage(
#     channel="#채널명",
#     text="<https://ssafy.elice.io|엘리스>는 정말 최고야!"
# )

# / 로 접속하면 서버가 준비되었다고 알려줍니다.
@app.route("/", methods=["GET"])
def index():
    return "<h1>Server is ready.</h1>"


if __name__ == '__main__':

    # _crawl_job_info('text')
    # jobs = _crawl_newbie_info('전체')
    # for job in jobs:
        # print(job.__getattribute__('company'))
    app.run('127.0.0.1', port=5000)


