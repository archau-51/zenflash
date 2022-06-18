import subprocess
import requests
import zipfile
import os
from colorama import Fore


def main():
    if os.path.isdir("./platform-tools") == False:
        try:
            subprocess.run(["adb"])
        except:
            print(
                Fore.YELLOW
                + "looks like you don't have android SDK platform tools on your system"
                + Fore.RESET
            )
            while True:
                down = input(
                    "Would you like to install it? ("
                    + Fore.GREEN
                    + "y"
                    + Fore.RESET
                    + "/"
                    + Fore.RED
                    + "n"
                    + Fore.RESET
                    + "): "
                )
                if down == "y" or down == "n":
                    break
                else:
                    print(Fore.RED + "Not a valid answer" + Fore.RESET)
            if down == "n":
                print(
                    Fore.YELLOW
                    + "You can manually download the Android SDK platform tools at "
                    + Fore.GREEN
                    + "https://developer.android.com/studio/releases/platform-tools"
                    + Fore.RESET
                )
                raise SystemExit
            else:
                print(
                    Fore.GREEN + "Downloading platform-tools-windows.zip" + Fore.RESET
                )
                try:
                    file = requests.get(
                        "https://dl.google.com/android/repository/platform-tools-latest-windows.zip"
                    )
                except:
                    print(Fore.RED + "Looks like you are not connected to the internet." + Fore.RESET)
                    raise SystemExit(1)
                open("platform-tools-windows.zip", "wb").write(file.content)
                with zipfile.ZipFile("./platform-tools-windows.zip", "r") as zip_ref:
                    zip_ref.extractall(".")
                os.remove("platform-tools-windows.zip")
                app_path = os.path.join("./", "platform-tools")
                os.environ["PATH"] += os.pathsep + app_path
                print(Fore.GREEN + 'Done!' + Fore.RESET)
    else:
        app_path = os.path.join("./", "platform-tools")
        os.environ["PATH"] += os.pathsep + app_path