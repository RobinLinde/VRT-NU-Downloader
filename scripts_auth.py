import netrc
from os import path, sep

def auth():
    nrcpath=path.expanduser('~' + sep + '.netrc')

    if not path.exists(nrcpath):
        username = input("\n-- Voer uw gebruikersnaam in: \n--- ")
        password = input("\n-- Voer uw wachtwoord in: \n--- ")

        f = open(nrcpath, 'x')
        f.write("machine vrtnu\nlogin "+ username + "\npassword "+ password)
        f.close()
    elif not netrc.netrc().authenticators('vrtnu'):
        username = input("\n-- Voer uw gebruikersnaam in: \n--- ")
        password = input("\n-- Voer uw wachtwoord in: \n--- ")

        f = open(nrcpath, 'a')
        f.write("\nmachine vrtnu\nlogin "+ username + "\npassword "+ password)
        f.close()
