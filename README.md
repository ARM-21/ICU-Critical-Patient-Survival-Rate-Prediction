# ICU Critical Patient Survival Rate Prediction

A machine learning-powered clinical decision-support system that predicts in-hospital mortality risk for ICU patients using the SUPPORT2 dataset. This project combines advanced data science techniques with an interactive Streamlit web application, enabling healthcare professionals to assess patient survival probabilities based on demographic, clinical, and laboratory features.

---

## 📋 Project Overview

The ICU Critical Patient Survival Rate Prediction project is a comprehensive machine learning application designed to support clinical decision-making in intensive care units. The system analyzes patient data including demographics, diagnosis groups, vital signs, and laboratory results to predict mortality risk with probability-based risk categorization. The project includes a fully functional Streamlit web application for interactive predictions, comprehensive Jupyter notebooks for data analysis and model development, and detailed feature documentation for clinical interpretation.

The project demonstrates advanced data science practices including exploratory data analysis, feature engineering, model selection and evaluation, hyperparameter tuning, and production-ready model deployment. It serves as both an educational resource for machine learning in healthcare and a practical clinical decision-support tool.

**Important Disclaimer**: This project is for educational and research demonstration purposes. Predictions are not a substitute for clinical judgment and should be used only as a supplementary tool in clinical decision-making.

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Machine Learning** | scikit-learn, pandas, NumPy |
| **Data Analysis** | Jupyter Notebook, matplotlib, seaborn |
| **Web Framework** | Streamlit |
| **Data Processing** | Python 3.8+ |
| **Model Serialization** | pickle |
| **Dataset** | SUPPORT2 (Study to Understand Prognoses and Preferences for Outcomes and Risks of Treatment) |
| **Deployment** | Streamlit Cloud |
| **License** | MIT |

---

## ✨ Core Features

### Machine Learning Model

The project implements a sophisticated machine learning model trained on the SUPPORT2 dataset containing over 9,000 ICU patient records. The model combines multiple classification algorithms including K-Nearest Neighbors (KNN), Random Forest (RF), and Decision Trees (DT) to predict patient mortality risk. The ensemble approach leverages the strengths of different algorithms to provide robust predictions. The model is serialized using pickle for efficient production deployment and includes preprocessing components such as scalers and one-hot encoders.

### Interactive Streamlit Web Application

The Streamlit application provides an intuitive interface for clinical staff to input patient information and receive mortality risk predictions. The interface includes form inputs for patient demographics (age, gender), diagnosis group, vital signs (heart rate, blood pressure, respiratory rate, temperature), and laboratory results. The application displays predictions as probability percentages and categorizes risk into four levels: Low (0-25%), Moderate (25-50%), High (50-75%), and Critical (75-100%). Real-time feature importance analysis shows which patient characteristics most significantly influence the prediction.

### Comprehensive Data Analysis

The project includes detailed Jupyter notebooks documenting the complete data science workflow. The main implementation notebook covers data loading, exploratory data analysis, feature engineering, model training with multiple algorithms, hyperparameter tuning, and comprehensive model evaluation. The column visualization notebook provides in-depth analysis of individual features, their distributions, relationships with mortality outcomes, and clinical significance. Feature metadata documentation explains the meaning and clinical relevance of each input variable.

### Feature Engineering and Selection

The project demonstrates sophisticated feature engineering techniques including handling missing values, categorical encoding, numerical scaling, and feature selection. The analysis identifies the most predictive features for mortality risk, reducing model complexity while maintaining predictive accuracy. Feature importance analysis reveals which patient characteristics are most influential in determining survival outcomes.

### Model Performance Evaluation

Comprehensive model evaluation includes multiple performance metrics such as accuracy, precision, recall, F1-score, and ROC-AUC. The project includes cross-validation analysis to assess model generalization and prevent overfitting. Confusion matrices and classification reports provide detailed insights into model performance across different risk categories.

### Risk Stratification

The application categorizes predictions into clinically meaningful risk levels enabling healthcare professionals to prioritize patient care and resource allocation. The risk categories are based on mortality probability ranges derived from clinical thresholds and model performance characteristics.

### Production-Ready Deployment

The project is configured for easy deployment on Streamlit Cloud with all necessary dependencies specified in requirements.txt. The serialized model artifact (model.pkl) ensures consistent predictions across different deployment environments. Version management of dependencies ensures reproducibility and prevents compatibility issues.

---

## 📁 Project Structure

