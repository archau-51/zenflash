from sys import platform
from colorama import Fore
if platform == "darwin":
    print(
        Fore.RED
        + "Sorry, this script is not compatible with macOS, please try Windows or Linux instead."
        + Fore.RESET
    )
    raise SystemExit(1)
elif platform == "win32":
    from windows import main
    pass
elif platform == "linux" or platform == "linux2":
    pass
main()
