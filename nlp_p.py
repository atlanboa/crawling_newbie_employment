#-*- coding: utf-8 -*-
import re
import urllib.request
from bs4 import BeautifulSoup
from flask import Flask
from slacker import Slacker
from slackclient import SlackClient
from slackeventsapi import SlackEventAdapter
from konlpy.tag import Kkma

SLACK_TOKEN = 'xoxb-672063103650-689651157104-ob4epdKigyRyQ0m0Hyyloo9r'
SLACK_SIGNING_SECRET = '4779b587edbf20decac9c981e5c3401e'

app = Flask(__name__)
# /listening 으로 슬랙 이벤트를 받습니다.
slack_events_adaptor = SlackEventAdapter(SLACK_SIGNING_SECRET, "/listening", app)
slack_web_client = SlackClient(token=SLACK_TOKEN)

# 직업 정보를 정의한 클래스
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
      print('링크 ({})'.format(self.co_link + self.link))
      print('-------------------------------------------------------------------------')

   def get_string(self):
      string = '-------------------------------------------------------------------------\n' + \
               '회사명 ({})\n'.format(self.company) + \
               '메인 타이틀 ({})\n'.format(self.title) + \
               '서브 타이틀 ({})\n'.format(self.sub_title) + \
               '경력 구분 ({})\n'.format(self.career) + \
               '학력 ({})\n'.format(self.education) + \
               '지역 ({})\n'.format(self.location) + \
               '고용 형태 ({})\n'.format(self.employment_type) + \
               '마감 ({})\n'.format(self.deadline) + \
               '링크 ({})\n'.format(self.co_link + self.link) + \
               '-------------------------------------------------------------------------\n'
      return string

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
    urls = {'경영':'http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10012&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=',
            '마케팅': 'http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10013&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=',
            'IT': 'http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10016&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=',
            '디자인': 'http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10019&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=',
            '무역': 'http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10014&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=',
            '디자인': 'http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10015&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=',
            '무역': 'http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10022&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=',
            '영업': 'http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10015&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=',
            '서비스': 'http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10022&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=',
            '연구개발': 'http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10018&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=',
            '생산': 'http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10017&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=',
            '교육': 'http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10023&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=',
            '건설': 'http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10021&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=',
            '의료': 'http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10024&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=',
            '미디어': 'http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10020&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=',
            '전문특수직': 'http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10025&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=',
            '전체': 'http://www.jobkorea.co.kr/starter/'
            }

    return urls[task]

# 크롤 함수
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

def _crawl_newbie_info(task):
   # url = 'http://www.jobkorea.co.kr/Starter/?JoinPossible_Stat=0&schPart=%2C%2C10013%2C%2C&schOrderBy=0&LinkGubun=0&LinkNo=0&schType=0&schGid=0&Page=1'
   # print(urls)
   # # get_newbie_url(task)로 업무에 따른 url 반환
   # # collect_url(url)로 pagination된 전체 페이지 url 획득
   # urls = collect_url(get_newbie_url(task))

   urls = collect_url(get_newbie_url(task))
   jobs = []

   for url in urls:
      source_code = urllib.request.urlopen(url).read()
      soup = BeautifulSoup(source_code, "html.parser")

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
         # job.show_info()
         jobs.append(job)
   return jobs

# url 파싱
def collect_url(url):
    # url = 'http://www.jobkorea.co.kr/starter'
    source_code = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source_code, "html.parser")
    page_button = soup.find('div', class_='tplPagination')
    urls = [url]
    for href in page_button.find_all('a'):
            urls.append('http://www.jobkorea.co.kr'+href.get('href'))
    return urls

def _chat_with_mybot(text):
   # 키워드 매칭을 위한 딕셔너리
   words = {'jobs': ['아이티', '인터넷', '게임', '큐에이', '테스터', '검증', '디비에이', '데이터베이스', '네트워크', '서버', '보안', '웹기획', '피엠', '웹마케팅', '웹프로그래머', '응용프로그래머', '시스템프로그래머', '컨텐츠', '사이트운영', '에이치티엠엘', '퍼블리싱', '유아이', '웹디자인', '이알피', '시스템분석', '시스템설계', '컴퓨터강사', '동영상제작', '동영상편집', '빅데이터', '인공지능', '소프트웨어', '하드웨어', '컴퓨터'],
            'names': ['이름', '성함'],
            'greetings': ['안녕','반가워'],
            'help': ['핼프']}
   jabs = {'아이티': 'IT', '인터넷': 'IT', '게임': 'IT', '큐에이': 'IT', '테스터': 'IT', '검증': 'IT', '디비에이': 'IT', '데이터베이스': 'IT', '네트워크': 'IT', '서버': 'IT',
    '보안': 'IT', '웹기획': 'IT', '피엠': 'IT', '웹마케팅': 'IT', '웹프로그래머': 'IT', '응용프로그래머': 'IT', '시스템프로그래머': 'IT', '컨텐츠': 'IT', '사이트운영': 'IT',
    '에이치티엠엘': 'IT', '퍼블리싱': 'IT', '유아이': 'IT', '웹디자인': 'IT', '이알피': 'IT', '시스템분석': 'IT', '시스템설계': 'IT', '컴퓨터강사': 'IT', '동영상제작': 'IT',
    '동영상편집': 'IT', '빅데이터': 'IT', '인공지능': 'IT', '소프트웨어': 'IT', '하드웨어': 'IT', '컴퓨터':'IT'}
   anw = []
   check = True
   kkma = Kkma()
   keywords = kkma.nouns(text)

   print(keywords)

   for i in range(len(words['greetings'])):
      if words['greetings'][i] in keywords:
         anw.append('안녕~ 반가워^_^\n')
         check = False

   for i in range(len(words['names'])):
      if words['names'][i] in keywords:
         anw.append('내 이름은 봇이얌 봇봇봇~!!\n')
         check = False

   for i in range(len(words['jobs'])):
      if words['jobs'][i] in keywords:
         anw.append(words['jobs'][i] + '에 관련된 직종을 추천해줄께 기다려봐~~^^\n')
         if
         _jobs = _crawl_newbie_info(jabs[words['jobs'][i]])
         index = 0
         for _job in _jobs:
            if index >= max:
               break
            else:
               index += 1
               anw.append(_job.get_string())
         anw.append(jabs[words['jobs'][i]] + '\n')
         check = False
   if check:
      anw.append('뭐라는 거야 ~~ -3- 그건 몰라~\n')
   return u'\n'.join(anw)

# 챗봇이 멘션을 받았을 경우 (이벤트 처리 부분)
@slack_events_adaptor.on("app_mention")
def app_mentioned(event_data):
   channel = event_data["event"]["channel"]
   text = event_data["event"]["text"]

   if text == '<@UL9K54M32>':
      keywords = '안녕나는 챗봇이얌~~!! 취업정보를 알려주는 봇이얌 ^_^'
   else:
      keywords = _chat_with_mybot(text)
   slack = Slacker(token=SLACK_TOKEN)
   slack.chat.post_message(
       channel=channel,
       text=keywords
   )

# / 로 접속하면 서버가 준비되었다고 알려줍니다.
@app.route("/", methods=["GET"])
def index():
   return "<h1>Server is ready.</h1>"

if __name__ == '__main__':
   app.run('127.0.0.1', port=5001)