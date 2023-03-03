from argparse import *
import requests
import time
from colorama import *
from infos import *




parser = ArgumentParser()
parser.add_argument("-u", "--url")

args = parser.parse_args()


start = time.time()



print("""
                 _     _               
                | |   | |              
  __ _ _ __ __ _| |__ | |__   ___ _ __ 
 / _` | '__/ _` | '_ \| '_ \ / _ \ '__|
| (_| | | | (_| | |_) | |_) |  __/ |   
 \__, |_|  \__,_|_.__/|_.__/ \___|_|   
  __/ |                                
 |___/                                 

""")
      


print("")
print("Copyright by cracknclose")
print("Don't use without permission. Or do if you want, I don't care.")
print("")



def getStat(url):
    status = requests.get(url)

    if status.ok:
        print("[*] Website " + Fore.GREEN + "online" + Fore.RESET)

        collectInfo.is_registered(args.url)
        collectInfo.getInfo(args.url)
    else:
        print("[!] Website" + Fore.RED + " offline " + Fore.RESET)


getStat(args.url)

endt = time.time() - start

print("")
print("")
print("Finished in " + str(endt) + " seconds.")