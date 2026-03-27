# Brute Force Attack Simulation Tool

## 1. Problem Statement
Many users are unaware of how brute force attacks can break weak passwords, making their accounts vulnerable to hacking. This project addresses the lack of ethical hacking awareness by demonstrating how automated scripts can guess passwords.

## 2. Project Objective
The goal of this application is to educate users on password security by simulating real-world attack scenarios (Brute Force and Dictionary Attacks) in a controlled web environment.

## 3. Solution Description
This is a web application built with **Flask (Python)** that demonstrates the difference between a systematic brute force generation and a wordlist-based dictionary attack. It helps users visualize the time and effort required to crack various password lengths and complexities.

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
   git clone https://github.com/priyaldev/Brute_Force_attack_simulator.git
2. Install dependencies:

   ```bash
   pip install Flask
   Run the application:
3. Run the application
   ```bash
   python app.py
 Open your browser and navigate to http://127.0.0.1:5000

  
## 7. Future Scope   

* Multi-threading: Implementation of concurrent processing to increase cracking speed.

* Complexity Analysis: Integration of a password entropy calculator to suggest stronger passwords.

* Account Lockout Simulation: Adding defensive features like CAPTCHA or rate-limiting to show how attacks can be prevented.


Author: Priyal Jain
   
