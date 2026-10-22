from fastapi import FastAPI, HTTPException
from schemas import LessonCreate

app = FastAPI()

lessons = []
next_lesson_id = 1

@app.get("/status")
async def get_status():
    return {"message": "API is running"}

@app.post("/lessons")
async def post_lessons(lesson: LessonCreate):
    lesson_data = lesson.model_dump()
    lesson_data["id"] = next_lesson_id
    
    lessons.append(lesson_data)
    next_lesson_id +=1
    
    return lesson_data

@app.get("/lessons")
async def get_lessons(lesson_id: int):
    return lessons

@app.get("/lessons/{lesson_id}")
async def get_lesson(lesson_id: int):
    for lesson in lessons:
        if lesson["id"] == lesson_id:
            return lesson
        
    raise HTTPException(
        status_code=404,
        detail="Lesson not found"
    )