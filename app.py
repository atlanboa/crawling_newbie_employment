# -*- coding: utf-8 -*-
import re
import urllib.request

from bs4 import BeautifulSoup

from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

SLACK_TOKEN = 'xoxb-691797361766-689184678356-0H4RfMhRMctD17vM3qd4awhn'
SLACK_SIGNING_SECRET = '56c25316dd82cc632339a6dc295701d3'

app = Flask(__name__)
# /listening 으로 슬랙 이벤트를 받습니다.
slack_events_adaptor = SlackEventAdapter(SLACK_SIGNING_SECRET, "/listening", app)
slack_web_client = WebClient(token=SLACK_TOKEN)


def job_korea():
    # URL 데이터를 가져올 사이트 url 입력
    url = "http://www.jobkorea.co.kr/top100/"

    # URL 주소에 있는 HTML 코드를 soup에 저장합니다.
    source_code = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source_code, "html.parser")

    list = []

    for naver_text in soup.find_all("a", class_="coLink"):
        list.append(naver_text.get_text())

    print(list)


# 크롤링 함수 구현하기
def _crawl_portal_keywords(text):
    url_match = re.search(r'<(http.*?)(\|.*?)?>', text)
    if not url_match:
        return '올바른 URL을 입력해주세요.'

    url = url_match.group(1)
    source_code = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source_code, "html.parser")

    # 여기에 함수를 구현해봅시다.
    keywords = []
    if 'naver' in url:

        for i, keyword in enumerate(soup.find_all("span", class_="ah_k")):
            if i < 20:
                keywords.append(keyword.get_text())  # 한글 지원을 위해 앞에 unicode u를 붙혀준다.


    else:

        for i, keyword in enumerate(soup.find_all("a", class_="link_issue")):
            if i < 20:
                keyword = keyword.get_text()
                if keyword not in keywords:
                    keywords.append(keyword)

                    # 키워드 리스트를 문자열로 만듭니다.
    return '\n'.join(keywords)


# 챗봇이 멘션을 받았을 경우
@slack_events_adaptor.on("app_mention")
def app_mentioned(event_data):
    channel = event_data["event"]["channel"]
    text = event_data["event"]["text"]

    keywords = _crawl_portal_keywords(text)
    slack_web_client.chat_postMessage(
        channel=channel,
        text=keywords
    )


# / 로 접속하면 서버가 준비되었다고 알려줍니다.
@app.route("/", methods=["GET"])
def index():
    return "<h1>Server is ready.</h1>"



if __name__ == '__main__':
    job_korea()
    app.run('127.0.0.1', port=5000)
