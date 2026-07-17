
from fastapi import FastAPI

app = FastAPI(
    title="VisionBet AI",
    version="1.0.0",
    description="Artificial Intelligence Platform for Sports Betting Analysis"
)

@app.get("/")
def root():
    return {
        "status": "online",
        "application": "VisionBet AI",
        "version": "1.0.0"
    }
