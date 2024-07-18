from contextlib import asynccontextmanager

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from settings import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self._session_factory = async_sessionmaker(
            bind=create_async_engine(
                url=url,
                echo=echo,
                poolclass=NullPool,
            ),
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    @asynccontextmanager
    async def get_session(self) -> AsyncSession:
        async with self._session_factory() as session:
            yield session
            await session.close()


db_helper = DatabaseHelper(
    url=str(settings.DB_URL),
    echo=False,
)
