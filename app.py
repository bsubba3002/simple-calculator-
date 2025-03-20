from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__, template_folder="templates")
CORS(app)  # Enable CORS for frontend communication

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return jsonify({'error': 'Division by zero is not allowed'})
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation'})

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
