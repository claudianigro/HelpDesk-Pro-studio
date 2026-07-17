import json
from .llm_provider import get_ai_response

def classify_ticket(title, description):
    prompt = f"""Sei un esperto di supporto tecnico. Analizza il ticket inserito e categorizzalo.
    Le categorie ammesse sono [bug, support, feature_request, other]
    Le priorità ammesse sono [bassa, media, elevata, critica]
    Titolo : {title}
    Descrizione : {description}

    Rispondi esclusivamente in formato JSON con questa struttura: {{
        "categoria" :"valore",
        "priority" : "valore",
        "riassunto" : "breve spiegazione del problema"
    }}"""

    raw_response = get_ai_response(prompt)
    if raw_response.startswith("Errore"):
        return {
        "categoria": "NA", 
        "priorità": "NA", 
        "riassunto": "Servizio AI non disponibile"
    }
    try:
        clean_json = raw_response.strip().replace('```json', '').replace('```', '')
        return json.loads(clean_json)
    except Exception as e:
        print(f"Errore nel parsing dell'AI: {e}")
        