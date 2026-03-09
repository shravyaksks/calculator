from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)

DATA_FILE = "data/calculations.json"

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        op = request.form["op"]

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b if b != 0 else "Error: Division by zero"

        # Save calculation to JSON file
        entry = {"a": a, "b": b, "op": op, "result": result}
        with open(DATA_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")

    return render_template("cal_index.html", result=result)

@app.route("/history")
def history():
    calculations = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                calculations.append(json.loads(line.strip()))
    return render_template("history.html", calculations=calculations)

if __name__ == "__main__":
    app.run(debug=True)
