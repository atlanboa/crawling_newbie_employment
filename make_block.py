from slack.web.classes import extract_json
from slack.web.classes.blocks import *


def make_block(_jobs):
    head_block = [{
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*There are many companies for you, Check it out, Take your wings*"
        }
    }]
    blocks = []

    index = 1
    for _job in _jobs:
        if index < 5:
            index += 1
            company = _job.__getattribute__('company')
            title = _job.__getattribute__('title')
            sub_title = _job.__getattribute__('sub_title')
            career = _job.__getattribute__('career')
            education = _job.__getattribute__('education')
            location = _job.__getattribute__('location')
            employment_type = _job.__getattribute__('employment_type')
            deadline = _job.__getattribute__('deadline')
            link = _job.__getattribute__('link')

            block = SectionBlock(
                text="*<" + link + " | " + company + ">*\n" + sub_title + '\n경력 : ' + career +
                     " | 학력 : " + education + " | 지역 : " + location + " | 고용 형태 : " + employment_type +
                     " | 마감일 : " + deadline
            )
            blocks.append(block)
        else:
            break
    # divider = DividerBlock(
    #     subtype="divider"
    # )

    # 섹션 블록: 짧은 문구 여러 개를 2줄로 표시합니다 (최대 10개).
    block2 = SectionBlock(
        fields=["text1", "text2", "text1", "text2"]
    )

    # 이미지 블록: 큰 이미지 하나를 표시합니다..
    block3 = ImageBlock(
        image_url="이미지의 URL",
        alt_text="이미지가 안 보일 때 대신 표시할 텍스트"
    )







    # # 여러 개의 블록을 하나의 메시지로 묶어 보냅니다.
    # my_blocks = [block1, block2, block3]
    # slack_web_client.chat_postMessage(
    #     channel="#채널명",
    #     blocks=extract_json(my_blocks)
    # )
    #
    return extract_json(blocks)



