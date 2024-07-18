from typing import Annotated, Iterator

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from db_helper import db_helper

router = APIRouter()


class FirstDependsWithParams:
    def __init__(self, param_1: int, param_2: int):
        self.param_1 = param_1
        self.param_2 = param_2

    async def __call__(self, request: Request) -> None:
        print(request)
        print(self.param_1, self.param_2)


def second_depends_with_params(param_1: int, param_2: int):
    def inner(request: Request) -> None:
        print(request)
        print(param_1, param_2)

    return inner


async def get_session_depends() -> Iterator[AsyncSession]:
    async with db_helper.get_session() as session:
        yield session

@router.get(
    r"/answer",
)
async def answer_get_handler(
        session_depends: Annotated[AsyncSession, Depends(get_session_depends)]
) -> str:
    print(session_depends)
    return "suscess"
