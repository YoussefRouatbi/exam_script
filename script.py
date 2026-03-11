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
}
print("Choose subject:")
for key, value in subjects.items():
    print(f"{key}. {value[0]}")
choice = int(input("Enter subject number: "))
year = input("Enter year (example 2025): ")
correct = input('With correction ? (y / n) : ')
subject_name, subject_slug = subjects[choice]
folder_path = f"{subject_name}/{year}"
os.makedirs(folder_path, exist_ok=True)

base_url = "http://bacweb.tn/bac"

exam_types = ["principale", "controle"]

for exam in exam_types:
    if correct.lower() == 'y':
        url = f"{base_url}/{year}/{exam}/informatique/{subject_slug}.pdf"
        file_path = f"{folder_path}/{exam}.pdf"
        url_c = f"{base_url}/{year}/{exam}/informatique/{subject_slug}_c.pdf"
        file_path_c = f"{folder_path}/{exam}_correction.pdf"
    else:    
        url = f"{base_url}/{year}/{exam}/informatique/{subject_slug}.pdf"
        file_path = f"{folder_path}/{exam}.pdf"

    try:
        response = requests.get(url)
        response_c = requests.get(url_c)
        if response.status_code == 200:
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"{exam} downloaded successfully.")
        else:
            print(f"{exam} not found (Status {response.status_code})")
            
        if response_c.status_code == 200:
            with open(file_path_c, "wb") as f:
                f.write(response_c.content)
            print(f"{exam} correction downloaded successfully.")
        else:
            print(f"{exam} correction not found (Status {response.status_code})")

    except Exception as e:
        print(f"Error downloading {exam}: {e}")

print("Done.")