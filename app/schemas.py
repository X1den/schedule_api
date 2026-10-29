from pydantic import BaseModel, ConfigDict, Field, model_validator

from typing import Self
from datetime import datetime

class LessonBase(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    start_time: datetime
    end_time: datetime
    
    @model_validator(mode='after')
    def validate_time(self) -> Self:  
        if self.start_time is not None:
            if self.start_time.tzinfo is None or self.start_time.utcoffset() is None:
                raise ValueError("start_time must include a timezone")
            
        if self.end_time is not None:
            if self.end_time.tzinfo is None or self.end_time.utcoffset() is None:
                raise ValueError("end_time must include a timezone")
        
        if (
            self.start_time is not None
            and self.end_time is not None
            and self.start_time >= self.end_time
            ):
                raise ValueError("End time must be later than start time")
        
        return self
    
class LessonCreate(LessonBase):
    pass

class LessonUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=100)
    start_time: datetime | None = None
    end_time: datetime | None = None
    
    @model_validator(mode="after")
    def validate_time(self) -> Self:
        if self.start_time is not None:
            if self.start_time.tzinfo is None or self.start_time.utcoffset() is None:
                raise ValueError("start_time must include a timezone")
            
        if self.end_time is not None:
            if self.end_time.tzinfo is None or self.end_time.utcoffset() is None:
                raise ValueError("end_time must include a timezone")
            
        if (
            self.start_time is not None
            and self.end_time is not None
            and self.start_time >= self.end_time
        ):
            raise ValueError("end_time must be later than start_time")
        
        return self
    
class LessonRespone(LessonBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)