# import asyncio
# import logging
#
# from aiogram import Dispatcher
#
# from handlers import (
#     defects_handlers,
#     other_handlers,
#     penalty_handlers,
#     ask_handlers,
# )
# from loader import bot, db, dp
#
# logger = logging.getLogger(__name__)
#
#
# async def shutdown(dispatcher: Dispatcher):
#     await dispatcher.storage.close()
#     logger.info("Storage closed")
#     await dispatcher.storage.wait_closed()
#
#
# async def main():
#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(filename)s:%(lineno)d #%(levelname)-8s "
#         "[%(asctime)s] - %(name)s - %(message)s",
#     )
#
#     logger.info("Starting bot")
#     await db.create_pool()
#     await db.create_tables()
#     logger.info("Database is created")
#
#     dp.include_router(other_handlers.router)
#     dp.include_router(penalty_handlers.router)
#     dp.include_router(defects_handlers.router)
#     dp.include_router(ask_handlers.router)
#
#     await bot.delete_webhook(drop_pending_updates=True)
#     await dp.start_polling(bot, on_shutdown=shutdown)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
