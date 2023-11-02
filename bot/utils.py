# from datetime import datetime
#
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from lexicon.lexicon import LEXICON_RU
#
#
# # Функция для формирования инлайн-клавиатуры на лету
# def create_inline_kb(
#     width: int, *args: str, **kwargs: str
# ) -> InlineKeyboardMarkup:
#     kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
#     buttons: list[InlineKeyboardButton] = []
#     if args:
#         for button in args:
#             buttons.append(
#                 InlineKeyboardButton(
#                     text=LEXICON_RU[button]
#                     if button in LEXICON_RU
#                     else button,
#                     callback_data=button,
#                 )
#             )
#     if kwargs:
#         for button, text in kwargs.items():
#             buttons.append(
#                 InlineKeyboardButton(text=text, callback_data=button)
#             )
#
#     kb_builder.row(*buttons, width=width)
#     return kb_builder.as_markup()
#
#
# def convert_to_float(amount_str: str) -> float:
#     clean_str = "".join(
#         filter(lambda x: x.isdigit() or x in [",", "."], amount_str)
#     )
#     if "." in clean_str and "," in clean_str:
#         if clean_str.find(".") < clean_str.find(","):
#             clean_str = clean_str.replace(".", "").replace(",", ".")
#         else:
#             clean_str = clean_str.replace(",", "")
#     else:
#         clean_str = clean_str.replace(",", ".")
#
#     return float(clean_str)
