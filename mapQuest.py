import urllib.parse

import requests

import colorama
from colorama import Fore, Back, Style
    #Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    #Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    #Style: DIM, NORMAL, BRIGHT, RESET_ALL
colorama.init(autoreset=True)
from pip._vendor import requests

 

main_api = "https://www.mapquestapi.com/directions/v2/route?"

key = "QAWzHgeqVXpkMAWzKGojDst5CNgXiAq1"

while True:

    orig = input("Starting Location: ")

    if orig == "quit" or orig == "q":

        break

    dest = input("Destination: ")

    if dest == "quit" or dest == "q":

        break

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

    json_data = requests.get(url).json()

    print("URL: " + (url))

    json_data = requests.get(url).json()

    json_status = json_data["info"]["statuscode"]

    if json_status == 0:

        print("API Status: " + str(json_status) + " = A successful route call.\n")

        print(Fore.RED+"=============================================")

        print(Fore.GREEN + Style.DIM + Back.WHITE +"Directions from " + (orig) + " to " + (dest))

        print(Fore.GREEN + Style.DIM + Back.WHITE +"Trip Duration:   " + (json_data["route"]["formattedTime"]))

        print(Fore.GREEN + Style.DIM + Back.WHITE +"Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))

        print(Fore.GREEN + Style.DIM + Back.WHITE +"Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))

        print(Fore.YELLOW +Style.DIM +"=============================================")

        for each in json_data["route"]["legs"][0]["maneuvers"]:

            print((Fore.BLUE + Style.DIM + Back.WHITE +each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))

        print(Fore.MAGENTA +Style.DIM +"=============================================\n")

    elif json_status == 402:

        print(Fore.WHITE +Style.DIM +Back.RED +"**********************************************")

        print(Fore.WHITE +Style.DIM +Back.RED +"Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")

        print(Fore.WHITE +Style.DIM +Back.RED +"**********************************************\n")

    elif json_status == 611:

        print(Fore.MAGENTA +Style.DIM +Back.RESET +"**********************************************")

        print(Fore.MAGENTA +Style.DIM +Back.RESET +"Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")

        print(Fore.MAGENTA +Style.DIM +Back.RESET +"**********************************************\n")

    else:

        print(Fore.WHITE +Style.DIM + Back.BLUE +"************************************************************************")

        print(Fore.WHITE +Style.DIM + Back.BLUE +"For Staus Code: " + str(json_status) + "; Refer to:")

        print(Fore.WHITE +Style.DIM + Back.BLUE +"https://developer.mapquest.com/documentation/directions-api/status-codes")

        print(Fore.WHITE +Style.DIM + Back.BLUE +"************************************************************************\n")