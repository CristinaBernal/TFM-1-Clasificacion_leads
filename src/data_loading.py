import pandas as pd
from datasets import load_dataset

def load_telco_data():
    dataset = load_dataset("aai510-group1/telco-customer-churn")

    train_df = dataset["train"].to_pandas()
    val_df   = dataset["validation"].to_pandas()
    test_df  = dataset["test"].to_pandas()

    train_df["split"] = "train"
    val_df["split"] = "validation"
    test_df["split"] = "test"

    df = pd.concat([train_df, val_df, test_df], ignore_index=True)

    return df
