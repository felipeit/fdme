from typing import Any
from rabbitmq_client import RMQConnection
from typing_extensions import Self

class RabbitMQConnection:
    _instance = None

    def __new__(cls, *args, **kwargs) -> Self:
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._connection = None
        return cls._instance

    def __init__(self, host='localhost', port=5672, username='guest', password='guest') -> None:
        if self._connection is None:
            self._parameters = {'host': host, 'port': port, 'username': username, 'password': password}
            self.connect()

    def connect(self) -> None:
        try:
            self._connection = RMQConnection(**self._parameters)
        except Exception as e:
            print(f"Failed to connect to RabbitMQ: {e}")

    def get_connection(self) -> Any:
        if self._connection is None or not self._connection.is_open:
            self.connect()
        return self._connection

# Exemplo de uso:
if __name__ == "__main__":
    rabbitmq_connection = RabbitMQConnection()
    connection = rabbitmq_connection.get_connection()
    # Faça o que precisar com a conexão...
