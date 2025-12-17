from pydantic import BaseModel

class RoundStateResponse(BaseModel):
    state:str
    message:str
