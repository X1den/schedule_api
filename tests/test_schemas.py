from schemas import LessonCreate
from pydantic import ValidationError
import pytest

def test_valid_lesson():
    lesson = LessonCreate(
        title="Python lesson",
        start_time="2026-10-20T10:00:00+02:00",
        end_time="2026-10-20T11:00:00+02:00",
    )
    
    assert lesson.title == "Python lesson"
    assert lesson.start_time < lesson.end_time
    
def test_end_before_start():
    with pytest.raises(ValidationError):
        LessonCreate(
            title="Python lesson",
            start_time="2026-10-20T11:00:00+02:00",
            end_time="2026-10-20T10:00:00+02:00"
        )
        
def test_timezone():
    with pytest.raises(ValidationError):
        LessonCreate(
            title="Python lesson",
            start_time="2026-10-20T10:00:00",
            end_time="2026-10-20T11:00:00"
        )
        
def test_min_title():
    with pytest.raises(ValidationError):
        LessonCreate(
            title="HI",
            start_time="2026-10-20T10:00:00+02:00",
            end_time="2026-10-20T11:00:00+02:00"
        )
        
def test_max_title():
    with pytest.raises(ValidationError):
        LessonCreate(
            title="a" * 101,
            start_time="2026-10-20T10:00:00+02:00",
            end_time="2026-10-20T11:00:00+02:00"
        )