import streamlit as st
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# --- Page config ---
st.set_page_config(page_title="Health Insurance Premium", page_icon="💼", layout="wide")

# --- CSS Styling ---
st.markdown("""
<style>
/* Background & gradient animation */
body, .stApp {
    background: linear-gradient(135deg, #e0d7f3, #d0c3f0);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    font-family: 'Segoe UI', sans-serif;
    color: #fff;
    overflow:hidden;
}
@keyframes gradientShift {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
}

/* Glassy Emoji Bubbles */
.emoji-bubble {
    position: absolute;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 24px;
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(5px);
    animation: floatEmoji linear infinite;
    z-index:0;
    opacity: 0;
}
.emoji-bubble:nth-child(1){left:5%; width:50px; height:50px; animation-duration:12s;}
.emoji-bubble:nth-child(2){left:20%; width:35px; height:35px; animation-duration:15s;}
.emoji-bubble:nth-child(3){left:40%; width:45px; height:45px; animation-duration:13s;}
.emoji-bubble:nth-child(4){left:60%; width:55px; height:55px; animation-duration:14s;}
.emoji-bubble:nth-child(5){left:80%; width:40px; height:40px; animation-duration:16s;}
.emoji-bubble:nth-child(6){left:15%; width:50px; height:50px; animation-duration:17s;}
.emoji-bubble:nth-child(7){left:35%; width:45px; height:45px; animation-duration:12s;}
.emoji-bubble:nth-child(8){left:70%; width:50px; height:50px; animation-duration:19s;}

@keyframes floatEmoji {
    0% { transform: translate(0,100vh) rotate(0deg) scale(0.5); opacity:0; }
    20% { opacity:1; }
    50% { transform: translate(20px,-50vh) rotate(180deg) scale(1); }
    100% { transform: translate(-20px,-100vh) rotate(360deg) scale(0.5); opacity:0; }
}

/* Card styling */
.card {
    background: rgba(25, 10, 60, 0.95);
    border-radius: 20px;
    padding: 20px 15px;
    box-shadow: 0 0 25px rgba(150, 130, 220, 0.5);
    border: 1px solid rgba(200, 180, 250,0.3);
    position: relative;
    z-index:1;
}

/* Header */
.header { text-align:center; font-size:34px; font-weight:bold; color:#5e3da1; margin-bottom:5px; }
.subtitle { text-align:center; font-size:16px; color:#fff; margin-bottom:20px; }

/* Inputs */
.stNumberInput input { border-radius:6px; padding:6px 8px; font-size:15px; background:#3a2f5c; color:#fff !important; border:1px solid #bfaaff; }
div.stNumberInput > label { color:#fff !important; font-size:14px; margin-bottom:3px; }

/* Result card */
.result {
    padding: 25px;
    border-radius: 16px;
    font-size: 18px;        
    font-weight: 500;
    text-align: left;       
    line-height: 1.7;       
    box-shadow: 0 0 18px #bfaaff;
    animation: fadeIn 0.8s ease-in-out;
    min-height: 200px;
    position: relative;
    z-index:1;
}
.result b { font-size: 20px; color: #f1eaff; }
.result .premium { font-size: 26px; font-weight: bold; color: #ffd700; }

/* Info card */
.info-card {
    background: rgba(58, 47, 92, 0.95);
    border-radius:16px;
    padding:20px;
    margin-top:15px;
    font-size:15px;         
    line-height:1.7;
    box-shadow:0 0 12px rgba(191, 170, 255,0.6);
    animation: fadeIn 1s ease-in-out;
}

/* BMI Card */
.bmi-card {
    background: rgba(58, 47, 92, 0.95);
    border-radius:16px;
    padding:20px;
    margin-top:15px;
    font-size:14px;
    box-shadow: 0 0 12px rgba(191, 170, 255,0.6);
}
.bmi-card h4 {
    text-align:center;
    color:#ffd700;
    margin-bottom:10px;
}
.bmi-result-box {
    text-align:center;
    margin-top:15px;
    padding:10px;
    border-radius:10px;
    background: rgba(45,37,69,0.9);
    font-weight:bold;
    font-size:16px;
    color:#ffd700;
    box-shadow: 0 0 10px rgba(191,170,255,0.4);
}

/* Footer */
.footer {
    background: rgba(25, 10, 60, 0.95);
    border-radius:15px;
    padding:25px;
    margin-top:30px;
    font-size:14px;
    line-height:1.6;
    box-shadow:0 0 20px rgba(191,170,255,0.5);
}
.footer h3 { color:#ffd700; margin-bottom:10px; }
.footer ul { margin-left:20px; }
.footer img { width:100%; max-width:600px; border-radius:10px; margin-top:10px; }

/* Button */
.stButton>button { background-color:#5e3da1; color:#fff; padding:8px 12px; font-size:14px; border-radius:8px; border:none; width:100%; transition:0.3s; }
.stButton>button:hover { background-color:#7a5fc1; }

@keyframes fadeIn { from {opacity:0; transform: translateY(10px);} to {opacity:1; transform: translateY(0);} }
</style>
""", unsafe_allow_html=True)

