# import time
#
# from aiogram import F, Router
# from aiogram.filters import Command, CommandStart, StateFilter
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import default_state
# from aiogram.types import CallbackQuery, Message
# from fsm_settings import AskMode, DefectsCalculation, PenaltyCalculation
# from lexicon.lexicon import CITIES_RU, LEXICON_RU
# from loader import db
# from utils import create_inline_kb
#
# router = Router()
#
# SLEEP_TIME_ANSWER = 2
# SLEEP_TIME_WARNING = 4
#
#
# async def delete_warning(message: Message, text: str):
#     bot_message = await message.answer(text=text)
#     time.sleep(SLEEP_TIME_WARNING)
#     await message.delete()
#     await bot_message.delete()
#
#
# async def main_menu(message: Message, text: str):
#     keyboard = create_inline_kb(
#         1,
#         "penalty_button",
#         "defects_button",
#         "ask_button",
#     )
#     await message.answer(text=text, reply_markup=keyboard)
#
#
# @router.message(CommandStart(), StateFilter(default_state))
# async def process_start_command(message: Message):
#     user = await db.get_user(message.from_user.id)
#     if not user:
#         await db.add_user(
#             message.from_user.id,
#             message.from_user.username,
#             message.from_user.first_name,
#             message.from_user.last_name,
#         )
#     await main_menu(message, LEXICON_RU["/start"])
#
#
# @router.callback_query(
#     F.data.in_(
#         [
#             "penalty_button",
#             "defects_button",
#             "ask_button",
#         ]
#     )
# )
# async def process_start_callback(callback: CallbackQuery, state: FSMContext):
#     if callback.data == "penalty_button":
#         await callback.message.edit_text(
#             text=LEXICON_RU["penalty_start_date1"]
#         )
#         time.sleep(SLEEP_TIME_ANSWER)
#         await callback.message.answer(text=LEXICON_RU["penalty_start_date2"])
#         time.sleep(SLEEP_TIME_ANSWER)
#         await callback.message.answer(text=LEXICON_RU["penalty_start_date3"])
#         await state.set_state(PenaltyCalculation.start_date)
#     elif callback.data == "defects_button":
#         await callback.message.edit_text(text=LEXICON_RU["defects_text1"])
#         time.sleep(SLEEP_TIME_ANSWER)
#         await callback.message.answer(text=LEXICON_RU["defects_text2"])
#         time.sleep(SLEEP_TIME_ANSWER)
#         keyboard = create_inline_kb(
#             2,
#             *CITIES_RU,
#         )
#         await callback.message.answer(
#             text=LEXICON_RU["defects_text3"], reply_markup=keyboard
#         )
#         await state.set_state(DefectsCalculation.start)
#     elif callback.data == "ask_button":
#         await callback.message.edit_text(text=LEXICON_RU["ask_text"])
#         await state.set_state(AskMode.start)
