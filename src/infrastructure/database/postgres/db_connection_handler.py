from contextlib import asynccontextmanager

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


class DbConnectionHandler:
    """Postgres database connection"""

    def __init__(self) -> None:
        self.__connection_string = "postgresql+asyncpg://postgres:articlepwd@localhost:5432/article_db"

    @property
    def __get_engine(self):
        """Return connection engine"""

        engine = create_async_engine(
            self.__connection_string, future=True, echo=False)
        return engine

    def __async_session_generator(self) -> AsyncSession:
        """generate async session"""
        return sessionmaker(
            bind=self.__get_engine, expire_on_commit=False, class_=AsyncSession
        )

    @asynccontextmanager
    async def get_session(self):
        """get session"""
        async_session = self.__async_session_generator()

        try:
            async with async_session() as session:
                yield session
        except:
            await session.rollback()
            raise
        finally:
            await session.close()
