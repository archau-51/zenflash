from sys import platform
from colorama import Fore
import subprocess

if platform == "darwin":
    print(
        Fore.RED
        + "Sorry, this script is not compatible with macOS, please try Windows or Linux instead."
        + Fore.RESET
    )
    raise SystemExit(1)
elif platform == "win32":
    from internal.windows import main

    pass
elif platform == "linux" or platform == "linux2":
    pass
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
with open('internal/codenames') as f:
    content = f.readlines()
    for line in content:
        if line == device + '\n':
            print(content[content.index(line) - 1])