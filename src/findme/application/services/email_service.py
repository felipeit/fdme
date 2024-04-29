from src.core.tasks import send_email_task
from src.findme.domain.events.dto import GenericEvent
from src.findme.infra.message_queue.rabbitmq_conn import RabbitMQConnection


class SendEmailActiveUserHandler:
    supported_events: list[str] = ["pre-register", "input-received"]
    
    def __init__(self, queue: RabbitMQConnection = RabbitMQConnection()) -> None:
        self.queue = queue
    
    
    def run(self, event: GenericEvent) -> None:
        print("send email to ...", event)
        send_email_task.delay(
            'Ativação do usuário cadastrado', 
            f"""<p>Segue o link para ativação da conta {event.data.first_name} {event.data.last_name}<p><br>
            <a href="www.google.com"> ATIVAR CONTA </a>'""",
            'noreply@findme.com', 
            [event.data.email]
            )