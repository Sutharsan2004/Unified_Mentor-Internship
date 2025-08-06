from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)

    # Evaluation metrics
    report = classification_report(y_test, y_pred, zero_division=0)
    roc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    cm = confusion_matrix(y_test, y_pred)

    # Print inside the function
    print("📊 Classification Report:\n", report)
    print("📉 Confusion Matrix:\n", cm)
    print(f"🔍 ROC AUC Score: {roc:.4f}")

    return report, roc
