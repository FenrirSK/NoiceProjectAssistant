from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.voice import router as voice_router


app = FastAPI(
    title="Noice Project Assistant",
    description="Voice-to-command layer for project management software",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(voice_router)

@app.get("/")
def home():
    return {
        "message": "Noice Project Assistant is running!"
    }
    
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
    

    