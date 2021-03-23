import scripts_vrt as s
import scripts_youtubedl as y
import scripts_auth as a

a.auth()

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