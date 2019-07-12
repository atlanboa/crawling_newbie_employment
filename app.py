# -*- coding: utf-8 -*-
import json
from flask import Flask, request
from slack import WebClient
import chat_with_my_bot
import make_block
from slack.web.classes.blocks import *
from slack.web.classes.elements import *
from slack.web.classes.interactions import MessageInteractiveEvent
from slackeventsapi import SlackEventAdapter

SLACK_TOKEN = 'xoxb-691797361766-689184678356-0H4RfMhRMctD17vM3qd4awhn'
SLACK_SIGNING_SECRET = '56c25316dd82cc632339a6dc295701d3'

app = Flask(__name__)
# /listening 으로 슬랙 이벤트를 받습니다.
slack_events_adaptor = SlackEventAdapter(SLACK_SIGNING_SECRET, "/listening", app)
slack_web_client = WebClient(token=SLACK_TOKEN)


job_objects = []


# 챗봇이 멘션을 받았을 경우 (이벤트 처리 부분)
@slack_events_adaptor.on("app_mention")
def app_mentioned(event_data):
    channel = event_data["event"]["channel"]
    text = event_data["event"]["text"]

    # chat_with_my_bot._chat_with_mybot()
    global job_objects
    if text == '<@UL9K54M32>':
        keywords = '안녕나는 챗봇이얌~~!! 취업정보를 알려주는 봇이얌 ^_^'
    else:
        # job_objects 는 blocks
        job_objects = chat_with_my_bot._chat_with_mybot(text)

        slack_web_client.chat_postMessage(
            channel=channel,
            blocks=extract_json(make_block.make_block(job_objects, 5))
        )
    # if type(keywords) == str:
    #     slack_web_client.chat_postMessage(
    #         channel=channel,
    #         text=keywords
    #     )
    # else:
    #     slack_web_client.chat_postMessage(
    #         channel=channel,
    #         blocks=make_block.make_block(keywords)
    #     )


# # 링크 만들기
# slack_web_client.chat_postMessage(
#     channel="#채널명",
#     text="<https://ssafy.elice.io|엘리스>는 정말 최고야!"
# )

# / 로 접속하면 서버가 준비되었다고 알려줍니다.
@app.route("/", methods=["GET"])
def index():
    return "<h1>Server is ready.</h1>"


current = 5


@app.route("/click", methods=["GET", "POST"])
def on_button_click():
    # 버튼 클릭은 SlackEventsApi에서 처리해주지 않으므로 직접 처리합니다

    payload = request.values["payload"]
    click_event = MessageInteractiveEvent(json.loads(payload))

    global current
    # keyword = click_event.block_id
    current = int(click_event.value)

    # 다른 리스트로 블록을 재가공
    message_blocks = make_block.make_block(job_objects, current)

    # 메시지를 채널에 올립니다
    slack_web_client.chat_postMessage(
        channel=click_event.channel.id,
        blocks=extract_json(message_blocks)
    )

    # Slack에게 클릭 이벤트를 확인했다고 알려줍니다
    return "OK", 200



if __name__ == '__main__':

    # _crawl_job_info('text')
    # jobs = _crawl_newbie_info('전체')
    # for job in jobs:
        # print(job.__getattribute__('company'))
    app.run('127.0.0.1', port=5000)


