from fastapi import FastAPI, UploadFile, File, Request
import shutil
import os
from datetime import datetime
import httpx
app = FastAPI()

# Создаем папку для входящих событий, если её нет
UPLOAD_DIR = "received_events"
os.makedirs(UPLOAD_DIR, exist_ok=True)
CORE_API_URL = "http://localhost:8001/core/event-receiver"

async def send_to_core(event_id: str, filename: str, user_id: int):
    """Функция-клиент для отправки данных в Core API"""
    payload = {
        "event_id": event_id,
        "filename": filename,
        "user_id": user_id,
        "status": "processed",
        "timestamp": "2026-04-15T12:10:00" # В реальном проекте используй datetime.now()
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(CORE_API_URL, json=payload)
            return response.status_code
        except Exception as e:
            print(f"[ERROR] Не удалось связаться с Core API: {e}")
            return None




@app.post("/eventProcessor/img")
async def process_image(file: UploadFile = File(...)):
    # Формируем путь для сохранения
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    # Сохраняем файл на диск
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    print(f" [!] Событие обработано: сохранен файл {file.filename}")
    metadata = {
        "event_id": "uuid-999",
           "filename": file.filename,
           "user_id": 42,
           "status": "detected",
           "timestamp": datetime.now().isoformat()}
    core_status = await send_to_core(metadata['event_id'], metadata['filename'], metadata['user_id'])
    if core_status != 200:
        return {"status": "error", "message": "Failed to send event to core"}
    return {
        "status": "success",
        "message": f"Image {file.filename} processed and saved",
        "size": os.path.getsize(file_path),
        "core_status": core_status
    }
@app.post('/eventProcessor/metadata')
async def get_metadata(response: Request):
    metadata = await response.json()
    return {"status": "metadata is ok", "metadata": metadata}

@app.get('/eventProcessor/event-receiver')
async def receive_event():
    
    return {"status": "event is ok", "core_status": 200}

if __name__ == "__main__":
    import uvicorn
    # Запускаем именно на 8000 порту, как указано в условии
    uvicorn.run(app, port=8000)