# -*- coding: utf-8 -*-


import contextlib
from typing import Optional, AsyncIterator

import asyncpg


from data import config


class Database:
    def __init__(self):
        self._pool: Optional[asyncpg.Pool] = None

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS product (
        id SERIAL PRIMARY KEY,
        type VARCHAR(100) NOT NULL,
        name VARCHAR(100) NOT NULL,
        price VARCHAR(15) NULL
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_tovar(self, type, name, price):
        sql = "INSERT INTO product (type, name, price) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, type, name, price, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM product"
        return await self.execute(sql, fetch=True)

    async def select_product(self, type):
        sql = "SELECT name, price, id FROM product WHERE type=$1"
        return await self.execute(sql, type, fetch=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM product"
        return await self.execute(sql, fetchval=True)

    async def update_name(self, name, id):
        sql = "UPDATE product SET name=$1 WHERE id=$2"
        return await self.execute(sql, name, id, execute=True)

    async def update_price(self, price, id):
        sql = "UPDATE product SET price=$1 WHERE id=$2"
        return await self.execute(sql, price, id, execute=True)

    async def delite_tovar(self, id):
        sql = "DELETE FROM product WHERE id=$1"
        return await self.execute(sql, id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM product WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE IF EXISTS product", execute=True)

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self._transaction() as connection:  # type: asyncpg.Connection
            if fetch:
                result = await connection.fetch(command, *args)
            elif fetchval:
                result = await connection.fetchval(command, *args)
            elif fetchrow:
                result = await connection.fetchrow(command, *args)
            elif execute:
                result = await connection.execute(command, *args)
        return result

    # Это можно просто скопировать для корректной работы с соединениями
    @contextlib.asynccontextmanager
    async def _transaction(self) -> AsyncIterator[asyncpg.Connection]:
        if self._pool is None:
            self._pool = await asyncpg.create_pool(
                user=config.DB_USER,
                password=config.DB_PASS,
                host=config.DB_HOST,
                database=config.DB_NAME,
            )
        async with self._pool.acquire() as conn:  # type: asyncpg.Connection
            async with conn.transaction():
                yield conn

    async def close(self) -> None:
        if self._pool is None:
            return None

        await self._pool.close()