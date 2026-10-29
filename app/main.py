from fastapi import FastAPI, HTTPException
from app.schemas import LessonBase, LessonUpdate

app = FastAPI()

lessons = []
next_lesson_id = 1

@app.get("/status")
async def get_status():
    return {"message": "API is running"}

@app.post("/lessons")
async def post_lessons(lesson: LessonBase):
    global next_lesson_id
    
    lesson_data = lesson.model_dump()
    lesson_data["id"] = next_lesson_id
    
    lessons.append(lesson_data)
    next_lesson_id +=1
    
    return lesson_data

@app.get("/lessons")
async def get_lessons():
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
    
@app.patch("/lessons/{lesson_id}")
async def update_lesson(lesson_id: int, lesson_update: LessonUpdate):
    for lesson in lessons:
        if lesson["id"] == lesson_id:
            update_data = lesson_update.model_dump(exclude_unset=True)
            lesson.update(update_data)
            return lesson
            
    raise HTTPException(
        status_code=404,
        detail="Lesson not found"
    )
    
@app.delete("/lessons/{lesson_id}")
async def delete_lesson(lesson_id: int):
    for lesson in lessons:
        if lesson["id"] == lesson_id:
            lessons.remove(lesson)
            return {"message": "Lesson deleted successfully"}
    
    raise HTTPException(
        status_code=404,
        detail="Lesson not found"
    )
