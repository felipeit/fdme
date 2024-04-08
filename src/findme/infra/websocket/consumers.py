from typing import Any
from channels.generic.websocket import AsyncJsonWebsocketConsumer



class GeolocationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self) -> None:
        print("conectando...")
        await self.accept()

    async def receive_json(self, content, **kwargs) -> dict:
        print(content)
        return content
        
    async def disconnect(self, close_code: bool = True) -> None:
        print("desconectando...")
        await super().disconnect(code=close_code)

    # async def user_joined(self, event) -> None:
    #     await self.send(text_data=self.encode_json(event))
