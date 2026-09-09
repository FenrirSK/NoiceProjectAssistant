from fastapi import FastAPI

app = FastAPI(
    title="Noice Project Assistant",
    description="Voice-to-command layer for project management software",
    version="1.0.0"
)

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