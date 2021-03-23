import scripts_vrt as s
import scripts_youtubedl as y
import netrc
from os import path, sep

nrcpath = path.expanduser('~' + sep + '.netrc')

print(nrcpath)

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
else :
    nrc = netrc.netrc()
    username = nrc.authenticators('vrtnu')[0]
    password = nrc.authenticators('vrtnu')[2]

s.search_input = input("\n-- Voer in welk programma of serie u wilt downloaden: \n--- ")
s.find_serie(s.search_input)

print("\n-- De series die overeenkomen met uw zoekopdracht zijn: ")
s.print_available_series()


s.chosen_serie = int(input("\n-- Kies het nummer dat overeenkomt met het gewenste programma of serie: \n--- "))
s.choose_serie(s.chosen_serie)

print("\n-- De aangeboden seizoenen van dit programma of serie zijn: ")
s.print_available_seasons()

s.chosen_season = input("\n-- Voer het nummer van het gewenste seizoen in: \n--- ")
s.choose_season(s.chosen_season)

y.download_serie()