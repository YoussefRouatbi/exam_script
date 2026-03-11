import os
import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════╗
║            BAC EXAM DOWNLOADER               ║
║                                              ║
║        Download Bac Exams from BacWeb        ║
║        Subjects • Years • Corrections        ║
║                                              ║
║        Simple CLI Tool for Students          ║
║                                              ║
║            Created by Youssef Rouatbi        ║
╚══════════════════════════════════════════════╝{Style.RESET_ALL}
"""
print(banner)

subjects = {
    1: ("Mathématiques", "math"),
    2: ("Sciences physiques", "physique"),
    3: ("Anglais", "anglais"),
    4: ("Arabe", "arabe"),
    5: ("Français", "francais"),
    6: ("Philosophie", "philo"),
    7: ("Espagnol", "espagnol"),
    8: ("Algorithmes", "algorithme"),
    9: ("Bases de données", "base-de-donnees"),
    0: ("Exit", None)
}

base_url = "http://bacweb.tn/bac"

while True:
    print("\nChoose subject:")
    for key, value in subjects.items():
        print(f"{Fore.YELLOW}{key}. {value[0]}{Style.RESET_ALL}")

    try:
        choice = int(input(f"{Fore.YELLOW}Enter subject number: {Style.RESET_ALL}"))
    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")
        continue

    if choice not in subjects:
        print(f"{Fore.RED}Option not in list. Try again.{Style.RESET_ALL}")
        continue

    if choice == 0:
        print(f"{Fore.CYAN}Goodbye.{Style.RESET_ALL}")
        break

    subject_name, subject_slug = subjects[choice]

    while True:
        year = input(f"{Fore.YELLOW}Enter year (2008 - 2025): {Style.RESET_ALL}")
        if not year.isdigit():
            print(f"{Fore.RED}Year must be a number.{Style.RESET_ALL}")
            continue
        year = int(year)
        if year < 2008 or year > 2025:
            print(f"{Fore.RED}Year must be between 2008 and 2025.{Style.RESET_ALL}")
            continue
        break

    while True:
        correct = input(f"{Fore.YELLOW}With correction? (y / n): {Style.RESET_ALL}").lower()
        if correct not in ["y", "n"]:
            print(f"{Fore.RED}Please enter y or n.{Style.RESET_ALL}")
            continue
        break

    folder_path = f"{subject_name}/{year}"
    os.makedirs(folder_path, exist_ok=True)

    exam_types = ["principale", "controle"]

    for exam in exam_types:
        url = f"{base_url}/{year}/{exam}/informatique/{subject_slug}.pdf"
        file_path = f"{folder_path}/{exam}.pdf"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(file_path, "wb") as f:
                    f.write(response.content)
                print(f"{Fore.GREEN}{exam} downloaded successfully.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}{exam} not found (Status {response.status_code}){Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error downloading {exam}: {e}{Style.RESET_ALL}")

        if correct == "y":
            url_c = f"{base_url}/{year}/{exam}/informatique/{subject_slug}_c.pdf"
            file_path_c = f"{folder_path}/{exam}_correction.pdf"
            try:
                response_c = requests.get(url_c)
                if response_c.status_code == 200:
                    with open(file_path_c, "wb") as f:
                        f.write(response_c.content)
                    print(f"{Fore.GREEN}{exam} correction downloaded successfully.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}{exam} correction not found (Status {response_c.status_code}){Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Error downloading correction for {exam}: {e}{Style.RESET_ALL}")

    print(f"\n{Fore.CYAN}Download finished.\n{Style.RESET_ALL}")