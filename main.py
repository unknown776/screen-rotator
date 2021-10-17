import rotatescreen
from time import sleep
import colorama
from colorama import Style, Fore
colorama.init(autoreset=True)

inp = int(input("Choose a number from 1 to 25:\n"))

if inp < 26:
    print(f"{Fore.RED}{Style.BRIGHT}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>WARNING<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\nPlease don't stop the program between the execution. If anything happens then Aariz will not be responsible for this. So, please don't press ctrl+c or any other key.")
    input("Press ENTER to start")
    screen = rotatescreen.get_primary_display()
    for i in range(inp):
        screen.rotate_to(i*90 % 360)
        sleep(1.5)
    screen.rotate_to(0)

else:
    print(Fore.RED+"Please choose a number between " + Fore.CYAN+ Style.BRIGHT + "10 to 25")
    sleep(1.5)
