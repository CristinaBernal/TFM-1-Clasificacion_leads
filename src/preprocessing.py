# preprocessing.py
import pandas as pd
import numpy as np

# ==============================================================================
# FUNCIONES AUXILIARES
# ==============================================================================

def group_dependents(x):
    if x == 0: return "0"
    elif x <= 2: return "1-2"
    elif x <= 4: return "3-4"
    else: return "5+"

def group_referrals(x):
    if x == 0: return "0"
    elif x == 1: return "1"
    else: return "2+"

def categorize_extra_data_charges(x):
    if x == 0: return "no charge"
    elif x > 50: return "High"
    else: return "Less"

# ==============================================================================
# FUNCIÓN PRINCIPAL
# ==============================================================================

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # 0. SANITIZACIÓN DE NOMBRES
    df.columns = df.columns.str.strip()

    # ---------------------------------------------------------
    # 1. TRANSFORMACIONES
    # ---------------------------------------------------------
    if "Number of Dependents" in df.columns:
        df["Number Dependents Grouped"] = df["Number of Dependents"].apply(group_dependents)

    if "Number of Referrals" in df.columns:
        df["Referrals Grouped"] = df["Number of Referrals"].apply(group_referrals)

    if "Total Extra Data Charges" in df.columns:
        df["Total Extra Data Charges Category"] = df["Total Extra Data Charges"].apply(categorize_extra_data_charges)

    # Transformaciones Numéricas
    if "Total Charges" in df.columns:
        df["Total Charges Log"] = np.log1p(df["Total Charges"])
        
    if "Total Long Distance Charges" in df.columns:
        upper_cap = df["Total Long Distance Charges"].quantile(0.95)
        df["Total Long Distance Charges Capped"] = df["Total Long Distance Charges"].clip(upper=upper_cap)
        df["Total Long Distance Charges Log"] = np.log1p(df["Total Long Distance Charges Capped"])
        
    if "Total Revenue" in df.columns:
        upper_cap = df["Total Revenue"].quantile(0.95)
        df["Total Revenue Capped"] = df["Total Revenue"].clip(upper=upper_cap)
        df["Total Revenue Log"] = np.log1p(df["Total Revenue Capped"])

    # ---------------------------------------------------------
    # 2. ELIMINACIÓN DE COLUMNAS 
    # ---------------------------------------------------------
    cols_to_drop = [
        'Customer ID', 'Country', 'State', 'City', 'Latitude', 'Longitude', 'Lat Long',
        'Quarter', 'Churn Category', 'Churn Reason', 'Churn Score', 'Zip Code',
        'Population', 'Offer', 'Age', 'Senior Citizen', 
        'Partner', 'Total Refunds', 'Internet Type', 
        'split', 'split_train', 'split_validation', 'Monthly Charge', 'Total Revenue Capped',
        # Originales transformadas:
        'Number of Dependents', 'Number of Referrals', 'Total Charges', 
        'Total Extra Data Charges', 'Total Long Distance Charges', 'Total Revenue', 'Streaming Music'
    ]
    
    existing_cols = [col for col in cols_to_drop if col in df.columns]
    df = df.drop(columns=existing_cols)

    # ---------------------------------------------------------
    # 3. ENCODING
    # ---------------------------------------------------------
    cat_vars = []
    for col in df.select_dtypes(include=["object", "category"]).columns:
        if not (df[col].nunique() == 2 and set(df[col].unique()).issubset({0, 1})):
            cat_vars.append(col)

    if cat_vars:
        df = pd.get_dummies(df, columns=cat_vars, drop_first=True)

    # Convertir bools a int
    bool_cols = df.select_dtypes(include="bool").columns
    if len(bool_cols) > 0:
        df[bool_cols] = df[bool_cols].astype(int)

    # ---------------------------------------------------------
    # 4. LIMPIEZA ESPECÍFICA (Streaming TV)
    # ---------------------------------------------------------
    if 'Streaming TV' in df.columns:
        df = df.drop(columns=['Streaming TV'])

    # ---------------------------------------------------------
    # 5. ELIMINACIÓN POR ALTA CORRELACIÓN 
    # ---------------------------------------------------------
    
    corr = df.corr()

    to_drop = []
    for col in corr.columns:
        for col2 in corr.columns:
            if col != col2 and abs(corr.loc[col, col2]) > 0.90:
                to_drop.append(col2)

    to_drop = list(set(to_drop))
    
    # Solo eliminamos si existen (seguridad por si acaso)
    to_drop = [col for col in to_drop if col in df.columns]
    
    df = df.drop(columns=to_drop)
    print("Variables eliminadas por correlación:", to_drop)

    return df