from app.schemas import LessonBase, LessonUpdate
from pydantic import ValidationError
from datetime import datetime
import pytest

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_valid_lesson():
    lesson = LessonBase(
        title="Python lesson",
        start_time=datetime.fromisoformat("2026-10-20T10:00:00+02:00"),
        end_time=datetime.fromisoformat("2026-10-20T11:00:00+02:00"),
    )

    assert lesson.title == "Python lesson"
    assert lesson.start_time < lesson.end_time


def test_end_before_start():
    with pytest.raises(ValidationError):
        LessonBase(
            title="Python lesson",
            start_time=datetime.fromisoformat("2026-10-20T11:00:00+02:00"),
            end_time=datetime.fromisoformat("2026-10-20T10:00:00+02:00"),
        )


def test_timezone():
    with pytest.raises(ValidationError):
        LessonBase(
            title="Python lesson",
            start_time=datetime.fromisoformat("2026-10-20T10:00:00"),
            end_time=datetime.fromisoformat("2026-10-20T11:00:00"),
        )


def test_min_title():
    with pytest.raises(ValidationError):
        LessonBase(
            title="HI",
            start_time=datetime.fromisoformat("2026-10-20T10:00:00+02:00"),
            end_time=datetime.fromisoformat("2026-10-20T11:00:00+02:00"),
        )


def test_max_title():
    with pytest.raises(ValidationError):
        LessonBase(
            title="a" * 101,
            start_time=datetime.fromisoformat("2026-10-20T10:00:00+02:00"),
            end_time=datetime.fromisoformat("2026-10-20T11:00:00+02:00"),
        )
        
def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}
    