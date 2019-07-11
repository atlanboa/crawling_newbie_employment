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


# job info class
class JobInfo:
    def __init__(self, company, title, sub_title, career, education, location, employment_type, deadline, link):
        self.company = company
        self.title = title
        self.sub_title = sub_title
        self.career = career
        self.education = education
        self.location = location
        self.employment_type = employment_type
        self.deadline = deadline
        self.link = link
        self.co_link = 'http://www.jobkorea.co.kr/top100'

    def show_info(self):
        print('-------------------------------------------------------------------------')
        print('회사명 ({})'.format(self.company))
        print('메인 타이틀 ({})'.format(self.title))
        print('서브 타이틀 ({})'.format(self.sub_title))
        print('경력 구분 ({})'.format(self.career))
        print('학력 ({})'.format(self.education))
        print('지역 ({})'.format(self.location))
        print('고용 형태 ({})'.format(self.employment_type))
        print('마감 ({})'.format(self.deadline))
        print('링크 ({})'.format(self.co_link+self.link))
        print('-------------------------------------------------------------------------')

    # setter
    def __setitem__(self, key, value):
        """Setting tag[key] sets the value of the 'key' attribute for the
        tag."""
        self.attrs[key] = value

    # getter
    def __getitem__(self, key):
        """tag[key] returns the value of the 'key' attribute for the tag,
        and throws an exception if it's not there."""
        return self.attrs[key]


# top 10 페이지 url
def get_top10_url(task):
    urls = {}
    return urls[task]


# top 10 페이지 크롤링
def get_newbie_url(task):
    urls = {}
    return urls[task]


def _crawl_newbie_info(task):
    # url = get_newbie_url(task)
    url = 'http://www.jobkorea.co.kr/Starter/?JoinPossible_Stat=0&schPart=%2C%2C10013%2C%2C&schOrderBy=0&LinkGubun=0&LinkNo=0&schType=0&schGid=0&Page=1'

    source_code = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source_code, "html.parser")

    jobs = []
    filter_list = soup.find('ul', class_='filterList')
    for li in filter_list.find_all('li'):
        company = li.find('a', class_='coLink').getText()
        title = li.find('a', class_='link').getText()
        sub_title = li.find('div', class_='sTit').getText()
        sdsc = li.find('div', class_='sDesc')
        employment_type = sdsc.find('strong').getText()
        career = ''
        try:
            education = sdsc.find_all('span')[0].getText()
            location = sdsc.find_all('span')[1].getText()

        except IndexError:
            pass
        deadline = li.find('span', class_='day').getText()
        link = li.find('a', class_='coLink').get('href')
        job = JobInfo(company,
                      title,
                      sub_title,
                      career,
                      education,
                      location,
                      employment_type,
                      deadline,
                      link
        )
        job.show_info()
        jobs.append(job)
        return jobs


# top 10 페이지 크롤링
def _crawl_job_info(task):
    url = get_top10_url(task)
    source_code = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source_code, "html.parser")

    jobs = []
    rank_list = soup.find('ol', class_='rankList')
    for li in rank_list.find_all('li'):
        company = li.find('a', class_='coLink').getText()
        title = li.find('a', class_='link').getText()
        sub_title = li.find('div', class_='sTit').getText()
        sdsc = li.find('div', class_='sDsc')
        try:
            career = sdsc.find_all('span')[0].getText()
            education = sdsc.find_all('span')[1].getText()
            location = sdsc.find_all('span')[2].getText()
            employment_type = sdsc.find_all('span')[3].getText()
        except IndexError:
            pass
        deadline = li.find('span', class_='day').getText()
        link = li.find('a', class_='coLink').get('href')
        job = JobInfo(company,
                      title,
                      sub_title,
                      career,
                      education,
                      location,
                      employment_type,
                      deadline,
                      link
        )
        jobs.append(job)
        # job.show_info()
    return jobs




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
    # _crawl_job_info('text')
    _crawl_newbie_info('task')
    # app.run('127.0.0.1', port=5000)
