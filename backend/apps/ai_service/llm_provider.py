import os
from google import genai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_ai_response(prompt):
    provider = os.getenv("AI_DEFAULT_PROVIDER", "gemini").lower()

    # GOOGLE GEMINI
    if provider == "gemini":
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            return "Errore: Manca la GEMINI_API_KEY nel file .env"
        
        client = genai.Client(api_key=api_key)
        
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Errore durante la chiamata a Gemini: {str(e)}"

    # --- OPENAI 
    elif provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "Errore: Manca la OPENAI_API_KEY nel file .env"
            
        client = OpenAI(api_key=api_key)
        
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Sei un assistente tecnico preciso."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Errore durante la chiamata a OpenAI: {str(e)}"

    return "Errore: Provider non riconosciuto."