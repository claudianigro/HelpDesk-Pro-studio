import json
from .llm_provider import get_ai_response
from apps.categories.models import Category

def classify_ticket(title, description):
    categorie_disponibili = list(Category.objects.filter(is_active=True).values_list('name', flat=True))
    categorie_str = ", ".join(categorie_disponibili) if categorie_disponibili else "Hardware, Software, Rete"

    prompt = f"""Sei un esperto di supporto tecnico. Analizza il ticket inserito e categorizzalo.
    Le categorie ammesse sono ESATTAMENTE queste, scegli solo tra queste: [{categorie_str}]
    Le priorità ammesse sono [bassa, media, elevata, critica]
    Titolo : {title}
    Descrizione : {description}

    Rispondi esclusivamente in formato JSON con questa struttura: {{
        "categoria" :"valore",
        "priority" : "valore",
        "riassunto" : "breve spiegazione del problema"
    }}"""

    raw_response = get_ai_response(prompt)
    
    print(f"\n--- DEBUG AI RESPONSE ---\n{raw_response}\n------------------------\n")
    
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
        return {
            "categoria": "NA", 
            "priorità": "NA", 
            "riassunto": "Errore parsing risposta AI"
        }