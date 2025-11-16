from client import call_server
from time import perf_counter

# stap 2) Pas de code aan zodat je voor elke inlogpoging ziet hoe veel tijd er 
# tussen het versturen van de credentials en het ontvangen van het 
# antwoord zit:

# def timing_loginattempt(username, password, variance=0.01):
#     start = perf_counter()
#     reply = call_server(username, password, variance)
#     end = perf_counter()

#     duration = end - start # in seconden

#     return reply, duration

print(call_server('000000', 'hunter2'))