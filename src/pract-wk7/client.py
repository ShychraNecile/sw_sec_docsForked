import asyncio, websockets
from json import dumps, loads
from time import sleep
from time import time


async def client_connect(username, password, variance=0.0):   
    server_address = "ws://127.0.0.1:8080"      # local (Docker) server
      
    while True:        
        try:         
            start = time.time()      
              
            async with websockets.connect(server_address) as websocket:
                await websocket.send(dumps([username, password, variance]))
                reply = await websocket.recv() 
            #end = time.time()
            # eindtijd_inlogpoging = time.time_ns()           
            # tijdsduur_inlogpoging = round(eindtijd_inlogpoging - starttijd_inlogpoging, 6)
            #print(starttijd_inlogpoging)
            #print(f"Tijdsduur inlogpoging: {tijdsduur_afgerond}")
            # print(tijdsduur_afgerond)

            print(round(start,6))
            return loads(reply)
        except:
            continue


def call_server(username, password, variance=0.01):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        reply = asyncio.run(client_connect(username, password, variance))               
    except KeyboardInterrupt:
        pass

    sleep(0.001) # Wait so as to not overload the server with 90 students at once!
   
    return(reply)

####Pas de code aan zodat je voor elke inlogpoging ziet hoe veel tijd er 
# tussen het versturen van de credentials en het ontvangen van het antwoord zit.



# Test basic server connectivity & functionality
#print(call_server('test', 'test'))
print(call_server('000000', 'hunter2'))