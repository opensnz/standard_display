import asyncio
import websockets
from modules.handler import Handler


class Server():

    def __init__(self, host : str, port : int):
        self.host = host
        self.port = port
        self.__server = None
        self.__handler = Handler()


    
    async def __start__(self):
        self.__server = await websockets.serve(self.__handle__, self.host, self.port)
        await self.__server.wait_closed()
        

    def run(self) -> None:
        """run server forever"""
        try :
            print("Local Server running...")
            asyncio.run(self.__start__())
        except:
            pass


    async def __handle__(self, websocket, path):
        try:
            while True:
                # Receiving message from the client
                data = await websocket.recv()
                response = self.__handler.handle(data)
                await websocket.send(response)
                


        except websockets.exceptions.ConnectionClosed:
            # Connection has been closed by the client or the server
            print("Connection closed")



