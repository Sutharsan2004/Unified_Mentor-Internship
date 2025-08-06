def create_features(df):
    df["Expenditure Ratio"] = df["Expenditure on Tobacco as a Percentage of Expenditure"]
    df["Affordability Index Scaled"] = df["Affordability of Tobacco Index"] / 100
    df["Smoker Rate"] = df["Smoker Rate"].fillna(df["Smoker Rate"].mean())

    # ✅ Manually chosen threshold
    threshold = 15000
    df["Mortality Label"] = (df["Mortality Rate"] > threshold).astype(int)

    return df
