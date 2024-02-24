import os
import subprocess
from colorama import init, Fore

# Inicializáljuk a colorama-t
init()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header():
    print(Fore.RED + """
     ___               ___________            __
    |   | ____  ____   \__    ___/___   ____ |  |
    |   |/ ___\/ __ \    |    | /  _ \ /  _ \|  |
    |   \  \__\  ___/    |    |(  <_> |  <_> )  |__
    |___|\___  >___  >   |____| \____/ \____/|____/
             \/    \/
    v1.5
    creator:Adam>:D
    A wonderful software with which you can hack any network and more :D
    (1) Export Wi-Fi Profiles
    (2) List Wi-Fi Connections
    (3) Exit
    (4) Update
    (5) Help
    """ + Fore.RESET)

def export_wifi_profiles():
    try:
        os.makedirs("wifiprofile", exist_ok=True)
        output = subprocess.check_output(["ls", "/etc/NetworkManager/system-connections"], text=True)
        for line in output.splitlines():
            connection_name = line.strip()
            export_path = os.path.join("wifiprofile", f"{connection_name}.txt")
            subprocess.run(["sudo", "cp", f"/etc/NetworkManager/system-connections/{connection_name}", export_path])
        print(Fore.GREEN + "Wi-Fi profiles exported successfully." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Error exporting Wi-Fi profiles: {e}" + Fore.RESET)

def list_wifi_connections():
    try:
        output = subprocess.check_output(["nmcli", "connection", "show", "--active"], text=True)
        print(output)
    except subprocess.CalledProcessError:
        print(Fore.RED + "Error: Failed to list Wi-Fi connections." + Fore.RESET)

def update_system():
    try:
        os.system("sudo apt update")
        print(Fore.GREEN + "System update completed successfully." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Error updating system: {e}" + Fore.RESET)

def help_menu():
    print("""
    (1) Export Wi-Fi Profiles: Exports Wi-Fi profiles.
    (2) List Wi-Fi Connections: Lists active Wi-Fi connections.
    (3) Exit: Exits the program.
    (4) Update: Updates the system using 'sudo apt update'.
    (5) Help: Displays this help menu.
    """ + Fore.RED)

def main():
    clear_terminal()
    show_header()
    while True:
        input_str = input(Fore.RED + "Choose: " + Fore.RESET)

        if input_str == "1":
            export_wifi_profiles()
        elif input_str == "2":
            list_wifi_connections()
        elif input_str == "3":
            print(Fore.RED + "Exiting program." + Fore.RESET)
            break
        elif input_str == "4":
            update_system()
        elif input_str == "5":
            help_menu()
        else:
            print(Fore.RED + "Invalid choice" + Fore.RESET)

if __name__ == "__main__":
    main()
