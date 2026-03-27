# Brute Force Attack Simulation Tool

## 1. Problem Statement
[cite_start]Many users are unaware of how brute force attacks can break weak passwords, making their accounts vulnerable to hacking[cite: 14]. [cite_start]This project addresses the lack of ethical hacking awareness by demonstrating how automated scripts can guess passwords[cite: 14].

## 2. Project Objective
[cite_start]The goal of this application is to educate users on password security by simulating real-world attack scenarios (Brute Force and Dictionary Attacks) in a controlled web environment[cite: 7, 14].

## 3. Solution Description
[cite_start]This is a web application built with **Flask (Python)** that demonstrates the difference between a systematic brute force generation and a wordlist-based dictionary attack[cite: 7]. [cite_start]It helps users visualize the time and effort required to crack various password lengths and complexities[cite: 37].

## 4. Features
* **Pure Brute Force Mode:** Systematically generates character combinations to find a match.
* **Dictionary Attack Mode:** Reads from a `passwords.txt` file to simulate attacks using common passwords.
* **Real-Time Analytics:** Displays the total number of attempts and the time taken for the crack to succeed.
* **Responsive UI:** A clean web dashboard built with Bootstrap for easy interaction.

## 5. Technology Stack
* [cite_start]**Backend:** Python (Flask) [cite: 51]
* **Frontend:** HTML5, CSS3, Bootstrap, JavaScript
* **Logic:** Itertools and Time modules

## 6. Setup and Installation
1. Clone this repository:
   ```bash
   git clone [Your-Repository-Link]

   
