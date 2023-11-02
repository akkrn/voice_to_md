# # import aioredis
# from dataclasses import dataclass, field
# from datetime import datetime
#
# import asyncpg
# from asyncpg import Pool
# from config_data.config import load_config
#
#
# @dataclass
# class Database:
#     name: str
#     user: str
#     password: str
#     host: str
#     port: int
#     pool: Pool = field(init=False, default=None)
#
#     async def create_pool(self):
#         self.pool = await asyncpg.create_pool(
#             database=self.name,
#             user=self.user,
#             password=self.password,
#             host=self.host,
#             port=self.port,
#         )
#
#     async def create_tables(self):
#         async with self.pool.acquire() as connection:
#             await connection.execute(
#                 """
#                 CREATE TABLE IF NOT EXISTS keyratecbr (
#                     id SERIAL PRIMARY KEY,
#                     date DATE NOT NULL,
#                     rate REAL NOT NULL
#                 );
#                 CREATE TABLE IF NOT EXISTS users (
#                     id SERIAL PRIMARY KEY,
#                     user_id INTEGER NOT NULL UNIQUE,
#                     username VARCHAR(255),
#                     first_name VARCHAR(255),
#                     last_name VARCHAR(255),
#                     created_at TIMESTAMP NOT NULL
#                 );
#                 CREATE TABLE IF NOT EXISTS penalties (
#                     id SERIAL PRIMARY KEY,
#                     user_id INTEGER NOT NULL,
#                     start_date DATE NOT NULL,
#                     end_date DATE NOT NULL,
#                     object_cost NUMERIC (12, 3) NOT NULL,
#                     penalty NUMERIC (12, 3) NOT NULL
#                 );
#                 CREATE TABLE IF NOT EXISTS defects (
#                     id SERIAL PRIMARY KEY,
#                     user_id INTEGER NOT NULL,
#                     city VARCHAR(25) NOT NULL,
#                     object_name VARCHAR(50) NOT NULL,
#                     object_square NUMERIC (6, 2) NOT NULL,
#                     compensation NUMERIC (12, 3) NOT NULL
#                 );
#                 CREATE TABLE IF NOT EXISTS questions (
#                     id SERIAL PRIMARY KEY,
#                     user_id INTEGER NOT NULL,
#                     question TEXT NOT NULL,
#                     answer TEXT NOT NULL
#                 );
#             """
#             )
#
#     async def get_user(self, user_id: int) -> asyncpg.Record | None:
#         async with self.pool.acquire() as connection:
#             return await connection.fetchrow(
#                 "SELECT * FROM users WHERE user_id = $1", user_id
#             )
#
#     async def add_user(
#         self, user_id: int, username: str, first_name: str, last_name: str
#     ) -> None:
#         async with self.pool.acquire() as connection:
#             await connection.execute(
#                 """
#                 INSERT INTO users (user_id, username, first_name, last_name,
#                 created_at)
#                 VALUES ($1, $2, $3, $4, $5)
#             """,
#                 user_id,
#                 username,
#                 first_name,
#                 last_name,
#                 datetime.now(),
#             )
#
#     async def get_rate_for_date(self, date: datetime) -> float | None:
#         async with self.pool.acquire() as connection:
#             result = await connection.fetchrow(
#                 "SELECT rate FROM keyratecbr WHERE date <= $1 ORDER BY date DESC "
#                 "LIMIT 1",
#                 date,
#             )
#             result = float(result[0])
#             return result if result else None
#
#     async def add_penalty(
#         self,
#         user_id: int,
#         start_date: datetime,
#         end_date: datetime,
#         object_cost: float,
#         penalty: float,
#     ) -> None:
#         async with self.pool.acquire() as connection:
#             await connection.execute(
#                 """
#                 INSERT INTO penalties (user_id, start_date, end_date, object_cost,
#                 penalty)
#                 VALUES ($1, $2, $3, $4, $5)
#             """,
#                 user_id,
#                 start_date,
#                 end_date,
#                 object_cost,
#                 penalty,
#             )
#
#     async def add_defects(
#         self,
#         user_id: int,
#         city: str,
#         object_name: str,
#         object_square: float,
#         compensation: float,
#     ) -> None:
#         async with self.pool.acquire() as connection:
#             await connection.execute(
#                 """
#                 INSERT INTO defects (user_id, city, object_name,
#                 object_square, compensation)
#                 VALUES ($1, $2, $3, $4, $5)
#             """,
#                 user_id,
#                 city,
#                 object_name,
#                 object_square,
#                 compensation,
#             )
#
#     async def add_question(
#         self,
#         user_id: int,
#         question: str,
#         answer: str,
#     ) -> None:
#         async with self.pool.acquire() as connection:
#             await connection.execute(
#                 """
#                 INSERT INTO questions (user_id, question, answer)
#                 VALUES ($1, $2, $3)
#             """,
#                 user_id,
#                 question,
#                 answer,
#             )
#
#
# # async def create_redis_pool():
# #     return await aioredis.from_url("redis://localhost:6379", db=5)
