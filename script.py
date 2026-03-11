import os
import requests
import colorama

banner = """
╔══════════════════════════════════════════════╗
║            BAC EXAM DOWNLOADER               ║
║                                              ║
║        Download Bac Exams from BacWeb        ║
║        Subjects • Years • Corrections        ║
║                                              ║
║        Simple CLI Tool for Students          ║
║                                              ║
║            Created by Youssef Rouatbi        ║
╚══════════════════════════════════════════════╝
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
        print(f"{key}. {value[0]}")

    try:
        choice = int(input("Enter subject number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice not in subjects:
        print("Option not in list. Try again.")
        continue

    if choice == 0:
        print("Goodbye.")
        break

    subject_name, subject_slug = subjects[choice]

    while True:
        year = input("Enter year (2008 - 2025): ")
        if not year.isdigit():
            print("Year must be a number.")
            continue
        year = int(year)
        if year < 2008 or year > 2025:
            print("Year must be between 2008 and 2025.")
            continue
        break
    while True:
        correct = input("With correction? (y / n): ").lower()
        if correct not in ["y", "n"]:
            print("Please enter y or n.")
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
                print(f"{exam} downloaded successfully.")
            else:
                print(f"{exam} not found (Status {response.status_code})")
        except Exception as e:
            print(f"Error downloading {exam}: {e}")

        if correct == "y":
            url_c = f"{base_url}/{year}/{exam}/informatique/{subject_slug}_c.pdf"
            file_path_c = f"{folder_path}/{exam}_correction.pdf"
            try:
                response_c = requests.get(url_c)
                if response_c.status_code == 200:
                    with open(file_path_c, "wb") as f:
                        f.write(response_c.content)
                    print(f"{exam} correction downloaded successfully.")
                else:
                    print(f"{exam} correction not found (Status {response_c.status_code})")
            except Exception as e:
                print(f"Error downloading correction for {exam}: {e}")

    print("\nDownload finished.\n")