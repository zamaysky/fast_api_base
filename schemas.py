from pydantic import BaseModel


class AnswerRequest(BaseModel):
    param1: int
    param2: int
    param3: int = 0


class AnswerResponse(BaseModel):
    answer: int
