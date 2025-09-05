import pandas as pd

def reconcile_data(vendor_df, accounting_df):
    merged = pd.merge(vendor_df, accounting_df, on="InvoiceNumber", how="outer", suffixes=("_vendor", "_accounting"))
    merged["Amount Discrepancy"] = merged["Amount_vendor"].fillna(0) - merged["Amount_accounting"].fillna(0)
    merged["Discrepancy"] = merged["Amount Discrepancy"].abs() > 1e-2  # Tolerance

    summary = {
        "Total Invoices (Vendor)": len(vendor_df),
        "Total Invoices (Accounting)": len(accounting_df),
        "Discrepancies Found": merged["Discrepancy"].sum()
    }
    return merged, summary

def generate_discrepancy_report(df):
    return df[df["Discrepancy"] == True].copy()
