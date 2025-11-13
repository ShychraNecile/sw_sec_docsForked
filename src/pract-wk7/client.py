import asyncio, websockets
from json import dumps, loads
from time import sleep
import time

### dit is de file waarin ik werk.
async def client_connect(username, password, variance=0.0):
    """Handle sending and receiving logins to & from the server.
    'while True' structure prevents singular network/socket
    errors from causing full crash.

    Parameters
    ----------
        username -- string of student ID for login attempt
        password -- string of password for login attempt
        variance -- float of maximum network delay

    Returns
    -------
        reply -- string of server's response to login attempt
    """
    # print("username is: " + username)
    # print("wachtwoord is: " + password)

    #server_address = "ws://20.224.193.77:8080"   # Hanze server
    server_address = "ws://127.0.0.1:8080"      # local (Docker) server
    
    while True:        
        try:
            start = time.time()
            async with websockets.connect(server_address) as websocket:

                await websocket.send(dumps([username, password, variance]))
                reply = await websocket.recv()

            # onderstaande toegevoegd
            end = time.time()
            rounded_end = round(end - start, 6)
            
            print(end-start)           
            print(rounded_end)
            # einde toevoeging 

            return loads(reply)
        except:
            continue

def call_server(username, password, variance=0.01):
    """Send a login attempt of username + password to the server
    and return the response. Optionally takes the variable variance to
    allow simulation of random network delays; the server will then
    delay its response by n microseconds, where 0 < n < variance.
    A higher variance will make guessing the password harder.


    Parameters
    ----------
        username -- string of student ID for login attempt
        password -- string of password for login attempt
        variance -- float of maximum delay, must be greater than 0.000001

    Returns
    -------
        reply -- string of server's response to login attempt
    """    
    print("aaaaaanvang")

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        reply = asyncio.run(client_connect(username, password, variance))
        print("bbbbbbbbb")         
    except KeyboardInterrupt:
        pass
        print("ccccc")
    sleep(0.001) # Wait so as to not overload the server with 90 students at once!

    print("dddddd")
    print("REPLY: " + reply)
    return (reply)

    print("eeeeeinde")


# Test basic server connectivity & functionality
#print(call_server('test', 'test'))
#print(call_server('000000', 'hunter2'))

# Gegeven: het wachtwoord bestaat alléén uit kleine letters en cijfers.



# for c in 'abcd...'

# temp_pass = c + 'a' * 6
#result = call_server('000000', 'hunter2')
result = call_server('000000', 'hunter3')
# print(result)