```
ICU-Critical-Patient-Survival-Rate-Prediction/
├── .devcontainer/                              # Development container configuration
│   ├── devcontainer.json                       # VS Code dev container settings
│   └── Dockerfile                              # Container image definition
├── app.py                                      # Streamlit web application
├── model.pkl                                   # Serialized trained ML model
├── support2-1.csv                              # SUPPORT2 dataset
├── Critical_Patient_Survival_Implementation.ipynb # Main implementation notebook
├── Column_Visualization.ipynb                  # Feature analysis notebook
├── Feature_Details.json                        # Feature metadata and descriptions
├── category_summary.csv                        # Category-level summary statistics
├── requirements.txt                            # Python dependencies
├── LICENSE                                     # MIT License
└── README.md                                   # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python** (version 3.8 or higher) - Download from [python.org](https://www.python.org/downloads/)
- **pip** (Python package manager, comes with Python)
- **Git** (for version control) - Download from [git-scm.com](https://git-scm.com/)
- **Virtual Environment** (recommended for dependency isolation)

### Installation Steps

**Step 1: Clone the Repository**

```bash
git clone https://github.com/ARM-21/ICU-Critical-Patient-Survival-Rate-Prediction.git
cd ICU-Critical-Patient-Survival-Rate-Prediction
```

**Step 2: Create and Activate Virtual Environment**

**On macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**On Windows (Command Prompt):**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**On Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
```

**Step 4: Run the Streamlit Application**

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

**Step 5: Verify Installation**

1. Navigate to the patient input form
2. Enter sample patient data
3. Click "Predict" to verify the model is working correctly
4. Review the predicted mortality risk and feature importance

---

## 📊 Dataset Overview

### SUPPORT2 Dataset

The project uses the SUPPORT2 (Study to Understand Prognoses and Preferences for Outcomes and Risks of Treatment) dataset, a comprehensive collection of ICU patient data from multiple medical centers. The dataset contains:

- **Records**: 9,105 ICU patient cases
- **Features**: 50+ clinical, demographic, and laboratory variables
- **Target**: In-hospital mortality outcome (binary classification)
- **Time Period**: Data collected over several years from multiple institutions

### Key Features

| Feature Category | Examples |
|-----------------|----------|
| Demographics | Age, Gender, Race |
| Clinical Diagnosis | Primary diagnosis group, secondary conditions |
| Vital Signs | Heart rate, Blood pressure, Respiratory rate, Temperature |
| Laboratory Results | Albumin, Creatinine, Glucose, Bilirubin, Urea nitrogen |
| Functional Status | APACHE score, SOFA score |
| Comorbidities | Diabetes, Hypertension, Congestive heart failure |

---

## 🤖 Model Architecture

### Algorithm Selection

The project implements and compares multiple machine learning algorithms:

**K-Nearest Neighbors (KNN)**
- Non-parametric algorithm that classifies based on nearest neighbors
- Effective for capturing local patterns in patient data
- Sensitive to feature scaling and dimensionality

**Random Forest (RF)**
- Ensemble method combining multiple decision trees
- Robust to overfitting and handles non-linear relationships
- Provides feature importance rankings

**Decision Trees (DT)**
- Interpretable algorithm that creates decision rules
- Useful for understanding clinical decision logic
- Prone to overfitting without pruning

### Model Pipeline

```
Raw Patient Input
    ↓
Data Validation & Preprocessing
    ↓
Categorical Encoding (One-Hot)
    ↓
Feature Scaling (StandardScaler)
    ↓
Feature Alignment to Training Features
    ↓
Model Prediction
    ↓
Risk Categorization
    ↓
Feature Importance Analysis
    ↓
Clinical Decision Support Output
```

### Feature Importance

The model identifies the most influential features for mortality prediction:

1. **Age**: Strong predictor of mortality risk
2. **APACHE Score**: Comprehensive severity assessment
3. **Albumin Level**: Nutritional and liver function indicator
4. **Creatinine**: Kidney function indicator
5. **Respiratory Rate**: Vital sign indicating respiratory distress

---

## 📈 Risk Categorization

The application categorizes mortality risk into four clinically meaningful levels:

| Risk Level | Probability Range | Clinical Interpretation | Recommended Action |
|-----------|------------------|----------------------|-------------------|
| **Low** | 0-25% | Patient likely to survive | Standard care protocol |
| **Moderate** | 25-50% | Moderate mortality risk | Enhanced monitoring |
| **High** | 50-75% | Significant mortality risk | Intensive intervention |
| **Critical** | 75-100% | Very high mortality risk | Maximum support measures |

---

## 🧪 Model Performance

### Evaluation Metrics

The model is evaluated using multiple performance metrics:

- **Accuracy**: Overall correctness of predictions
- **Precision**: Accuracy of positive predictions
- **Recall**: Ability to identify actual positive cases
- **F1-Score**: Harmonic mean of precision and recall
- **ROC-AUC**: Area under the receiver operating characteristic curve
- **Confusion Matrix**: Breakdown of prediction outcomes

### Cross-Validation

The model uses k-fold cross-validation to assess generalization performance and prevent overfitting. Cross-validation results provide confidence intervals for performance metrics.

---

## 🌐 Deployment

### Local Deployment

Run the application locally for development and testing:

```bash
streamlit run app.py
```

### Streamlit Cloud Deployment

Deploy to Streamlit Cloud for public access:

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Click "New app"
4. Select your GitHub repository and main file (app.py)
5. Deploy

### Deployment Requirements

For successful deployment, ensure:

- `app.py` is in the repository root
- `model.pkl` is in the repository root
- `requirements.txt` contains all dependencies
- scikit-learn version in requirements.txt matches the version used to create model.pkl
- All data files are committed to the repository

