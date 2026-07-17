from .llm_provider import get_ai_response

def check_duplicate(new_title, new_description, recent_tickets):
    
    prompt = f"""
    Sei un sistema di deduplicazione per un HelpDesk.
    Il tuo compito è capire se un NUOVO ticket è lo stesso identico problema di uno dei TICKET RECENTI.
    
    NUOVO TICKET:
    Titolo: {new_title}
    Descrizione: {new_description}
    
    TICKET RECENTI (Lista):
    {recent_tickets}
    
    Regole fondamentali:
    1. Analizza il significato del problema, non solo le parole esatte.
    2. Se trovi che il NUOVO TICKET è un duplicato evidente di uno dei TICKET RECENTI, rispondi ESCLUSIVAMENTE con l'ID numerico del ticket duplicato (es. "42").
    3. Se NON ci sono duplicati o sei in dubbio, rispondi ESCLUSIVAMENTE con la parola "NONE".
    4. Non aggiungere NESSUN'ALTRA parola, spiegazione o punteggiatura alla tua risposta. Devi essere un output formattato per un computer.
    """
    
    raw_response = get_ai_response(prompt)
    result = raw_response.strip().upper()

    if result.startswith("ERRORE"):
        return {"is_duplicate": False, "duplicate_id": None, "error": raw_response}

    if result == "NONE":
        return {"is_duplicate": False, "duplicate_id": None}

    if result.isdigit():
        return {"is_duplicate": True, "duplicate_id": int(result)}
    
    return {"is_duplicate": False, "duplicate_id": None, "error": "Risposta AI in formato inatteso"}