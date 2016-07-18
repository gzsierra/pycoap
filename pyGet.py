#!/usr/bin/python3
import logging, asyncio

from aiocoap import *

logging.basicConfig(level=logging.INFO)

@asyncio.coroutine
def main():
    protocol = yield from Context.create_client_context()

    request = Message(code=GET)
    request.set_request_uri('coap://127.0.0.1/temp/client1')

    try:
        response = yield from protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        resp = ((response.payload).decode("utf-8")).split(',')
        print(resp[1])

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
