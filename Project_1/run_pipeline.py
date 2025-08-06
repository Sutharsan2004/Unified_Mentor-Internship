from src.utils import load_csv, merge_data
from src.data_preprocessing import *
from src.feature_engineering import create_features
from src.model_training import train_model
from src.evaluate_model import evaluate_model

from sklearn.preprocessing import StandardScaler


# Load and preprocess
ad = preprocess_admissions(load_csv('data/raw/admissions.csv'))
fa = preprocess_fatality(load_csv('data/raw/fatalities.csv'))
me = preprocess_metrics(load_csv('data/raw/metrics.csv'))
pr = preprocess_prescriptions(load_csv('data/raw/prescriptions.csv'))
sm = preprocess_smokers(load_csv('data/raw/smokers.csv'))

# Merge
merged = merge_data([ad, fa, me, sm])
df = create_features(merged)
print("Available columns:\n", df.columns.tolist())


#  Train
features = [
    "Affordability Index Scaled",
    "Expenditure Ratio",
    "Smoker Rate",
    "Admission Rate",
    "Tobacco Price Index",
    "Household Expenditure on Tobacco"
]
scaler = StandardScaler()
df[features] = scaler.fit_transform(df[features])

# Show some known class 1 examples
print("Sample inputs with Mortality Label = 1:\n")
print(df[df["Mortality Label"] == 1][[
    "Affordability Index Scaled",
    "Expenditure Ratio",
    "Smoker Rate",
    "Admission Rate",
    "Tobacco Price Index",
    "Household Expenditure on Tobacco"
]].head())

print(df["Mortality Rate"].describe())
print(df["Mortality Label"].value_counts())

model, X_test, y_test = train_model(df, features, 'Mortality Label')


# Evaluate
report, roc = evaluate_model(model, X_test, y_test)
print(report)
print(f"ROC AUC: {roc}")
