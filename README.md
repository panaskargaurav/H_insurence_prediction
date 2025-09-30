# 🏥 Health Insurance Premium Predictor

A **Streamlit web app** that predicts health insurance premiums based on personal information such as age, BMI, number
of children, gender, and smoking habits.
It also includes a **BMI calculator** with health advice and floating animated emoji bubbles for a premium look.

---

## 🚀 Features

- Predicts health insurance premium based on user inputs.
- Provides **BMI category** and personalized advice.
- Gives **smoking-related health guidance**.
- Compact and visually appealing **glass card UI** with animated emoji bubbles.
- Tracks **total predictions made** during a session.
- Separate **BMI Calculator** tab for quick BMI computation.
- Responsive **mobile-friendly design**.
- Premium look with gradient background, glassy cards, and floating effects.

---

## 🛠 Installation

1. **Clone the repository**


git clone https://github.com/panaskargaurav/H_insurence_prediction
cd health-insurance-predictor
Create a virtual environment (optional but recommended)

## bash

python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
Install dependencies

# bash

pip install -r requirements.txt
Make sure you have streamlit and scikit-learn installed.

## 🖥 Usage
Run the Streamlit app:

bash

streamlit run app.py
Open the link displayed in your terminal (usually http://localhost:8501) in a web browser.

Premium Predictor Tab:

Enter Age, BMI, Children, Gender, and Smoking habits.

Click Predict Premium to see your predicted health insurance premium and BMI advice.

BMI Calculator Tab:

Enter Height, Weight, Age, and Gender.

Click Calculate BMI to see your BMI value and category.

📊 Example Output
Premium Predictor Result:

Predicted Premium: ₹ 4500

BMI Category: ✅ Normal

BMI Advice: 🎉 Keep up your lifestyle!

Smoking Advice: ✅ Great! Staying smoke-free helps long-term health.

BMI Calculator Result:

BMI: 23.4

Category: ✅ Normal

🎨 UI/UX
Gradient animated background.

Glassy emoji bubbles floating in different directions.

Card-style input and result layout.

Footer with detailed insurance benefits.

⚡ Notes
Minimum predicted premium is capped at ₹1000 to avoid unrealistic predictions.

Model predictions depend on the model.pkl file, ensure it is present in the repo.

All user sessions track the number of predictions made.

📂 File Structure

health-insurance-predictor/
│
├─ app.py           # Main Streamlit app
├─ model.pkl        # Trained model file
├─ requirements.txt # Python dependencies
└─ README.md        # Project description
📦 requirements.txt
Here’s a basic requirements.txt you can include:

nginx
Copy code
streamlit
scikit-learn
pandas
numpy
(Add any other libraries you used for training your model.pkl.)

 



