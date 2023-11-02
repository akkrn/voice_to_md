# from aiogram.filters.state import State, StatesGroup
# from aiogram.fsm.storage.memory import MemoryStorage
# #from aiogram.fsm.storage.redis import RedisStorage
# # from database import create_redis_pool
# # import asyncio
#
# # loop = asyncio.get_event_loop()
# # redis = loop.run_until_complete(create_redis_pool())
# # storage = RedisStorage(redis=redis)
# storage = MemoryStorage()
#
# class PenaltyCalculation(StatesGroup):
#     start_date = State()
#     end_date_choice = State()
#     end_date = State()
#     object_cost = State()
#     confirm_details = State()
#     change_details = State()
#
#
# class DefectsCalculation(StatesGroup):
#     start = State()
#     input_city = State()
#     object_name = State()
#     object_square = State()
#     confirm_details = State()
#     change_details = State()
#
#
# class AskMode(StatesGroup):
#     start = State()
