from fastapi import APIRouter , HTTPException
from gtts import gTTS
from fastapi.responses import FileResponse
import os

router= APIRouter()

@router.post('/tts')
async def create_audiobook(text: str, filename: str = "audiobook.mp3"):
    try:
        tts = gTTS(text)
#       tts.save(filename)
        return FileResponse(filename, media_type='audio/mpeg', filename=filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
