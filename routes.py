from typing import Annotated

from fastapi import APIRouter, Depends
from starlette.requests import Request

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


@router.get(
    r"/answer",
)
async def answer_get_handler(
        first_depends: Annotated[None, Depends(FirstDependsWithParams(1, 2)),],
        second_depends: Annotated[None, Depends(second_depends_with_params(1, 2))]
) -> str:
    return "suscess"
