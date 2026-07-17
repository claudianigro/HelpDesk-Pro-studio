from .llm_provider import get_ai_response

def generate_reply(title, description, operator_notes=""):

    
    prompt = f"""
    Sei un assistente AI per un HelpDesk tecnico. 
    Il tuo compito è scrivere una bozza di risposta professionale, empatica e risolutiva da inviare al cliente.
    
    Titolo del ticket: {title}
    Descrizione del problema: {description}
    Appunti dell'operatore su come risolvere (se presenti): {operator_notes}
    Regole:
    1. Usa un tono cortese e professionale.
    2. Se ci sono "Appunti dell'operatore", basati su quelli per dare la soluzione.
    3. Se NON ci sono appunti, dai una risposta generica dicendo che il team sta prendendo in carico il problema.
    4. Restituisci SOLO il testo della mail/messaggio, senza frasi introduttive come "Ecco la risposta:".
    """
    
    raw_response = get_ai_response(prompt)
    
    # Puliamo eventuali spazi vuoti extra all'inizio e alla fine
    if raw_response.startswith("Errore"):
        return "Al momento non è possibile generare una bozza di risposta!"
    return raw_response.strip()

    