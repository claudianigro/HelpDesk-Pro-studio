🗄 Database ER Diagram
erDiagram

    USER {
        int id PK
        string username
        string email
        string password
        string role
        boolean is_active
        datetime created_at
    }

    TICKET {
        int id PK
        string title
        text description
        string status
        string priority
        int author_id FK
        int category_id FK
        datetime created_at
        datetime updated_at
    }

    CATEGORY {
        int id PK
        string name
        text description
    }

    COMMENT {
        int id PK
        int ticket_id FK
        int author_id FK
        text content
        datetime created_at
    }

    TICKET_ASSIGNMENT {
        int id PK
        int ticket_id FK
        int operator_id FK
        datetime assigned_at
    }

    TICKET_HISTORY {
        int id PK
        int ticket_id FK
        string old_status
        string new_status
        int changed_by FK
        datetime changed_at
    }

    USER ||--o{ TICKET : creates
    USER ||--o{ COMMENT : writes
    USER ||--o{ TICKET_ASSIGNMENT : assigned_to
    USER ||--o{ TICKET_HISTORY : changes

    CATEGORY ||--o{ TICKET : categorizes

    TICKET ||--o{ COMMENT : has
    TICKET ||--|| TICKET_ASSIGNMENT : assigned
    TICKET ||--o{ TICKET_HISTORY : history


🧠 Descrizione
User → gestisce autenticazione e ruoli (cliente, operatore, admin)

Ticket → entità principale del sistema

Category → classificazione dei ticket

Comment → conversazione tra utenti

TicketAssignment → assegnazione operatori

TicketHistory → tracciamento modifiche stato

🔥 Note progettuali

Separazione assignment → maggiore flessibilità

Tabella history → audit completo

Struttura modulare → facile estensione


```bash
USER
+----------------+
| id (PK)        |
| username       |
| email          |
| password       |
| role           |
| is_active      |
| created_at     |
+----------------+
       || 
       || creates
       o|
TICKET
+----------------+
| id (PK)        |
| title          |
| description    |
| status         |
| priority       |
| author_id (FK) |
| category_id(FK)|
| created_at     |
| updated_at     |
+----------------+
       || assigned
       || 
       || 1
TICKET_ASSIGNMENT
+----------------+
| id (PK)        |
| ticket_id (FK) |
| operator_id(FK)|
| assigned_at    |
+----------------+

TICKET ||--o{ COMMENT : has
COMMENT
+----------------+
| id (PK)        |
| ticket_id (FK) |
| author_id(FK)  |
| content        |
| created_at     |
+----------------+

TICKET ||--o{ TICKET_HISTORY : history
TICKET_HISTORY
+----------------+
| id (PK)        |
| ticket_id (FK) |
| old_status     |
| new_status     |
| changed_by(FK) |
| changed_at     |
+----------------+

CATEGORY ||--o{ TICKET : categorizes
CATEGORY
+----------------+
| id (PK)        |
| name           |
| description    |
+----------------+




