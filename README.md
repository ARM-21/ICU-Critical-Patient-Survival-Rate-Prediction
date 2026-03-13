# Smart Data Discovery — Coursework

This repository contains coursework, notebooks, datasets, and scripts used for the Smart Data Discovery project and related assignments.

**Project:** Smart Data Discovery — AI / Data Science coursework and experiments

**Scope:** A collection of Jupyter notebooks, Python scripts, and CSV datasets demonstrating data preprocessing, exploratory analysis, modeling, and evaluation for course assignments.

**Contents & Highlights**
- **Description:** Notebooks and scripts covering classification, regression, evaluation metrics, and data visualization.
- **Key files:**
	- `requirements.txt`: Python dependencies
	- `loan_model_metrics.csv`, `loan_data.csv`, `loan.csv`: example datasets and results
	- Notebooks: many `*.ipynb` files demonstrating experiments (decisionTree.ipynb, support2_modeling.py, etc.)

**Getting Started**

1. Clone the repository.
2. Create a Python virtual environment and activate it:

	 - Windows (PowerShell):

		 ```powershell
		 python -m venv .venv
		 .\.venv\Scripts\Activate.ps1
		 ```

	 - macOS / Linux:

		 ```bash
		 python3 -m venv .venv
		 source .venv/bin/activate
		 ```

3. Install dependencies:

	 ```bash
	 pip install -r requirements.txt
	 ```

4. Open notebooks with Jupyter or VS Code and run cells for exploration and training.

**Usage & Typical Workflows**

- Exploratory analysis: open the appropriate notebook (e.g., `decisionTree.ipynb`) and run the cells.
- Training models: run the modeling notebooks or Python scripts (search for files named `*_modeling` or `support2_modeling.py`).
- Evaluating models: results and metrics are saved in CSV files such as `loan_model_metrics.csv`.

**Project Structure (selected)**
- `coursework/` — coursework-specific notebooks and helper files.
- `week-*` folders — tutorial notebooks and practice exercises.
- `scraping/` — files related to web scraping experiments.

**Data & Privacy**

Datasets included are intended for coursework and learning. If any dataset contains sensitive or personal data, remove or anonymize it before sharing publicly.

**License**

This project is licensed under the MIT License — see the included `LICENSE` file for the full text. Replace the license owner placeholder in `LICENSE` with the appropriate name or organization.

**How to Contribute**

- If you'd like to contribute improvements, open an issue or send a pull request with a clear description of changes.
- Keep notebooks reproducible: include environment requirements, and prefer scripts for long-running training.

**Contact & Attribution**

For questions or collaboration requests, add a note in an issue or contact the repository owner. Acknowledge course instructors or datasets where applicable.

**Next steps**
- Replace placeholder owner name in `LICENSE`.
- Optionally add a short `CONTRIBUTING.md` describing contribution expectations and code style.

---

Version: 1.0 — README drafted and added license (update owner as needed).