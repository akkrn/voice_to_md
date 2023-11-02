# from dataclasses import dataclass
#
# from environs import Env
#
#
# @dataclass
# class OpenAIConfig:
#     api_key: str
#     url: str
#
#
# @dataclass
# class DatabaseConfig:
#     postgres_db: str
#     db_host: str
#     postgres_user: str
#     postgres_password: str
#     db_port: int
#
#
# @dataclass
# class TgBot:
#     token: str
#
#
# @dataclass
# class Config:
#     tg_bot: TgBot
#     db: DatabaseConfig
#     openai: OpenAIConfig
#
#
# def load_config(path: str | None) -> Config:
#     env: Env = Env()
#     env.read_env(path)
#
#     return Config(
#         tg_bot=TgBot(token=env("BOT_TOKEN")),
#         db=DatabaseConfig(
#             postgres_db=env("POSTGRES_DB"),
#             db_host=env("DB_HOST"),
#             postgres_user=env("POSTGRES_USER"),
#             postgres_password=env("POSTGRES_PASSWORD"),
#             db_port=env.int("DB_PORT"),
#         ),
#         openai=OpenAIConfig(
#             api_key=env("OPENAI_API_KEY"), url=env("OPENAI_API_URL")
#         ),
#     )
