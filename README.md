# Candy Case Study

## Overview
Analysis of candy popularity based on various attributes including brand ownership, composition features, and market characteristics.

## Project Structure
candy_case_study/
├── data/
│   ├── candy-data.csv
│   └── candy-data-cleaned.csv
├── notebooks/
│   ├── exploratory_data_analysis.ipynb
│   ├── feature_engineering.ipynb
│   └── analysis_modeling.ipynb
├── utils/
│   ├── llm.py
│   └── text_matching.py
├── requirements.txt
└── README.md

## Data

### Original Features
- Binary features: chocolate, fruity, caramel, peanutyalmondy, nougat, crispedricewafer, hard, bar, pluribus  
- Continuous features: sugarpercent, pricepercent  
- Target: winpercent (converted to 0–1 scale)

### Engineered Features
- mother_company: Parent brand (identified via GPT-4)  
- big_brand: Binary flag for top 7 companies by product count

## Key Findings

### Statistical Analysis
- ANOVA test (p < 0.05): Significant differences in win percentage across mother companies  
- Normality tests (Shapiro–Wilk): All major brands show normally distributed win percentages  
- Top performers: Companies with 3+ products tested

### Model Performance

#### Baseline OLS
- Cross-validation RMSE: ~11.5%

#### CatBoost with Brand Features
- Improved explainability through SHAP values  
- Category features: All binary attributes + mother_company  
- Hyperparameters: 100 iterations, learning rate 0.05, depth 6

## Usage

1. Setup environment  
```uv sync```

2. Add API key to `.env`:  
```OPENAI_API_KEY=your_key_here```
