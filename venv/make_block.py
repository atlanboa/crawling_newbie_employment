from slack.web.classes import extract_json
from slack.web.classes.blocks import *


def make_block(_job):

    company = _job.__getattribute__('company')
    title = _job.__getattribute__('title')
    sub_title =_job.__getattribute__('sub_title')
    career = _job.__getattribute__('career')
    education = _job.__getattribute__('education')
    location = _job.__getattribute__('location')
    employment_type = _job.__getattribute__('employment_type')
    deadline = _job.__getattribute__('deadline')
    link = _job.__getattribute__('link')

    head_block =  {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*There are many companies for you, Check it out, Take your wings*"
            },
        },
    block = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*There are many companies for you, Check it out, Take your wings*"
            },
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*<fakeLink.toHotelPage.com|Windsor Court Hotel>*\n★★★★★\n$340 per night\nRated: 9.4 - Excellent"
            },
            "accessory": {
                "type": "image",
                "image_url": "https://api.slack.com/img/blocks/bkb_template_images/tripAgent_1.png",
                "alt_text": "Windsor Court Hotel thumbnail"
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "image",
                    "image_url": "https://api.slack.com/img/blocks/bkb_template_images/tripAgentLocationMarker.png",
                    "alt_text": "Location Pin Icon"
                },
                {
                    "type": "plain_text",
                    "emoji": true,
                    "text": "Location: Central Business District"
                }
            ]
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*<fakeLink.toHotelPage.com|The Ritz-Carlton New Orleans>*\n★★★★★\n$340 per night\nRated: 9.1 - Excellent"
            },
            "accessory": {
                "type": "image",
                "image_url": "https://api.slack.com/img/blocks/bkb_template_images/tripAgent_2.png",
                "alt_text": "Ritz-Carlton New Orleans thumbnail"
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "image",
                    "image_url": "https://api.slack.com/img/blocks/bkb_template_images/tripAgentLocationMarker.png",
                    "alt_text": "Location Pin Icon"
                },
                {
                    "type": "plain_text",
                    "emoji": true,
                    "text": "Location: French Quarter"
                }
            ]
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*<fakeLink.toHotelPage.com|Omni Royal Orleans Hotel>*\n★★★★★\n$419 per night\nRated: 8.8 - Excellent"
            },
            "accessory": {
                "type": "image",
                "image_url": "https://api.slack.com/img/blocks/bkb_template_images/tripAgent_3.png",
                "alt_text": "Omni Royal Orleans Hotel thumbnail"
            }
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "image",
                    "image_url": "https://api.slack.com/img/blocks/bkb_template_images/tripAgentLocationMarker.png",
                    "alt_text": "Location Pin Icon"
                },
                {
                    "type": "plain_text",
                    "emoji": true,
                    "text": "Location: French Quarter"
                }
            ]
        },
        {
            "type": "divider"
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "emoji": true,
                        "text": "Next 2 Results"
                    },
                    "value": "click_me_123"
                }
            ]
        }
    ]
    block1 = SectionBlock(
        text="텍스트"
    )

    # 섹션 블록: 짧은 문구 여러 개를 2줄로 표시합니다 (최대 10개).
    block2 = SectionBlock(
        fields=["text1", "text2", ...]
    )

    # 이미지 블록: 큰 이미지 하나를 표시합니다..
    block3 = ImageBlock(
        image_url="이미지의 URL",
        alt_text="이미지가 안 보일 때 대신 표시할 텍스트"
    )

    # 여러 개의 블록을 하나의 메시지로 묶어 보냅니다.
    my_blocks = [block1, block2, block3]
    slack_web_client.chat_postMessage(
        channel="#채널명",
        blocks=extract_json(my_blocks)
    )