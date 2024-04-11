import json
from time import sleep
import pytest


@pytest.mark.asyncio
async def test_my_consumer(communicator_fixture) -> None:
    try:
        # arrange
        connected, subprotocol = await communicator_fixture.connect()
        
        # act
        await communicator_fixture.send_json_to({"hello": "world"})
        response = communicator_fixture.input_queue._queue[0]
        
        # assert
        assert connected
        assert response['type'] == 'websocket.receive'
        assert json.loads(response['text']) == {"hello": "world"}
    finally:
        await communicator_fixture.disconnect()
