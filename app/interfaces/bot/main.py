import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from app.core.config import Settings

app = FastAPI()
load_dotenv()

@app.get("/")
async def root():
    return {"settings": settings}

if __name__ == '__main__':

    settings = Settings()
    print(settings)
    uvicorn.run(app)
