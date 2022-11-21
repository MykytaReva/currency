from pydantic import BaseSettings
#import typing

class Settings(BaseSettings):
    telegram_token: str #    TELEGRAM_TOKEN = '5839227850:AAHVWD13bl99gQz4Gac7M7Ifv-W1n05Twno'
    # api_version: typing.Optional(int)
    rates_url: str

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = '.env'
        env_file_encoding = 'utf-8'
settings = Settings()

