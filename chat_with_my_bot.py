from konlpy.tag import Kkma
import crawl


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
            #크롤링한 직업정보 반환받고
            _jobs = crawl._crawl_newbie_info(jabs[words['jobs'][i]])

            return _jobs

    if check:
        anw.append('뭐라는 거야 ~~ -3- 그건 몰라~\n')

    return u'\n'.join(anw)