### Deployment Notes

- Keep model.pkl and requirements.txt synchronized
- If rebuilding the model, regenerate model.pkl before redeploying
- Monitor deployment logs for any runtime errors
- Test predictions after deployment to verify functionality

---

## 📚 Jupyter Notebooks

### Critical_Patient_Survival_Implementation.ipynb

The main implementation notebook containing:

- Data loading and initial exploration
- Missing value analysis and handling
- Feature engineering and selection
- Exploratory data analysis (EDA)
- Model training with multiple algorithms
- Hyperparameter tuning and optimization
- Model evaluation and comparison
- Feature importance analysis
- Model serialization to pickle format

### Column_Visualization.ipynb

Feature analysis notebook containing:

- Individual feature distributions
- Feature relationships with mortality outcome
- Categorical feature analysis
- Numerical feature statistics
- Correlation analysis
- Clinical significance interpretation
- Visualization of feature patterns

---

## 🔐 Data Privacy and Security

The project implements several privacy and security considerations:

- **Data Anonymization**: SUPPORT2 dataset uses de-identified patient data
- **Local Processing**: Predictions processed locally without external data transmission
- **Model Serialization**: Secure model storage using pickle format
- **No Data Storage**: Application does not store patient input data
- **HIPAA Considerations**: For clinical deployment, implement appropriate HIPAA compliance measures

---

## ⚠️ Clinical Considerations and Limitations

### Important Disclaimers

This project is for educational and research purposes. Key limitations include:

- **Not a Substitute for Clinical Judgment**: Predictions should supplement, not replace, clinical expertise
- **Historical Data**: Model trained on historical data may not reflect current clinical practices
- **Population Specificity**: Model trained on specific patient populations may not generalize to all ICU settings
- **Feature Limitations**: Predictions based only on provided features; clinical context is essential
- **Regulatory Compliance**: Clinical deployment requires appropriate regulatory approval and validation

### Clinical Validation

For clinical deployment, the model requires:

- Prospective validation in target clinical setting
- Comparison with existing clinical scoring systems
- Regulatory approval (FDA, CE marking, etc.)
- Clinical staff training and education
- Ongoing performance monitoring
- Ethical review and approval

---

## 🤝 Contributing

We welcome contributions from the community. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeatureName`)
3. Commit your changes (`git commit -m 'Add YourFeatureName'`)
4. Push to the branch (`git push origin feature/YourFeatureName`)
5. Open a Pull Request with a clear description of your changes

---

## 👨‍💻 Developer

**Manoj Neupane** - Project Lead & Data Science Implementation

---

## 📄 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software for educational and research purposes. See the [LICENSE](LICENSE) file for complete license terms.

**Copyright © 2026** Manoj Neupane

---

## 📞 Support & Contact

For questions, bug reports, or feature requests:

1. Open an issue on the GitHub repository
2. Contact the project maintainer directly
3. Check the project documentation for common questions

---

## 📚 Additional Resources

### Machine Learning and Healthcare

- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [SUPPORT2 Dataset Paper](https://www.ncbi.nlm.nih.gov/pubmed/10565802)

### Clinical Decision Support

- [Clinical Decision Support Systems Overview](https://en.wikipedia.org/wiki/Clinical_decision_support_system)
- [APACHE Score Information](https://en.wikipedia.org/wiki/APACHE_II)
- [SOFA Score Information](https://en.wikipedia.org/wiki/SOFA_score)

### Machine Learning Best Practices

- [Scikit-learn Model Evaluation Guide](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [Cross-Validation Techniques](https://scikit-learn.org/stable/modules/cross_validation.html)
- [Feature Engineering Best Practices](https://scikit-learn.org/stable/modules/preprocessing.html)

---

## 🎯 Future Enhancements

Planned features and improvements:

- **Deep Learning Models**: Neural network implementation for improved predictions
- **Ensemble Methods**: Advanced ensemble techniques combining multiple models
- **Real-time Data Integration**: Connection to hospital EHR systems
- **Explainability**: SHAP values and LIME for model interpretation
- **Mobile Application**: Mobile app for bedside predictions
- **Multi-hospital Validation**: Prospective validation across multiple institutions
- **Continuous Learning**: Model retraining with new patient data
- **Risk Stratification**: More granular risk categories
- **Comorbidity Analysis**: Detailed analysis of comorbidity impact
- **Temporal Analysis**: Time-series analysis of patient trajectory

---

## 📖 Citation

If you use this project in your research or work, please cite:

```bibtex
@software{neupane2026icu,
  author = {Neupane, Manoj},
  title = {ICU Critical Patient Survival Rate Prediction},
  year = {2026},
  url = {https://github.com/ARM-21/ICU-Critical-Patient-Survival-Rate-Prediction}
}
```

---

**Last Updated**: January 2026  
**Version**: 1.0.0  
**Status**: Active Development  
**Repository**: [GitHub - ARM-21/ICU-Critical-Patient-Survival-Rate-Prediction](https://github.com/ARM-21/ICU-Critical-Patient-Survival-Rate-Prediction)
