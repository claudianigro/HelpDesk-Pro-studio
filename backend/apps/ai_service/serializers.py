from rest_framework import serializers

class TicketClassificationSerializer(serializers.Serializer):
    ticket_id = serializers.IntegerField(
        required=True,
        error_messages={
            'required': 'Devi specificare l\'ID del ticket da classificare.',
        }
    )


class ReplyGenerationSerializer(serializers.Serializer):
    ticket_id = serializers.IntegerField(
        required=True,
        error_messages={'required': 'Manca l\'ID del ticket.'}
    )
    operator_notes = serializers.CharField(required=False, allow_blank=True, default="")


class TicketSummarizerSerializer(serializers.Serializer):
    title = serializers.CharField(
        max_length=255, 
        required=True,
        error_messages={'required': 'Titolo obbligatorio per il riassunto.', 'blank': 'Titolo non valido.'}
    )
    description = serializers.CharField(
        required=True,
        error_messages={'required': 'Descrizione obbligatoria per il riassunto.', 'blank': 'Descrizione non valida.'}
    )
    history = serializers.CharField(required=False, allow_blank=True, default="")
class DuplicateCheckSerializer(serializers.Serializer):
    ticket_id = serializers.IntegerField(
        required=True,
        error_messages={'required': 'Manca l\'ID del ticket da controllare.'}
    )