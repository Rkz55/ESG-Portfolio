import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from io import StringIO

# Set page config
st.set_page_config(
    page_title="ESG Portfolio Analysis",
    page_icon="🌱",
    layout="wide"
)

# Data loading function
@st.cache_data
def load_data():
    # Create empty dataframes with the required columns
    funds_columns = ['Fund Name', 'ESG Score', 'Carbon Footprint (tCO2e)', 
                    'Financial Return (%)', 'Water Usage (m³)', 'Waste Management Score',
                    'Social Score', 'Governance Score', 'Environmental Score',
                    'Total Assets (M€)', 'Year']
    companies_columns = ['Company', 'ESG Score', 'Carbon Footprint (tCO2e)', 
                        'Financial Return (%)', 'Water Usage (m³)', 'Waste Management Score',
                        'Social Score', 'Governance Score', 'Environmental Score',
                        'Market Cap (M€)', 'Year']
    
    return pd.DataFrame(columns=funds_columns), pd.DataFrame(columns=companies_columns)

# Load data
funds_df, companies_df = load_data()

# Sidebar filters
st.sidebar.title("Filters")
analysis_type = st.sidebar.radio(
    "Select Analysis Type",
    ["Funds Analysis", "Companies Analysis"]
)

# Data upload section in sidebar
st.sidebar.subheader("Upload Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        if analysis_type == "Funds Analysis":
            funds_df = df
        else:
            companies_df = df
        st.sidebar.success("Data uploaded successfully!")
    except Exception as e:
        st.sidebar.error(f"Error uploading file: {str(e)}")

# Main content
st.title("🌱 ESG Portfolio Analysis Dashboard")

# Display filters and metrics
col1, col2, col3 = st.columns(3)

with col1:
    if not funds_df.empty:
        st.metric(
            label="Average ESG Score",
            value=f"{funds_df['ESG Score'].mean():.1f}",
            delta=f"{funds_df['ESG Score'].mean() - 80:.1f}"
        )
    else:
        st.metric(label="Average ESG Score", value="N/A")

with col2:
    if not funds_df.empty:
        st.metric(
            label="Average Carbon Footprint",
            value=f"{funds_df['Carbon Footprint (tCO2e)'].mean():.0f} tCO2e",
            delta=f"{120 - funds_df['Carbon Footprint (tCO2e)'].mean():.0f}"
        )
    else:
        st.metric(label="Average Carbon Footprint", value="N/A")

with col3:
    if not funds_df.empty:
        st.metric(
            label="Average Financial Return",
            value=f"{funds_df['Financial Return (%)'].mean():.1f}%",
            delta=f"{funds_df['Financial Return (%)'].mean() - 12:.1f}%"
        )
    else:
        st.metric(label="Average Financial Return", value="N/A")

# Interactive visualizations
st.subheader("ESG vs Financial Performance")
if not funds_df.empty:
    fig1 = px.scatter(
        funds_df,
        x='ESG Score',
        y='Financial Return (%)',
        size='Total Assets (M€)',
        color='Fund Name',
        hover_data=['Water Usage (m³)', 'Waste Management Score', 'Social Score', 'Governance Score'],
        title="ESG Score vs Financial Return"
    )
    st.plotly_chart(fig1, use_container_width=True)
else:
    st.info("Please upload data to view the ESG vs Financial Performance visualization.")

# ESG Components Analysis
st.subheader("ESG Components Analysis")
if not funds_df.empty:
    col1, col2 = st.columns(2)
    
    with col1:
        fig2 = px.bar(
            funds_df,
            x='Fund Name',
            y=['Environmental Score', 'Social Score', 'Governance Score'],
            title="ESG Components by Fund",
            barmode='group'
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        fig3 = px.scatter(
            funds_df,
            x='Carbon Footprint (tCO2e)',
            y='Water Usage (m³)',
            size='Total Assets (M€)',
            color='Environmental Score',
            hover_data=['Fund Name', 'ESG Score'],
            title="Environmental Impact Analysis"
        )
        st.plotly_chart(fig3, use_container_width=True)

# Time Series Analysis
if not funds_df.empty and 'Year' in funds_df.columns:
    st.subheader("Performance Over Time")
    fig4 = px.line(
        funds_df,
        x='Year',
        y=['ESG Score', 'Financial Return (%)'],
        title="ESG Score and Financial Return Over Time"
    )
    st.plotly_chart(fig4, use_container_width=True)

# Comparative analysis
st.subheader("Comparative Analysis")
if not funds_df.empty:
    metric_to_compare = st.selectbox(
        "Select Metric to Compare",
        ['ESG Score', 'Carbon Footprint (tCO2e)', 'Financial Return (%)', 
         'Water Usage (m³)', 'Waste Management Score', 'Total Assets (M€)']
    )

    fig5 = px.bar(
        funds_df,
        x='Fund Name',
        y=metric_to_compare,
        title=f"{metric_to_compare} by Fund"
    )
    st.plotly_chart(fig5, use_container_width=True)
else:
    st.info("Please upload data to view the Comparative Analysis visualization.")

# Data input section
st.subheader("Data Upload Instructions")
st.markdown("""
To add your data:
1. Prepare a CSV file with the following columns:
   - Fund Name/Company
   - ESG Score
   - Carbon Footprint (tCO2e)
   - Financial Return (%)
   - Water Usage (m³)
   - Waste Management Score
   - Social Score
   - Governance Score
   - Environmental Score
   - Total Assets (M€)/Market Cap (M€)
   - Year
2. Use the upload button in the sidebar to add your data
""")

# Detailed data table
st.subheader("Detailed Data")
if analysis_type == "Funds Analysis":
    st.dataframe(funds_df)
else:
    st.dataframe(companies_df)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Created for Sustainable Finance Course</p>
    </div>
""", unsafe_allow_html=True) 