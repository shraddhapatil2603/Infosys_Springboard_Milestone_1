# 🐾 Pawdentify — AI-Powered Dog Breed Identification System

**Pawdentify** is an AI-powered web application that identifies dog breeds from uploaded images using a trained **Convolutional Neural Network (CNN)**.  
It also provides detailed breed information such as temperament, origin, health issues, and care tips.

---

## 📁 Project Structure
pawdentify/
├── data/
│   └── breed_info.json
├── models/
│   ├── pawdentify_cnn.h5
│   └── class_indices.json
├── scripts/
│   ├── prepare_from_xls.py
│   ├── train_model.py
│   ├── classify_and_describe.py
│   └── fetch_breed_info.py
├── web_app/
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── uploads/
├── venv/
└── README.md

---

## 🚀 Features
- 🐶 Upload an image and identify the dog breed instantly.  
- 🎯 Displays breed confidence score.  
- 📘 Shows detailed breed info (origin, size, temperament, etc.).  
- 🧠 Uses a trained **TensorFlow/Keras CNN** model.  
- 💻 Built with **Flask**, responsive HTML, and CSS.  
- 🧾 Dynamic breed data using the Wikipedia API.

---

## 🧠 Technologies Used
- **Python 3.10+**
- **Flask**
- **TensorFlow / Keras**
- **Pandas, NumPy**
- **Pillow (PIL)**
- **Wikipedia API**

---

## ⚙️ Setup Instructions
1️⃣ Clone the Repository
    git clone https://github.com/yourusername/pawdentify.git
    cd pawdentify

2️⃣ Create and Activate Virtual Environment
Windows (CMD):
    python -m venv venv
    venv\\Scripts\\activate

macOS / Linux:
    python3 -m venv venv
    source venv/bin/activate

3️⃣ Install Dependencies
    pip install -r requirements.txt

4️⃣ Run the App
    python web_app/app.py

Then open: http://127.0.0.1:5000

---

## 📷 How It Works
1. Upload a dog image.
2. CNN predicts the breed and confidence.
3. Breed info is shown with full details.

---

## 🧩 Model Training (Optional)
To retrain your own CNN model:
    python scripts/train_model.py

---

## 💡 Future Enhancements
- User profiles & history.
- Vet consultation API.
- Dog match quiz.
- Cloud deployment.

---

## 🧑‍💻 Author
**Gaurav [Your Full Name]**  
AI & Data Science | ML Engineer | Full Stack Developer

---

## 📜 License
Licensed under the **MIT License**.

---

## 🧾 Requirements
Flask==3.0.3
tensorflow==2.16.1
pandas==2.2.2
numpy==1.26.4
Pillow==10.3.0
matplotlib==3.9.0
scipy==1.13.0
wikipedia-api==0.6.0
h5py==3.11.0
"""

file_path = "/mnt/data/README.md"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

file_path