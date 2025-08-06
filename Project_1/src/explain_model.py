import shap
import matplotlib.pyplot as plt

def explain(model, X):
    explainer = shap.Explainer(model)
    shap_values = explainer(X)
    shap.summary_plot(shap_values, X)
