from .models import Ticket

TICKET_WORKFLOW = {
    Ticket.StatusChoice.OPEN: [Ticket.StatusChoice.IN_PROGRESS],
    Ticket.StatusChoice.IN_PROGRESS: [
        Ticket.StatusChoice.RESOLVED,
        Ticket.StatusChoice.OPEN
    ],
    Ticket.StatusChoice.RESOLVED: [Ticket.StatusChoice.CLOSED],
}