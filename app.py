from flask import Flask, jsonify, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('front.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    if request.method == 'POST':
        try:
            # Replace 'python_script.py' with the actual path to your Python script
            result = subprocess.run(['python', 'cv.py'], capture_output=True, text=True)
            return jsonify({'message': result.stdout})
        except Exception as e:
            return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
