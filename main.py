from fastapi import FastAPI
from pydantic import BaseModel
from deep_translator import GoogleTranslator

app = FastAPI()

# Data lene ka format (Schema)
class TranslationRequest(BaseModel):
    text: str          # Jo likha hua translate karna hai
    target_lang: str   # Jis zaban mein karna hai (ur, hi, en, ar)

@app.get("/")
def home():
    return {"status": "Online", "message": "Translator API chal rahi hai!"}

@app.post("/translate")
def translate_text(item: TranslationRequest):
    try:
        # Google Translate ka free version use kar rahe hain
        translator = GoogleTranslator(source='auto', target=item.target_lang)
        result = translator.translate(item.text)
        
        return {
            "success": True,
            "original_text": item.text,
            "translated_text": result,
            "target_lang": item.target_lang
        }
    except Exception as e:
        return {"success": False, "error": str(e)}

# Local run karne ke liye (sirf testing ke liye)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
