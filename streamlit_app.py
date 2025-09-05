import streamlit as st
import pandas as pd
from utils.reconcile import reconcile_data, generate_discrepancy_report

st.set_page_config(page_title="Invoice Reconciliation Tool", layout="wide")

st.title("🧾 Invoice Reconciliation Tool")
st.caption("Compare vendor invoices with accounting exports to detect mismatches.")

st.markdown("#### Step 1: Upload your files")

col1, col2 = st.columns(2)

with col1:
    vendor_file = st.file_uploader("Vendor Invoice", type=["csv"])
with col2:
    accounting_file = st.file_uploader("Accounting Export", type=["csv"])

if vendor_file and accounting_file:
    vendor_df = pd.read_csv(vendor_file)
    accounting_df = pd.read_csv(accounting_file)

    st.markdown("#### Step 2: Reconciliation Summary")
    result_df, summary = reconcile_data(vendor_df, accounting_df)

    st.write("**Summary:**", summary)

    st.markdown("#### Step 3: Discrepancy Report")
    report_df = generate_discrepancy_report(result_df)
    st.dataframe(report_df, use_container_width=True)

    csv = report_df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Report", csv, "discrepancy_report.csv", "text/csv")

else:
    st.info("Upload both files to begin.")
