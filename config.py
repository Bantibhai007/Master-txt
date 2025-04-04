import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '')
    API_ID = int(os.environ.get("API_ID", '24630940'))
    API_HASH = os.environ.get("API_HASH", 'df46be1ad6b0027ec1dff6dd3bb703dd')
    AUTH_USER = os.environ.get('AUTH_USERS','5923201419').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://api.masterapi.tech"
    CREDIT = "ROCKY"#Here You Can Change with Your Name  or any custom name or title you prefer
