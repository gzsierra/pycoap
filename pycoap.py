import pyRead, sys, coapSender, asyncio

# Check File
pyRead.checkArg(sys.argv)
# Read File
file = pyRead.readFile(sys.argv[1])

# Send each line to the server
for line in file:
    split = line.split()
    # Make sure we wait until msg is send to server
    asyncio.get_event_loop().run_until_complete(coapSender.send(split[0], split[1]))
