from client import call_server

# stap 2) Pas de code aan zodat je voor elke inlogpoging ziet hoe veel tijd er 
# tussen het versturen van de credentials en het ontvangen van het 
# antwoord zit:
USER = '000000'

def test_logins(attempts):
    """
    Voer meerdere inlogpogingen uit en print per poging
    het antwoord van de server en de tijdsduur.

    Parameters
    ----------
        attempts -- lijst van tuples (username, password)
    """
    for username, password in attempts:
        reply, duration = call_server(username, password)
        print(f"Inlogpoging met gebruiker '{username}':")
        print(f"  Antwoord van server: {reply}")
        print(f"  Tijd tussen versturen en ontvangen: {duration:.6f} seconden\n")


# Voorbeeldgebruik:
login_attempts = [
    (USER, "wachtwoord1"),
    (USER, "wachtwoord2"),
    (USER, "hunter2")
]

test_logins(login_attempts)