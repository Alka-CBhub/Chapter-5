# System Identification using SINDy

This repository contains code, notebooks, and results for discovering governing equations for the 5 canonical models using **SINDy** (Sparse Identification of Nonlinear Dynamics).
---

## 📚 Models Included

- **1. FitzHugh–Nagumo Model**
- **2. Goodwin Model**
- **3. Mass-Action Model**
- **4. Oregonator Model**
- **5. Glycolytic Oscillations in Yeast**


Each model includes:
- Time-series simulation and constructing a candidate library for training SINDy.
- Time series and 2D/3D phase-space visualization for original and SINDy identified system.
- Steady state analysis and Interaction network for SINDy identified system.


---
## 📁 Folder Structure

<pre> <code> 
Chapter-5-SINDy/
├── 1_Fitzhugh_Nagumo_Model_L1_chapter5.ipynb
├── 1_Fitzhugh_Nagumo_Model_L2_chapter5.ipynb
├── 2_Goodwin_Model_L1_Chapter5.ipynb
├── 3_Mass_Action_Model_L1_chapter5.ipynb
├── 3_Mass_Action_Model_L2_chapter5.ipynb
├── 4_Oregonator_Model_L1_chapter5.ipynb
├── 4_Oregonator_Model_L2_chapter5.ipynb
├── 5_Glycolytic_Oscillation_L1_chapter5.ipynb
├── 5_Glycolytic_Oscillation_L2_chapter5.ipynb
├── network_utils/ # Interaction network visualization
├── plot_utils/ # Custom plotting and diagnostics
├── steady_states/ # Tools for computing steady states
├── symbolic_parser/ # Symbolic reformulation 
├── environment.yml # Reproducible environment file
└── README.md
</code> </pre>

---
## 🧪 Environment Setup

To reproduce results or run notebooks, install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/).

Then execute in terminal or Git CMD:

```bash
conda env create -f environment.yml
conda activate implicit_sindy
```
This will install all required dependencies into a new environment.

---

🚀 Running the Code
Launch Jupyter after activating the environment:

```bash
jupyter notebook
```

Then open and run any of the notebooks.

---


## 📦 Dependencies
This project uses Python 3.10 with the following key packages:

- pysindy
- sympy
- scikit-learn, scipy, numpy, pandas
- matplotlib, seaborn, plotly, scikit-learn
- graphviz, tqdm

All dependencies are listed in `environment.yml`.

---

## 📬 Contact

For questions or suggestions, please open an issue on the GitHub repository:  
👉 [Alka-CBhub/Chapter-5-SINDy](https://github.com/Alka-CBhub/Chapter-5-SINDy)
