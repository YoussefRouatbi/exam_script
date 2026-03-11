# Bac Exam Downloader

**BAC_EXAM_DOWNLOADER**
Created by **Youssef Rouatbi**

A **Python CLI tool** that allows students to quickly download **Tunisian Bac exam papers** directly from **BacWeb**. Select the **subject**, **year**, and whether you want the **correction**, and the script will automatically download the available exam PDFs. Designed to be **simple, fast, and student-friendly**.

---

## 🔹 Features

* Download **Bac exams by subject and year**
* Option to download **with or without corrections**
* Automatically downloads both:

  * **Session principale**
  * **Session contrôle**
* Organizes downloads into **folders by subject and year**
* Easy **command-line interface**
* Works directly from the terminal without GUI

---

## ⚙️ Requirements

* Python **3.8+**
* `pip` package manager

Python packages used:

* `requests` – for HTTP downloads
* `colorama` – for terminal colors (optional banner styling)

---

## 🚀 Installation

1. **Clone the repository**

```bash
git clone https://github.com/youssefrouatbi/exam_script.git
```

2. **Go into the project folder**

```bash
cd exam_script
```

3. **Install dependencies**

```bash
pip install requests colorama
```

---

## 💻 Usage

Run the script in your terminal:

```bash
python script.py
```

You will see a CLI interface with a banner and prompts:

```
╔══════════════════════════════════════════════╗
║            BAC EXAM DOWNLOADER               ║
║        Download Bac Exams from BacWeb        ║
║        Subjects • Years • Corrections        ║
║        Simple CLI Tool for Students          ║
║            Created by Youssef Rouatbi        ║
╚══════════════════════════════════════════════╝
```

### Step 1: Choose the subject

```
Choose subject:
1. Mathématiques
2. Sciences physiques
3. Anglais
4. Arabe
5. Français
6. Philosophie
7. Espagnol
8. Algorithmes
9. Bases de données
```

### Step 2: Enter the year

```
Enter year (example 2025): 2023
```

### Step 3: Choose if you want corrections

```
With correction ? (y / n): y
```

---

## 📂 Download Structure

The script automatically creates folders like this:

```
Algorithmes/
   └── 2023/
        ├── principale.pdf
        ├── principale_correction.pdf
        ├── controle.pdf
        └── controle_correction.pdf
```

All exams are organized **by subject and year**.

---

## ✅ Example Output

```
principale downloaded successfully.
principale correction downloaded successfully.
controle downloaded successfully.
controle correction downloaded successfully.
Done.
```

---

## ⚠️ Notes

* Exams are downloaded from **[http://bacweb.tn](http://bacweb.tn)**
* Some years or subjects may not exist on the server
* Missing files are skipped automatically

---

## Author

**Youssef Rouatbi**
Student in **Bac Informatique**
