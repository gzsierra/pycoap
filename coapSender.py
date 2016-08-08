import logging, asyncio

from aiocoap import *

logging.basicConfig(level=logging.INFO)
@asyncio.coroutine

def send(time, value):
    # print("Send to server")

    context = yield from Context.create_client_context()

    # yield from asyncio.sleep(2)

    payload = (time +","+ value).encode()
    request = Message(code=PUT, payload=payload)
    request.opt.uri_host = 'localhost'
    request.opt.uri_path = ('temp', 'client1')

    response = yield from context.request(request).response

    print('Result: %s\n%r'%(response.code, response.payload))
