import logging, asyncio, pyRead, sys

from aiocoap import *

logging.basicConfig(level=logging.INFO)

@asyncio.coroutine
def main():

    # Check File
    pyRead.checkArg(sys.argv)
    # Read File
    pyRead.readFile(sys.argv[1])

    protocol = yield from Context.create_client_context()

    request = Message(code=GET)
    request.set_request_uri('coap://localhost/time')

    try:
        response = yield from protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print('Result: %s\n%r'%(response.code, response.payload))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
