import pandas as pd

def preprocess_admissions(df):
    df = df[df['Metric'].str.lower().str.contains("rate|number")]
    df = df[df['Diagnosis Type'].str.lower().str.contains("primary")]
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
    return df[['Year', 'Value']].rename(columns={"Value": "Admission Rate"})

def preprocess_fatality(df):
    df = df[df['Metric'].str.lower().str.contains("rate|number")]
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
    return df[['Year', 'Value']].rename(columns={"Value": "Mortality Rate"})

def preprocess_metrics(df):
    df.columns = df.columns.str.strip().str.replace("\\n", " ")
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except ValueError:
            pass
    return df

def preprocess_prescriptions(df):
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except ValueError:
            pass
    return df

def preprocess_smokers(df):
    df.columns = df.columns.str.strip().str.replace("\\n", " ")
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except ValueError:
            pass
    return df[['Year', '16 and Over']].rename(columns={"16 and Over": "Smoker Rate"})
