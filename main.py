from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins=[
    "*", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
async def hello():
    return "hello User"

from app.api.tts import router as TTS_router
app.include_router(TTS_router, prefix='/api/tts')


if __name__=="__main__":
    import uvicorn;
    uvicorn.run(app, host='0.0.0.0', port=8000)