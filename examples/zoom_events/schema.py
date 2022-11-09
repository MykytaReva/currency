from pydantic import  UUID4, BaseModel, EmailStr, Field, validator

class ZoomEventCreate(BaseModel):
    event: str
    event_ts: int
    payload: dict