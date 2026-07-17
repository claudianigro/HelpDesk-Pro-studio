```bash
🚀 Helpdesk AI – Sistema di Ticketing per Supporto Tecnico

📌Overview 
Helpdesk AI è una piattaforma di ticketing avanzata progettata per centralizzare e ottimizzare la gestione del supporto tecnico.
Nasce per risolvere i problemi tipici delle software house in crescita che gestiscono richieste via email:
❌ difficoltà nel tracciare le richieste
❌ assegnazione inefficiente del lavoro
❌ scarsa visibilità sullo stato dei ticket
❌ impossibilità di analizzare i tempi di risposta
✅ La soluzione: un sistema moderno, scalabile e potenziato dall’AI.

🎯 Obiettivo 
Costruire una piattaforma centralizzata dove:
i clienti aprono ticket
gli operatori li gestiscono
gli admin controllano tutto il sistema
Con integrazione AI per:
automatizzare processi
ridurre i tempi di risposta
migliorare la qualità del supporto

🧠 Funzionalità AI
Il sistema integra moduli intelligenti per:
🏷 Classificazione automatica ticket
✍️ Suggerimento risposta operatore
🔍 Rilevamento duplicati
🧾 Riassunto ticket complessi

🏗 Architettura del Sistema 
Applicazione composta da:
🌐 Frontend Web (React)
⚙️ Backend API (Django + DRF)
🗄 Database (SQLite)
🤖 Modulo AI
🔐 Sistema di autenticazione (JWT)

🛠 Tech Stack

Backend: 
Django 5.1
Django REST Framework 3.15
JWT (SimpleJWT)

Frontend: 
React 18
Vite
Tailwind CSS
Database
SQLite 
AI
Google Gemini 1.5
Cloud / Deploy
AWS (EC2, RDS, S3, ALB, CloudFront)

📂 Struttura del Progetto

helpdesk-ai/
├── backend/
├── frontend/
├── docs/
├── README.md
└── requirements.txt

Backend (Django)
bash
backend/
├── config/
├── apps/
│   ├── users/
│   ├── tickets/
│   ├── comments/
│   ├── categories/
│   └── ai_service/
├── core/
├── api/
└── tests/

Frontend (React)
bash
frontend/
├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── hooks/
│   ├── context/
│   └── routes/


🎫 Sistema Ticket

📌 Campi principali
titolo
descrizione
categoria
priorità
autore
allegati

🔄 Workflow Ticket
OPEN → IN_PROGRESS → WAITING_FEEDBACK → RESOLVED → CLOSED

Regole:
non si può chiudere senza risolvere
ticket chiusi possono essere riaperti
ogni modifica è tracciata

💬 Commenti
supporto thread conversazionale
allegati
storico completo

👥 Ruoli e Permessi
Ruolo
Permessi
Cliente
Crea ticket, commenta, visualizza
Operatore
Gestisce ticket assegnati
Admin
Controllo completo sistema


🔐 Sicurezza
Autenticazione JWT
Controllo accessi per ruolo
Protezione endpoint API

🔌 API REST
Base URL
/api/

Autenticazione
Authorization: Bearer <token>

Endpoint principali:

Auth
POST /auth/login/
POST /auth/register/

Tickets
GET /tickets/
POST /tickets/
GET /tickets/{id}/
PUT /tickets/{id}/

Commenti
GET /comments/ticket/{id}/
POST /comments/ticket/{id}/

AI
POST /ai/classify-ticket
POST /ai/suggest-reply
POST /ai/detect-duplicates
POST /ai/summarize-ticket

⚙️ Installazione

Backend
# 1. Clona il repository
git clone https://github.com/username/helpdesk-ai.git
cd helpdesk-ai

# 2. Crea virtual environment
python -m venv venv

# attiva:
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# 3. Installa dipendenze
pip install -r requirements.txt

# 4. Configura variabili ambiente
cp .env.example .env

# 5. Migrazioni database
python manage.py migrate

# 6. Avvia server
python manage.py runserver

-----------

Frontend
cd frontend

npm install
npm run dev


🔐 Environment Variables
Crea un file .env nella root del backend:
DEBUG=True
SECRET_KEY=your_django_secret_key

# Database 
DATABASE_URL=sqlite:///db.sqlite3

GEMINI_API_KEY=your_gemini_key
JWT_SECRET_KEY=your_jwt_secret

Dove ottenere le chiavi
Google Gemini → https://ai.google.dev/

🚀 Utilizzo
Registrati o effettua il login
Crea un nuovo ticket
Visualizza i ticket nella dashboard
Filtra per stato, priorità o categoria
Accedi al dettaglio del ticket
Aggiungi commenti

(Operatore) gestisci e aggiorna lo stato del ticket
Usa le funzionalità AI:
classificazione automatica
suggerimento risposta
riassunto ticket
rilevamento duplicati

🚀 Deploy (AWS)

Architettura:
User → CloudFront → ALB → EC2 → RDS
                         ↓
                        S3
                         ↓
                      AI APIs

Servizi utilizzati:
EC2 (backend)
RDS (database)
S3 (storage)
CloudFront (CDN)
ALB (load balancing)

🔄 Workflow Git
main → produzione
develop → sviluppo
Flusso:
feature → pull request → develop → main


📚 Documentazione
Disponibile in:
/docs/

Include:
API documentation
Architettura sistema AWS
Diagrammi

👥 Team
Chiara Giovoni – Backend (API, Auth)
Angelica Sangregorio – Frontend (UI, React)
Claudia Nigro – Backend (AI Integration)
Giulia Ferrandina – Backend (Database & Models)
Emily D’Ugo – Backend (Business Logic)

📄 Licenza
MIT License

