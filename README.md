```markdown
# 🧮 Flask Calculator

A simple web-based calculator built with **Flask**, featuring a clean UI, calculation history, and persistent storage.

---

## 📂 Project Structure
```
calculator/
│
├── cal_app.py              # Main Flask application
├── data/
│   └── calculations.json   # Stores past calculations
├── static/
│   └── style.css           # Styling for the app
├── templates/
│   ├── cal_index.html      # Calculator interface
│   └── history.html        # History page
```

---

## 🚀 Features
- Perform basic arithmetic operations: **Addition, Subtraction, Multiplication, Division**
- User-friendly interface with responsive design
- Stores calculation history in JSON format
- View past calculations in a styled table
- Clean separation of logic, templates, and static assets

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/shravyaksks/calculator.git
   cd calculator
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install flask
   ```

4. **Run the application**
   ```bash
   python cal_app.py
   ```

5. Open your browser and visit:
   ```
   http://127.0.0.1:5000
   ```

---

## 📸 Screenshots
- **Calculator Page**: Enter numbers, choose operation, and calculate.
- **History Page**: View all past calculations neatly formatted.

---

## 🛠️ Tech Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS (with Jinja2 templating)
- **Data Storage**: JSON file

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License
This project is licensed under the MIT License.
```

---

👉 Save this as `README.md` in your project root, commit, and push:

```bash
git add README.md
git commit -m "Add README.md with project details"
git push
```