# --- Floating Glassy Emoji Bubbles ---
st.markdown("""
<div class="emoji-bubble">🩺</div>
<div class="emoji-bubble">💊</div>
<div class="emoji-bubble">🏥</div>
<div class="emoji-bubble">❤️</div>
<div class="emoji-bubble">🩹</div>
<div class="emoji-bubble">🧬</div>
<div class="emoji-bubble">🥼</div>
<div class="emoji-bubble">🦠</div>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="header">🏥 Health Insurance Premium Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Compact form for instant results</div>', unsafe_allow_html=True)

# --- Helper Functions ---
def bmi_category_advice(bmi):
    if bmi < 18.5:
        return "🔹 Underweight", "⚠️ Improve diet with balanced nutrition.", "#3498db"
    elif 18.5 <= bmi < 24.9:
        return "✅ Normal", "🎉 Keep up your lifestyle!", "#2ecc71"
    elif 25 <= bmi < 29.9:
        return "🟠 Overweight", "⚠️ Exercise & mindful eating recommended.", "#f39c12"
    else:
        return "🔴 Obese", "⚠️ Consult healthcare for weight management.", "#e74c3c"

def smoking_advice(smoker):
    return "🚭 Smoking increases risk of cancer, heart & lung diseases. Consider quitting!" if smoker.lower()=="yes" else "✅ Great! Staying smoke-free helps long-term health."

# --- Prediction Counter ---
if 'prediction_count' not in st.session_state:
    st.session_state['prediction_count'] = 0

# --- Tabs ---
tab1, tab2 = st.tabs(["💼 Premium Predictor", "📐 BMI Calculator"])

# --- Premium Predictor Tab ---
with tab1:
    col_form, col_result = st.columns([1,1])

    with col_form:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        # Main Inputs
        c1, c2 = st.columns(2)
        with c1:
            age = st.number_input('🧑 Age', min_value=1, max_value=120, step=1)
        with c2:
            bmi = st.number_input('⚖️ BMI', min_value=10.0, max_value=60.0, step=0.1)

        children = st.number_input('👶 Children', min_value=0, max_value=10, step=1)

        col_gen, col_smoke = st.columns(2)
        with col_gen:
            gender = st.radio('⚧ Gender:', ('Male', 'Female'))
        with col_smoke:
            smoker = st.radio('🚬 Do You Smoke?:', ('No', 'Yes'))

        predict_clicked = st.button('💡 Predict Premium', use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_result:
        result_placeholder = st.empty()
        counter_placeholder = st.empty()

    # --- Prediction & Display ---
    if predict_clicked:
        st.session_state['prediction_count'] += 1
        
        gender_val = 0 if gender.upper() == 'MALE' else 1
        smoker_val = 0 if smoker.upper() == 'NO' else 1
        X_test = [[age, bmi, children, gender_val, smoker_val]]

        # Predict premium and ensure minimum value of 2000
        predicted_value = model.predict(X_test)[0]
        if predicted_value < 1000:
            predicted_value = 1000
        yp = str(round(predicted_value, 2))

        category, bmi_advice_text, color = bmi_category_advice(bmi)
        smoke_msg = smoking_advice(smoker)

        result_placeholder.markdown(f"""
        <div class="result" style="border:2px solid {color}; box-shadow:0 0 18px {color}; background: rgba(58, 47, 92, 0.95);">
            💰 <b>Predicted Premium:</b> <span class="premium">₹ {yp}</span><br>
            📊 <b>BMI Category:</b> {category}<br>
            🩺 <b>BMI Advice:</b> {bmi_advice_text}<br>
            🚬 <b>Smoking Advice:</b> {smoke_msg}
        </div>
        """, unsafe_allow_html=True)

        counter_placeholder.markdown(f"""
        <div style="text-align:center; margin-top:20px; font-size:18px; font-weight:bold; color:white;">
            🔢 Total Predictions Made: {st.session_state['prediction_count']}
        </div>
        """, unsafe_allow_html=True)

# --- BMI Calculator Tab ---
with tab2:
    st.markdown('<div class="bmi-card">', unsafe_allow_html=True)
    st.markdown("<h4>📐 BMI Calculator</h4>", unsafe_allow_html=True)

    cc1, cc2 = st.columns(2)
    with cc1:
        calc_height = st.number_input("📏 Height (cm)", min_value=50.0, max_value=250.0, step=0.5, key="calc_h_tab")
        calc_age = st.number_input("🎂 Age (years)", min_value=1, max_value=120, step=1, key="calc_age_tab")
    with cc2:
        calc_weight = st.number_input("⚖️ Weight (kg)", min_value=10.0, max_value=300.0, step=0.5, key="calc_w_tab")
        calc_gender = st.radio("⚧ Gender", ["Male","Female"], key="calc_gen_tab")

    if st.button("📊 Calculate BMI", use_container_width=True, key="calc_bmi_btn_tab"):
        if calc_height > 0:
            bmi_val = round(calc_weight / ((calc_height/100)**2), 2)
            if bmi_val < 18.5:
                category = "🔹 Underweight"
            elif 18.5 <= bmi_val < 24.9:
                category = "✅ Normal"
            elif 25 <= bmi_val < 29.9:
                category = "🟠 Overweight"
            else:
                category = "🔴 Obese"

            st.markdown(f'<div class="bmi-result-box">Your BMI: {bmi_val} <br>Category: {category}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div class="footer">
<h3>Top reasons to buy Elevate health insurance</h3>
<ul>
<li>Hospitalisation & day care treatment cover</li>
<li>Unlimited reset of sum insured</li>
<li>Cashless EverywhereQ (cashless treatment at any hospital in India)</li>
<li>Up to 30% discount on renewals for staying active</li>
<li>100% sum insured increase every yearY, irrespective of claims</li>
<li>Unlimited coverage for any 1 claim of your choice during policy lifetimeY</li>
<li>AYUSH treatment covered up to sum insured</li>
<li>Pre & post hospitalisation expenses from 90 days until 180 days</li>
<li>Road & air ambulanceY covered up to sum insured</li>
<li>Customisable waiting periodsY</li>
<li>Cashless OPD services like ordering medicines, booking lab tests, etc. (with additional premium)</li>
<li>Cashless hospitalisation worldwideGY</li>
</ul>
</div>
""", unsafe_allow_html=True)
