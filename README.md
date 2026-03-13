# ICU-Critical-Patient-Survival-Rate-Prediction

This project predicts ICU patient mortality risk using the SUPPORT2 dataset. It includes a deployable Streamlit web app, notebooks for analysis, and supporting metadata files used during model development and interpretation.

**Project objective**

- Estimate in-hospital mortality risk from patient demographics, diagnosis group, vital signs, and laboratory features.
- Provide an interactive clinical decision-support demo through a web interface.
- Document feature analysis and modeling decisions in notebooks.

**What is implemented**

- A trained machine-learning artifact loaded by `app.py` from `model.pkl`.
- Interactive patient-form input and risk prediction in Streamlit.
- Probability-based risk categories: Low, Moderate, High, and Critical.
- Display of model performance metrics and top feature-importance values.

**Folder contents (this `coursework` folder)**

- `app.py`: Streamlit application entrypoint.
- `model.pkl`: serialized model artifact used at runtime.
- `support2-1.csv`: primary dataset for ICU prediction experiments.
- `Critical_Patient_Survival_Implementation.ipynb`: main end-to-end notebook for data preparation, training, and evaluation.
- `Column_Visualization.ipynb`: feature and column-level visual analysis notebook.
- `Feature_Details.json`: feature metadata and mappings used during analysis.
- `category_summary.csv`: summarized category-level output used for interpretation.
- `requirements.txt`: Python dependencies for local run and Streamlit deployment.
- `LICENSE`: MIT license text.
- `README.md`: project documentation.

**Model and prediction workflow**

1. User enters patient values in the app form.
2. Inputs are converted to a single-row dataframe.
3. Categorical fields are one-hot encoded and aligned to training feature columns.
4. Scaler from `model.pkl` transforms the aligned input.
5. Classifier from `model.pkl` outputs mortality probability and class.
6. App shows risk percentage, risk level, and top feature-importance table.

**How to run locally**

1. Open terminal in `coursework/`.
2. Create and activate a virtual environment.
3. Install dependencies.
4. Run Streamlit.

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
streamlit run app.py
```

For PowerShell activation on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

**Deployment notes (Streamlit Cloud)**

- Set app file to `app.py`.
- Ensure deployment root contains `app.py`, `model.pkl`, and `requirements.txt`.
- Keep `scikit-learn` version in `requirements.txt` aligned with the version used to create `model.pkl`.
- If you rebuild the model, regenerate `model.pkl` and commit it before redeploying.

**Data and usage disclaimer**

This project is for educational and research demonstration purposes. Predictions are not a substitute for clinical judgment.

**License**

Licensed under MIT. See `LICENSE`.