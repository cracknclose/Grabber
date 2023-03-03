import whois
from colorama import *


class collectInfo:
    def is_registered(url):
        w = whois.whois(url)
        print(Fore.GREEN + "[+] is registered" + Fore.RESET)

    def getInfo(url):
        w = whois.whois(url)

        print("[+] Domain registrar: " + str(w.registrar))
        print("[+] Server: " + str(w.whois_server))
        print("[+] Status: " + str(w.status))
        print("[+] Creation date: " + str(w.creation_date))
        print("[+] Expiration date: " + str(w.expiration_date))
        print("[+] Organisation: " + str(w.org))
        print("[+] Emails: " + str(w.emails))
        print("[+] Country: " + str(w.country))
        print("[+] City: " + str(w.city))
        print("[+] Postal code: " + str(w.registrant_postal_code))
        print("[+] Address: " + str(w.address))

        #print(w)