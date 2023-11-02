# from datetime import datetime
# from typing import Union
#
# from aiogram.filters import BaseFilter
# from aiogram.types import Message
#
#
# class IsValidCostFilter(BaseFilter):
#     async def __call__(self, message: Message) -> bool:
#         return all(c.isdigit() or c in [" ", ".", ","] for c in message.text)
#
#
# class IsValidDateFilter(BaseFilter):
#     async def __call__(self, message: Message) -> bool:
#         try:
#             date = datetime.strptime(message.text, "%d.%m.%Y")
#             if datetime.now() >= date >= datetime(2006, 10, 23):
#                 return True
#             return False
#         except ValueError:
#             return False
