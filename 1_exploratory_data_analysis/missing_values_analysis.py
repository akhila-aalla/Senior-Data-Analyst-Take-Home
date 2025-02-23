import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno


products_file = "../data/PRODUCTS_TAKEHOME.csv"
transactions_file = "../data/TRANSACTION_TAKEHOME.csv"
users_file = "../data/USER_TAKEHOME.csv"


products_df = pd.read_csv(products_file)
transactions_df = pd.read_csv(transactions_file)
users_df = pd.read_csv(users_file)

print("Data loaded successfully!")


def missing_values_summary(df, dataset_name):
    missing_values = df.isnull().sum()
    missing_percentage = (missing_values / len(df)) * 100
    missing_summary = pd.DataFrame({
        "Dataset": dataset_name,
        "Column": missing_values.index,
        "Missing Values": missing_values.values,
        "Percentage": missing_percentage.values
    })
    return missing_summary[missing_summary["Missing Values"] > 0].sort_values(by="Percentage", ascending=False)

products_missing = missing_values_summary(products_df, "PRODUCTS_TAKEHOME")
transactions_missing = missing_values_summary(transactions_df, "TRANSACTION_TAKEHOME")
users_missing = missing_values_summary(users_df, "USER_TAKEHOME")


missing_data_summary = pd.concat([products_missing, transactions_missing, users_missing], ignore_index=True)

# Save to CSV file
missing_values_csv_path = "../1_exploratory_data_analysis/reports/missing_values_summary.csv"
missing_data_summary.to_csv(missing_values_csv_path, index=False)

print(f" Missing values summary saved: {missing_values_csv_path}")




def plot_missing_heatmap(df, dataset_name):
    plt.figure(figsize=(10,6))
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis", yticklabels=False)
    plt.title(f"Missing Data Heatmap - {dataset_name}")
    plt.show()

print(" Generating missing data heatmaps...")

plot_missing_heatmap(products_df, "PRODUCTS_TAKEHOME")
plot_missing_heatmap(transactions_df, "TRANSACTION_TAKEHOME")
plot_missing_heatmap(users_df, "USER_TAKEHOME")

# Function to plot missing values count
def plot_missing_values_bar(df, dataset_name):
    missing_count = df.isnull().sum()
    missing_count = missing_count[missing_count > 0].sort_values(ascending=False)

    plt.figure(figsize=(12,6))
    sns.barplot(x=missing_count.index, y=missing_count.values, palette="coolwarm")
    plt.title(f"Missing Values Count - {dataset_name}")
    plt.xlabel("Columns")
    plt.ylabel("Missing Count")
    plt.xticks(rotation=45, ha="right")
    plt.show()

print(" Generating missing values bar charts...")

plot_missing_values_bar(products_df, "PRODUCTS_TAKEHOME")
plot_missing_values_bar(transactions_df, "TRANSACTION_TAKEHOME")
plot_missing_values_bar(users_df, "USER_TAKEHOME")


print("\n Missing Values Summary:")
print(missing_data_summary)

summary_report_path = "../1_exploratory_data_analysis/reports/missing_values_analysis.txt"
with open(summary_report_path, "w") as f:
    f.write(" Missing Values Analysis Report\n\n")
    f.write(missing_data_summary.to_string())

print(f" Missing values analysis report saved: {summary_report_path}")