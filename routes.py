from fastapi import APIRouter, Body

from schemas import AnswerRequest, AnswerResponse

router = APIRouter()


@router.get(
    r"/answer",
    response_model=AnswerResponse
)
async def answer_get_handler(
        param1: int,
        param2: int,
        param3: int = 0,
) -> AnswerResponse:
    return AnswerResponse(
        answer=param1 + param2 + param3
    )


@router.post(
    r"/answer"
)
async def answer_post_handler(
        body_params: AnswerRequest = Body(),
) -> AnswerResponse:
    return AnswerResponse(
        answer=body_params.param1 + body_params.param2 + body_params.param3
    )
