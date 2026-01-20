import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(
    page_title="ICU Mortality Risk Predictor",
    layout="centered"
)
# ===== Load Model =====
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model_artifact = load_model()
rf = model_artifact['model']
scaler = model_artifact['scaler']
feature_names = model_artifact['feature_names']
performance = model_artifact['performance']

# ===== Header =====
st.title(" ICU Patient Mortality Risk Predictor")
st.markdown("""
**Model Performance:** Accuracy {:.1f}% | AUC {:.3f}
""".format(performance['accuracy']*100, performance['auc']))
st.markdown("---")
# ===== Disease Category Mapping =====
DISEASE_GROUPS = {
    "Acute Respiratory Failure (ARF)": "ARF",
    "COPD/CHF/Cirrhosis": "COPD/CHF/Cirrhosis",
    "Coma": "Coma",
    "Colon Cancer": "Colon Cancer",
    "Lung Cancer": "Lung Cancer",
    "Multiple Organ System Failure (Malignancy)": "MOSF w/Malig",
    "Multiple Organ System Failure (Sepsis)": "MOSF w/Sepsis",
    "Other": "Other"
}
# ===== Input Form =====
with st.form("prediction_form"):
    st.subheader("Patient Information")
    
    # Section 1: Demographics
    st.markdown("**Demographics**")
    col1, col2 = st.columns(2)
    age = col1.number_input(
        "Age (years)", 
        min_value=18, max_value=120, value=65, 
        help="Patient age in years"
    )
    sex = col2.selectbox(
        "Gender", 
        ["Male", "Female"],
        help="Patient biological sex"
    )
    
    st.markdown("---")
    # Section 2: Disease Category
    st.markdown("**Primary Diagnosis**")
    dzgroup = st.selectbox(
        "Disease Category",
        list(DISEASE_GROUPS.keys()),
        help="Primary reason for ICU admission"
    )
    
    st.markdown("---")
    # Section 3: Severity Scores
    st.markdown("**Severity Scores** (Most Important Predictors)")
    col1, col2 = st.columns(2)
    sps = col1.number_input(
        "SUPPORT Score (SPS)",
        min_value=0.0, max_value=100.0, value=30.0, step=1.0,
        help="SUPPORT physiological score (higher = sicker)"
    )
    aps = col2.number_input(
        "APACHE Score (APS)",
        min_value=0.0, max_value=200.0, value=40.0, step=1.0,
        help="APACHE III physiological score (higher = sicker)"
    )
    st.markdown("---")
    
    # Section 4: Vital Signs
    st.markdown("**Vital Signs**")
    col1, col2 = st.columns(2)
    meanbp = col1.number_input(
        "Mean Blood Pressure (mmHg)",
        min_value=30.0, max_value=200.0, value=80.0, step=1.0,
        help="Mean arterial blood pressure"
    )
    hrt = col2.number_input(
        "Heart Rate (bpm)",
        min_value=30.0, max_value=220.0, value=90.0, step=1.0,
        help="Heart rate in beats per minute"
    )
    
    col1, col2 = st.columns(2)
    resp = col1.number_input(
        "Respiratory Rate (/min)",
        min_value=5.0, max_value=60.0, value=20.0, step=1.0,
        help="Breaths per minute"
    )
    temp = col2.number_input(
        "Temperature (°C)",
        min_value=32.0, max_value=42.0, value=37.0, step=0.1,
        help="Body temperature in Celsius"
    )
    
    st.markdown("---")
    # Section 5: Laboratory Values
    st.markdown("**Laboratory Values**")
    col1, col2 = st.columns(2)
    
    crea = col1.number_input(
        "Creatinine (mg/dL)",
        min_value=0.1, max_value=20.0, value=1.2, step=0.1,
        help="Serum creatinine - kidney function marker"
    )
    sodium = col2.number_input(
        "Sodium (mEq/L)",
        min_value=100.0, max_value=180.0, value=140.0, step=1.0,
        help="Serum sodium level"
    )
    
    col1, col2 = st.columns(2)
    ph = col1.number_input(
        "Blood pH",
        min_value=6.8, max_value=7.8, value=7.4, step=0.01,
        help="Blood pH level (7.35-7.45 is normal)"
    )
    pafi = col2.number_input(
        "PaO2/FiO2 Ratio",
        min_value=50.0, max_value=600.0, value=300.0, step=10.0,
        help="Oxygenation measure (>300 is normal, <200 indicates ARDS)"
    )
    
    col1, col2 = st.columns(2)
    alb = col1.number_input(
        "Albumin (g/dL)",
        min_value=1.0, max_value=6.0, value=3.5, step=0.1,
        help="Serum albumin - nutritional/liver status"
    )
    bili = col2.number_input(
        "Bilirubin (mg/dL)",
        min_value=0.1, max_value=30.0, value=1.0, step=0.1,
        help="Total bilirubin - liver function marker"
    )
    
    col1, col2 = st.columns(2)
    wblc = col1.number_input(
        "WBC Count (cells/μL)",
        min_value=0.1, max_value=100.0, value=10.0, step=0.5,
        help="White blood cell count (4-11 is normal)"
    )
    glucose = col2.number_input(
        "Glucose (mg/dL)",
        min_value=20.0, max_value=800.0, value=120.0, step=5.0,
        help="Blood glucose level"
    )
    
    st.markdown("---")
    # Section 6: Clinical Status
    st.markdown("**Clinical Status**")
    col1, col2 = st.columns(2)
    
    scoma = col1.number_input(
        "Coma Score",
        min_value=0.0, max_value=100.0, value=0.0, step=1.0,
        help="Glasgow coma scale score (0 = alert, higher = worse)"
    )
    adlsc = col2.number_input(
        "ADL Score",
        min_value=0.0, max_value=7.0, value=0.0, step=1.0,
        help="Activities of Daily Living impairment score"
    )
    
    hday = col1.number_input(
        "Hospital Day",
        min_value=0, max_value=365, value=1, step=1,
        help="Day of current hospitalization"
    )
    
    # Submit button
    st.markdown("---")
    submit = st.form_submit_button("🔮 Predict Mortality Risk", use_container_width=True)

