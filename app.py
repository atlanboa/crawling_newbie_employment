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


<<<<<<< HEAD
class Job_Info:
    def __init__(self, company, title, sub_title, deadline, type, education, location, employment_type):
        self.company = company
        self.title = title
        self.sub_title = sub_title
        self.deadline = deadline
        self.type = type
        self.education = education
        self.location = location
        self.employment_type = employment_type

    def __getattr__(self, item):
        if item == 'company':
            return self.company
        elif item == 'title':
            return self.title
        elif item == 'sub_title':
            return self.sub_title
        elif item == 'deadline':
            return self.deadline
        elif item == 'type':
            return self.type
        elif item == 'education':
            return self.education
        elif item == 'location':
            return self.location
        else:
            return self.employment_type


def _crawl_job_korea(text):
    if True:
        return

def _crawl_top10(task):
    url = _getUrl_(task)
    source_code = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source_code, "html.parser")

    job_infos = []
    job_info = Job_Info
    for


#url 반환 함수
def _getUrl_(task):
    urls = {'직무 전체': 'http://www.jobkorea.co.kr/top100/',
            '경영': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10012&BizJobtype_Bctgr_Name=%EA%B2%BD%EC%98%81%C2%B7%EC%82%AC%EB%AC%B4&BizJobtype_Code=0&BizJobtype_Name=%EA%B2%BD%EC%98%81%C2%B7%EC%82%AC%EB%AC%B4+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0',
            '사무': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10012&BizJobtype_Bctgr_Name=%EA%B2%BD%EC%98%81%C2%B7%EC%82%AC%EB%AC%B4&BizJobtype_Code=0&BizJobtype_Name=%EA%B2%BD%EC%98%81%C2%B7%EC%82%AC%EB%AC%B4+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '마케팅': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10013&BizJobtype_Bctgr_Name=%EB%A7%88%EC%BC%80%ED%8C%85%C2%B7%EA%B4%91%EA%B3%A0%C2%B7%ED%99%8D%EB%B3%B4&BizJobtype_Code=0&BizJobtype_Name=%EB%A7%88%EC%BC%80%ED%8C%85%C2%B7%EA%B4%91%EA%B3%A0%C2%B7%ED%99%8D%EB%B3%B4+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '홍보': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10013&BizJobtype_Bctgr_Name=%EB%A7%88%EC%BC%80%ED%8C%85%C2%B7%EA%B4%91%EA%B3%A0%C2%B7%ED%99%8D%EB%B3%B4&BizJobtype_Code=0&BizJobtype_Name=%EB%A7%88%EC%BC%80%ED%8C%85%C2%B7%EA%B4%91%EA%B3%A0%C2%B7%ED%99%8D%EB%B3%B4+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '광고': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10013&BizJobtype_Bctgr_Name=%EB%A7%88%EC%BC%80%ED%8C%85%C2%B7%EA%B4%91%EA%B3%A0%C2%B7%ED%99%8D%EB%B3%B4&BizJobtype_Code=0&BizJobtype_Name=%EB%A7%88%EC%BC%80%ED%8C%85%C2%B7%EA%B4%91%EA%B3%A0%C2%B7%ED%99%8D%EB%B3%B4+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            'IT': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10016&BizJobtype_Bctgr_Name=IT%C2%B7%EC%9D%B8%ED%84%B0%EB%84%B7&BizJobtype_Code=0&BizJobtype_Name=IT%C2%B7%EC%9D%B8%ED%84%B0%EB%84%B7+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '인터넷': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10016&BizJobtype_Bctgr_Name=IT%C2%B7%EC%9D%B8%ED%84%B0%EB%84%B7&BizJobtype_Code=0&BizJobtype_Name=IT%C2%B7%EC%9D%B8%ED%84%B0%EB%84%B7+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '디자인': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10019&BizJobtype_Bctgr_Name=%EB%94%94%EC%9E%90%EC%9D%B8&BizJobtype_Code=0&BizJobtype_Name=%EB%94%94%EC%9E%90%EC%9D%B8+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '무역': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10014&BizJobtype_Bctgr_Name=%EB%AC%B4%EC%97%AD%C2%B7%EC%9C%A0%ED%86%B5&BizJobtype_Code=0&BizJobtype_Name=%EB%AC%B4%EC%97%AD%C2%B7%EC%9C%A0%ED%86%B5+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '유통': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10014&BizJobtype_Bctgr_Name=%EB%AC%B4%EC%97%AD%C2%B7%EC%9C%A0%ED%86%B5&BizJobtype_Code=0&BizJobtype_Name=%EB%AC%B4%EC%97%AD%C2%B7%EC%9C%A0%ED%86%B5+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '영업': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10015&BizJobtype_Bctgr_Name=%EC%98%81%EC%97%85%C2%B7%EA%B3%A0%EA%B0%9D%EC%83%81%EB%8B%B4&BizJobtype_Code=0&BizJobtype_Name=%EC%98%81%EC%97%85%C2%B7%EA%B3%A0%EA%B0%9D%EC%83%81%EB%8B%B4+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '고객상담': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10015&BizJobtype_Bctgr_Name=%EC%98%81%EC%97%85%C2%B7%EA%B3%A0%EA%B0%9D%EC%83%81%EB%8B%B4&BizJobtype_Code=0&BizJobtype_Name=%EC%98%81%EC%97%85%C2%B7%EA%B3%A0%EA%B0%9D%EC%83%81%EB%8B%B4+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '연구개발': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10018&BizJobtype_Bctgr_Name=%EC%97%B0%EA%B5%AC%EA%B0%9C%EB%B0%9C%C2%B7%EC%84%A4%EA%B3%84&BizJobtype_Code=0&BizJobtype_Name=%EC%97%B0%EA%B5%AC%EA%B0%9C%EB%B0%9C%C2%B7%EC%84%A4%EA%B3%84+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '설계': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10018&BizJobtype_Bctgr_Name=%EC%97%B0%EA%B5%AC%EA%B0%9C%EB%B0%9C%C2%B7%EC%84%A4%EA%B3%84&BizJobtype_Code=0&BizJobtype_Name=%EC%97%B0%EA%B5%AC%EA%B0%9C%EB%B0%9C%C2%B7%EC%84%A4%EA%B3%84+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '서비스': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10022&BizJobtype_Bctgr_Name=%EC%84%9C%EB%B9%84%EC%8A%A4&BizJobtype_Code=0&BizJobtype_Name=%EC%84%9C%EB%B9%84%EC%8A%A4+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '생산': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10017&BizJobtype_Bctgr_Name=%EC%83%9D%EC%82%B0%C2%B7%EC%A0%9C%EC%A1%B0&BizJobtype_Code=0&BizJobtype_Name=%EC%83%9D%EC%82%B0%C2%B7%EC%A0%9C%EC%A1%B0+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '제조': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10017&BizJobtype_Bctgr_Name=%EC%83%9D%EC%82%B0%C2%B7%EC%A0%9C%EC%A1%B0&BizJobtype_Code=0&BizJobtype_Name=%EC%83%9D%EC%82%B0%C2%B7%EC%A0%9C%EC%A1%B0+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '교육': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10023&BizJobtype_Bctgr_Name=%EA%B5%90%EC%9C%A1&BizJobtype_Code=0&BizJobtype_Name=%EA%B5%90%EC%9C%A1+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '건설': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10021&BizJobtype_Bctgr_Name=%EA%B1%B4%EC%84%A4&BizJobtype_Code=0&BizJobtype_Name=%EA%B1%B4%EC%84%A4+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '의료': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10024&BizJobtype_Bctgr_Name=%EC%9D%98%EB%A3%8C&BizJobtype_Code=0&BizJobtype_Name=%EC%9D%98%EB%A3%8C+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '미디어': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10020&BizJobtype_Bctgr_Name=%EB%AF%B8%EB%94%94%EC%96%B4&BizJobtype_Code=0&BizJobtype_Name=%EB%AF%B8%EB%94%94%EC%96%B4+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '전문': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10025&BizJobtype_Bctgr_Name=%EC%A0%84%EB%AC%B8%C2%B7%ED%8A%B9%EC%88%98%EC%A7%81&BizJobtype_Code=0&BizJobtype_Name=%EC%A0%84%EB%AC%B8%C2%B7%ED%8A%B9%EC%88%98%EC%A7%81+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on',
            '특수직': 'http://www.jobkorea.co.kr/Top100/?Main_Career_Type=1&Search_Type=1&BizJobtype_Bctgr_Code=10025&BizJobtype_Bctgr_Name=%EC%A0%84%EB%AC%B8%C2%B7%ED%8A%B9%EC%88%98%EC%A7%81&BizJobtype_Code=0&BizJobtype_Name=%EC%A0%84%EB%AC%B8%C2%B7%ED%8A%B9%EC%88%98%EC%A7%81+%EC%A0%84%EC%B2%B4&Major_Big_Code=0&Major_Big_Name=%EC%A0%84%EC%B2%B4&Major_Code=0&Major_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Code=9&Edu_Level_Name=%EC%A0%84%EC%B2%B4&Edu_Level_Name=%EC%A0%84%EC%B2%B4&MidScroll=0&duty-depth2=on'

            }
    return urls[task]

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
=======
# 챗봇이 멘션을 받았을 경우 (이벤트 처리 부분)
>>>>>>> beed056623473538ae4728fe0aa1d040344bf089
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


