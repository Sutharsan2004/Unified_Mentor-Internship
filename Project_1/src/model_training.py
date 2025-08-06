from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from xgboost import XGBClassifier


def train_model(df, features, target, save_path='model.pkl'):
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

    #clf = RandomForestClassifier(class_weight='balanced', random_state=42)
    clf = XGBClassifier(scale_pos_weight=3)
    clf.fit(X_train, y_train)
    joblib.dump(clf, save_path)

    return clf, X_test, y_test