# ===== Process Prediction =====
if submit:
    with st.spinner("Calculating risk..."):
        # Create input dataframe
        input_data = pd.DataFrame([{'sps': sps,'aps': aps,'age': age,'meanbp': meanbp,'hrt': hrt,'resp': resp,'temp': temp,'crea': crea,'sodium': sodium,
        'ph': ph,'pafi': pafi,'alb': alb,'bili': bili,'wblc': wblc,'glucose': glucose,
        'scoma': scoma,'adlsc': adlsc,'hday': hday,'dzgroup': DISEASE_GROUPS[dzgroup],'sex': sex.lower()
        }])
        
        # One-hot encode to match training
        input_encoded = pd.get_dummies(input_data, drop_first=False)
        # Align with training features
        input_aligned = input_encoded.reindex(columns=feature_names, fill_value=0)
        # Scale
        input_scaled = scaler.transform(input_aligned)
        # Predict
        risk_prob = rf.predict_proba(input_scaled)[0, 1]
        risk_class = rf.predict(input_scaled)[0]
    # ===== Display Results =====
    st.markdown("---")
    st.subheader("📊 Prediction Results")
    
    # Risk percentage with color coding
    risk_pct = risk_prob * 100
    
    if risk_pct < 20:
        color = "green"
        risk_level = "Low Risk"
    elif risk_pct < 50:
        color = "orange"
        risk_level = "Moderate Risk"
    elif risk_pct < 75:
        color = "red"
        risk_level = "High Risk"
    else:
        color = "darkred"
        risk_level = "Critical Risk"
    
    st.markdown(f"""
    <div style='background-color: {color}; padding: 20px; border-radius: 10px; text-align: center;'>
        <h1 style='color: white; margin: 0;'>{risk_pct:.1f}%</h1>
        <h3 style='color: white; margin: 5px 0 0 0;'>{risk_level}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    **Interpretation:**
    - Predicted in-hospital mortality risk: **{risk_pct:.1f}%**
    - Risk category: **{risk_level}**
    - Classification: **{'High Risk (Death Predicted)' if risk_class == 1 else 'Lower Risk (Survival Predicted)'}**
    """)

    
    # Key risk factors (feature contribution)
    with st.expander("View Key Risk Factors"):
        st.markdown("**Top factors influencing this prediction:**")
        
        # Get feature importance for display
        top_features = model_artifact['feature_importance'].head(10)
        st.dataframe(top_features, use_container_width=True)

