from pydantic import BaseModel, Field, model_validator

from typing import Self
from datetime import datetime

class LessonCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    start_time: datetime
    end_time: datetime
    
    @model_validator(mode='after')
    def validate_time(self) -> Self:  
        if self.start_time.tzinfo is None or self.start_time.utcoffset() is None:
            raise ValueError("start_time must include a timezone")
        
        if self.end_time.tzinfo is None or self.end_time.utcoffset() is None:
            raise ValueError("end_time must include a timezone")
        
        if self.start_time >= self.end_time:
            raise ValueError("End time must be later than start time")
        
        return self