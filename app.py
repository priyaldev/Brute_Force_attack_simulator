from flask import Flask, render_template, request, jsonify
import itertools
import string
import time
import os

app = Flask(__name__)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/crack', methods=['POST'])
def crack():
    data = request.get_json()
    target = data.get('password', '')
    mode = data.get('mode', 'brute')
    
    start_time = time.time()
    found = False
    attempts = 0

    if mode == 'brute':
       
        chars = string.ascii_lowercase + string.digits
        for length in range(1, 5): 
            if found: break
            for guess in itertools.product(chars, repeat=length):
                attempts += 1
                if ''.join(guess) == target:
                    found = True
                    break
    else:
        # using passwords.txt to simulate dictionary attack 
        file_path = "passwords.txt"
        
        if not os.path.exists(file_path):
            return jsonify({"status": "failed", "message": "passwords.txt file nahi mili!"})

        with open(file_path, "r") as f:
            for line in f:
                attempts += 1
                word = line.strip() # newline (\n) hatane ke liye
                if word == target:
                    found = True
                    break
    
    duration = time.time() - start_time
   
    
    if found:
        return jsonify({
            "status": "success",
            "message": f"Password cracked in {attempts} attempts!",
            "time": f"{duration:.4f} seconds"
        })
    else:
        return jsonify({
            "status": "failed",
            "message": "Password not found in this simulation range."
        })

if __name__ == '__main__':
    app.run(debug=True)

