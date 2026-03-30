# 🚀 AI-Powered Network Intrusion Detection System

A full-stack cybersecurity project that detects network intrusions using Machine Learning.  
Built with Flask, this system supports real-time predictions, bulk CSV analysis, and data visualization.

---

## ✨ Features

### 🔐 Intrusion Detection

- Classifies network traffic into:
  - Normal
  - DOS
  - PROBE
  - R2L
  - U2R

### 📊 Bulk CSV Analysis

- Upload CSV files for batch predictions
- Automatically processes multiple network records

### 📈 Visualization Dashboard

- Displays attack distribution using graphs
- Helps analyze traffic patterns quickly

### 🛡️ Robust Backend

- Handles invalid inputs safely
- Dynamic feature handling to prevent runtime errors

---

## 🖥️ Tech Stack

- **Frontend:** HTML, Tailwind CSS
- **Backend:** Flask (Python)
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib

---

## 📂 Project Structure

├── app.py
├── model.pkl
├── requirements.txt
├── templates/
│ ├── index.html
│ └── result.html
├── static/
│ └── chart.png
├── sample_input.csv

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/your-username/AI-Intrusion-Detection-System.git
cd AI-Intrusion-Detection-System

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```
