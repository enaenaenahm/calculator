import threading
import webbrowser
import time
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

history = {'+': [], '-': [], '*': [], '/': []}

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Ошибка: деление на ноль"
        return num1 / num2
    else:
        return "Неизвестная операция"

def print_history():
    for op, ops in history.items():
        print(f"{op} {ops}")

def repl():
    while True:
        try:
            num1 = input("> ")
            if num1.lower() == 'exit':
                break
            num1 = float(num1)
            
            num2 = float(input("> "))
            operation = input("> ")
            
            result = calculate(num1, num2, operation)
            
            if isinstance(result, str):
                print(result)
            else:
                expression = f"{num1} {operation} {num2} = {result}"
                history[operation].append(expression)
                print(expression)
            
            print_history()
        except ValueError:
            print("Ошибка: введите число")
        except Exception as e:
            print(f"Ошибка: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def handle_calculate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'нет данных'}), 400

        num1 = data.get('num1')
        num2 = data.get('num2')
        operation = data.get('operation')

        if num1 is None or num2 is None or operation is None:
            return jsonify({'error': 'отсутствуют аргументы'}), 400

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            return jsonify({'error': 'некорректные числа'}), 400

        result = calculate(num1, num2, operation)

        if isinstance(result, str):
            return jsonify({'error': result}), 400

        expression = f"{num1} {operation} {num2} = {result}"
        history[operation].append(expression)

        return jsonify({'result': result, 'history': history})
    except Exception as e:
        return jsonify({'error': f'Ошибка: {str(e)}'}), 500

def open_browser():
    time.sleep(1)
    webbrowser.open("http://localhost:5000")

if __name__ == '__main__':
    threading.Thread(target=open_browser, daemon=True).start()
    app.run(debug=True, use_reloader=False)