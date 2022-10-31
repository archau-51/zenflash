from sys import platform
from colorama import Fore
import subprocess
import requests
from bs4 import BeautifulSoup
try:
    f = open("./internal/ag_conf", 'r')
    if f.read() != "This file expresses agreement to the terms of this software throughout all excecutions":
        raise SystemError()()
    f.close()
except:
    print(
    Fore.RED
    + """

 _  _  _____                _    _                _  _ 
| || |/  __ \              | |  (_)              | || |
| || || /  \/  __ _  _   _ | |_  _   ___   _ __  | || |
| || || |     / _` || | | || __|| | / _ \ | '_ \ | || |
|_||_|| \__/\| (_| || |_| || |_ | || (_) || | | ||_||_|
(_)(_) \____/ \__,_| \__,_| \__||_| \___/ |_| |_|(_)(_)
                                                       
                                                       

"""
    + Fore.RESET
)
    print(
    Fore.YELLOW
    + "I am not responsible for whatever happens to your device, throughout all executions of this software"
)
    print(
    "By proceeding, you agree that any damage to your device is your and solely your responsibilty"
    + Fore.RESET
)
    if input(Fore.RED + 'To proceed, type "I AGREE": ' + Fore.YELLOW) != "I AGREE":
        print(Fore.CYAN + "Okay, exiting" + Fore.RESET)
        raise SystemExit
    else:
        f = open("./internal/ag_conf", "w")
        f.write("This file expresses agreement to the terms of this software throughout all excecutions")
        f.close()
print(Fore.RESET)
# check platform
if platform == "darwin":
    print(
        Fore.RED
        + "This script has not been tested on OSX, add an issue on github if something goes wrong"
        + Fore.RESET
    )
elif platform == "win32":
    from internal.windows import main

    pass
elif platform == "linux" or platform == "linux2":
    from internal.linux import main
else:
    print(Fore.CYAN + "I have no clue what OS you are running, but it is definetly not supported \n add an issue on github if you think that support should be added or if there is a problem."+ Fore.RESET)
    raise SystemError()
main()
if (
    subprocess.run(["adb", "devices", "-l"], capture_output=True)
    .stdout.splitlines()[1]
    .decode("utf-8")
    == ""
):
    print(Fore.YELLOW + "Connect your device" + Fore.RESET)
    while True:
        if (
            subprocess.run(["adb", "devices", "-l"], capture_output=True)
            .stdout.splitlines()[1]
            .decode("utf-8")
            == ""
        ):
            continue
        else:
            break
print(Fore.GREEN + "Device found!" + Fore.RESET)
if (
    subprocess.run(["adb", "devices", "-l"], capture_output=True)
    .stdout.splitlines()[1]
    .decode("utf-8")
    .split()[1]
    == "unauthorized"
):
    print(
        Fore.YELLOW
        + "Looks Like you have not authorized usb debugging from this computer on the device yet. \nIf a prompt appeared on yor device, tap allow. \nIf not, check the specific instructions for your device."
        + Fore.RESET
    )
    while True:
        if (
            subprocess.run(["adb", "devices", "-l"], capture_output=True)
            .stdout.splitlines()[1]
            .decode("utf-8")
            .split()[1]
            == "unauthorized"
        ):
            continue
        else:
            break
print(Fore.GREEN + "This computer is authorized!" + Fore.RESET)
device1 = list(
    subprocess.run(["adb", "devices", "-l"], capture_output=True)
    .stdout.splitlines()[1]
    .decode("utf-8")
    .split()[4]
)
device = device1.copy()
for char in device1:
    device.pop(0)
    if char == ":":
        break
device = "".join(device)
print(device)
with open("internal/codenames") as f:
    content = f.readlines()
    for line in content:
        if line == device + "\n":
            print(content[content.index(line) - 1])


def url_ok(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError as e:
        return e


twrp = url_ok("https://dl.twrp.me/" + device + "/")
if twrp != True and twrp != False:
    print(Fore.YELLOW + "Looks like you are not connected to the internet, Skipping recovery availability check" + Fore.RESET)
else:
    page = requests.get("https://orangefox.download/device/" + device + "/")
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="nf-img")
    # wrote this like 3 months ago or something, no idea how it works
    try:
        if results.prettify:
            of = False
    except:
        of = True
    
