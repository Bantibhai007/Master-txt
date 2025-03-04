import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '8005429189:AAHquY4qiB2nNJIVmUUbhkuUWGdHE9Qev4g')
    API_ID = int(os.environ.get("API_ID", '20114039'))
    API_HASH = os.environ.get("API_HASH", '87297b8f3cc8fc9bbce591ad30da5896')
    AUTH_USER = os.environ.get('AUTH_USERS','8172163893').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "ᗷᕼᑌᗰIᕼᗩᖇ"#Here You Can Change with Your Name  or any custom name or title you prefer
