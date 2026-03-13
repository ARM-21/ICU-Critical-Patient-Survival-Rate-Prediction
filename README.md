# ICU-Critical-Patient-Survival-Rate-Prediction

This repository focuses on an ICU survival prediction application: building, evaluating, and comparing classifiers to predict short-term survival for critical patients using the SUPPORT2 dataset. The codebase also contains additional example experiments (e.g., credit/loan analyses), but the primary application is ICU survival prediction.

**Application purpose**

- Provide reproducible pipelines to preprocess SUPPORT2 data, train candidate classifiers, and evaluate model performance for clinical decision-support.
- Enable model comparison based on performance, calibration, and practical constraints specific to ICU outcome prediction.

**Contents & Key files**
- `Critical_Patient_Survival_Implementation.ipynb`: notebook with the clinical prediction analysis and results.
- `support2-1.csv`: SUPPORT2 cohort data used for the ICU survival experiments.
- `support2_modeling.py` (root): end-to-end modeling script comparing Logistic Regression, KNN, Decision Tree, and Random Forest.
- `app.py`: example application or experiment runner.
- `Column_Visualization.ipynb`, `Feature_Details.json`, `category_summary.csv`: helper notebooks and artifacts used in analysis and visualization.
- `requirements.txt`: Python dependencies.

**Implemented models**

The project includes implementations and comparisons of common supervised classifiers:
- Logistic Regression
- K-Nearest Neighbours (KNN)
- Decision Tree
- Random Forest

**Implementation & pipeline details**

- Data preparation: remove identifiers and leakage columns, handle missing values, and split into features/target.
- Preprocessing pipeline: median imputation + scaling for numeric features; most-frequent imputation + one-hot encoding for categorical features. Implemented as a scikit-learn `ColumnTransformer` in `support2_modeling.py`.
- Training: stratified 80/20 train/test split; models trained via a scikit-learn `Pipeline` combining preprocessing and estimator.
- Evaluation: accuracy, precision, recall, F1-score, ROC AUC, and Brier score are computed for each candidate model. Results are printed and can be saved to CSV for comparison.

**Model selection rationale**

- Prioritize models with strong ROC AUC and balanced precision/recall for the class of interest, especially for imbalanced datasets.
- Use Brier score to assess calibration when probability estimates matter for downstream decisions.
- Consider interpretability and computational cost when finalizing a deployed model (Decision Trees for interpretability, Random Forests for performance, Logistic Regression for simplicity and calibration).

**Reproducing experiments**

1. Create and activate a virtual environment, then install dependencies:

   ```bash
   python -m venv .venv
   source .venv/Scripts/activate   # Windows (Git Bash / MSYS) or use Activate.ps1 for PowerShell
   pip install -r requirements.txt
   ```

2. Run the SUPPORT2 modeling script:

   ```bash
   python support2_modeling.py
   ```

3. Open the notebooks to inspect loan experiments and other analyses; check `loan_model_metrics.csv` for saved comparisons.

**License & attribution**

This project is provided under the MIT License. See the `LICENSE` file and replace the owner placeholder before publishing.

**Questions or updates**

If you'd like the README to include a table of model metrics, deployment guidance, or a `CONTRIBUTING.md`, tell me which and I will add it.