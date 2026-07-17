```bash
📘 Documentazione Architettura Cloud
AI HelpDesk – Layer 3 (AWS Cloud Architecture)

🎯 Obiettivo
L’obiettivo di questo layer è distribuire il sistema AI HelpDesk su infrastruttura AWS garantendo:
Scalabilità automatica
Alta disponibilità
Sicurezza dei dati
Gestione centralizzata dei segreti
Integrazione con servizi di Intelligenza Artificiale esterni

🧩 Componenti del Sistema
L’architettura supporta i seguenti componenti:
Frontend Web: React
Backend API: Django + Django REST Framework
Database: PostgreSQL
File Storage: gestione allegati
AI Integration: OpenAI / Gemini / Anthropic

🏗 Architettura Generale
Diagramma Architetturale (Logico)
                   Internet
                       │
                 ┌─────▼─────┐
                 │ Route 53  │
                 │   (DNS)   │
                 └─────┬─────┘
                       │
                 ┌─────▼─────┐
                 │CloudFront │
                 │ CDN + SSL │
                 └─────┬─────┘
                       │
                       ▼
             ┌──────────────────┐
             │ Load Balancer    │
             │      (ALB)       │
             └─────┬──────┬─────┘
                   ▼      ▼
             ┌────────┐ ┌────────┐
             │  EC2   │ │  EC2   │
             │Django  │ │Django  │
             └────┬───┘ └────┬───┘
                  │           │
                  └────┬──────┘
                       ▼
                  ┌──────────┐
                  │   RDS    │
                  │PostgreSQL│
                  └────┬─────┘
                       │
                       ▼
                  ┌──────────┐
                  │    S3    │
                  │ Storage  │
                  └────┬─────┘
                       ▼
                   AI APIs


🔄 Flusso principale
User → Route53 → CloudFront → ALB → EC2 → RDS/S3 → AI APIs

☁️ Servizi AWS Utilizzati
Servizio - Funzione
Route 53 DNS e gestione dominio
CloudFront CDN globale + HTTPS
Amazon S3 Storage frontend e allegati
Application Load Balancer Bilanciamento traffico
EC2 Backend Django
Auto Scaling Group Scalabilità automatica
Amazon RDS Database PostgreSQL
Secrets Manager Gestione credenziali
CloudWatch Monitoring
IAM Controllo accessi
AWS Certificate Manager Certificati SSL


🔍 Descrizione dei Componenti

🌐 Route 53
Gestisce il dominio e il routing DNS.

Funzioni:
- Risoluzione DNS
- Alta disponibilità
- Routing verso CloudFront

Perché è stato scelto:
- Servizio DNS completamente gestito e altamente affidabile
- Integrazione nativa con servizi AWS

⚡ CloudFront (CDN)
Distribuisce il frontend statico a livello globale.

Funzioni:
- Caching contenuti
- Riduzione latenza (<50ms)
- Terminazione HTTPS

Flusso: S3 → CloudFront → User

Perché è stato scelto:
- Migliora le performance globali
- Riduce il carico sui server backend

🗂 Amazon S3

Utilizzato per:
- Hosting frontend React
- Archiviazione allegati ticket
- Backup e log

Struttura esempio:
s3://helpdesk-storage/
├── frontend/
├── attachments/
├── static/
└── backups/

Perché è stato scelto:
- Storage scalabile e a basso costo
- Alta durabilità (99.999999999%)

⚖️ Application Load Balancer (ALB)
Gestisce il traffico verso il backend.

Funzioni:
- Bilanciamento carico
- HTTPS termination
- Health checks
- Routing API

Configurazione: Redirect HTTP → HTTPS

Endpoint: /api/health/

Perché è stato scelto:
- Distribuzione intelligente del traffico
- Integrazione con Auto Scaling

🖥 EC2 Instances
Server che eseguono il backend Django.

Stack:
Ubuntu 24.04
Docker
Django + DRF
Gunicorn
Nginx

Parametro - Valore
Instance type t3.micro
Auto Scaling 2–6
Deployment Docker

Perché è stato scelto:
- Massima flessibilità e controllo sull’ambiente
- Supporto per container Docker

📈 Auto Scaling Group
Gestisce automaticamente il numero di istanze EC2.

Parametro - Valore
Min 2
Desired 2
Max 6

Policy:
CPU > 70% → +1 istanza
CPU < 40% → -1 istanza

Perché è stato scelto:
- Scalabilità automatica
- Alta resilienza

🗄 Amazon RDS (PostgreSQL)
Database relazionale gestito.

Dati:
Users
Tickets
Comments
Categories

Parametro - Valore
Engine PostgreSQL
Instance db.t4g.micro
Storage 20GB
Multi-AZ Attivo

Failover: < 60s

Perché è stato scelto:
- Gestione automatica backup e failover
- Riduzione complessità operativa

🔐 AWS Secrets Manager
Gestione sicura delle credenziali.

Perché è stato scelto:
- Evita credenziali hardcoded
- Supporta rotazione automatica

📊 Amazon CloudWatch
Sistema di monitoraggio.

Perché è stato scelto:
- Monitoraggio centralizzato
- Integrazione con alert automatici

🔒 Strategia di Sicurezza
IAM (Least Privilege)
Accesso minimo necessario per ogni servizio.

🔥 Security Groups
ALB → accesso pubblico (80, 443)
EC2 → accesso solo da ALB
RDS → accesso solo da EC2
👉 Database non esposto su Internet

🔐 HTTPS
Gestito tramite AWS Certificate Manager (ACM).

🛡 Misure aggiuntive
AWS WAF → protezione attacchi web
VPC Endpoints → traffico privato
CloudTrail → auditing
GuardDuty → threat detection
SSM → accesso sicuro senza SSH

📈 Scalabilità e Alta Disponibilità

Scalabilità 
Utenti - Istanze 
100 2
1000 5
5000 10

Alta disponibilità
Componente - Strategia
EC2 - Auto Scaling
RDS - Multi-AZ
ALB - Multi-zone
CloudFront - Globale

Gestione guasti:
EC2 → sostituzione automatica
AZ → failover
DB → failover automatico
Disponibilità stimata: 99.95%

🤖 Integrazione AI
User → Frontend → Django API → AI Layer → Provider AI

Funzionalità:
- Classificazione ticket
- Suggerimento risposte
- Summarization
- Ricerca semantica

🚀 CI/CD (Opzionale)
GitHub → GitHub Actions → Docker → ECR → EC2

💰 Stima Costi Mensili
Servizio - Costo
EC2 $0
RDS $28
ALB $22
S3 $0.25
CloudFront $0.90
Secrets Manager $4.50
CloudWatch $5
EBS $1.60

Totale: ≈ $62/mese

🔮 Estensioni Future
Redis (ElastiCache)
SQS
ECS / EKS
AWS Lambda

✅ Vantaggi
✔ Altamente scalabile
✔ Resiliente ai guasti
✔ Sicurezza avanzata
✔ AI-ready
✔ Costi controllati
✔ Servizi gestiti AWS 

