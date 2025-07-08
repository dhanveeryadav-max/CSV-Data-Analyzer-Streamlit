import streamlit as st
import pandas as pd
from chart_utils import create_bar_chart, create_line_chart

# --- Page Configuration ---
st.set_page_config(
    page_title="CSV Data Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 CSV Data Analyzer")
st.write("Upload your CSV file and get instant data analysis, charts, and filters.")

# --- File Uploader ---
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # --- Read the data ---
    try:
        # Use a cache to avoid reloading data on every interaction
        @st.cache_data
        def load_data(file):
            return pd.read_csv(file)
        
        df = load_data(uploaded_file)
        st.success("File uploaded and processed successfully!")

        # --- Sidebar for user inputs ---
        with st.sidebar:
            st.header("Chart & Filter Options")

            # --- Identify column types for user selection ---
            numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
            categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
            
            # --- Chart Selection ---
            st.subheader("1. Select Chart Type")
            chart_type = st.selectbox("Chart Type", ["Bar Chart", "Line Chart"])

            # --- Column Selection for Chart ---
            st.subheader("2. Select Columns for Chart")
            if categorical_cols:
                x_axis = st.selectbox("Select X-axis (Categorical/Dimension)", categorical_cols)
            else:
                st.warning("No categorical columns found for the X-axis.")
                x_axis = None
                
            if numeric_cols:
                y_axis = st.selectbox("Select Y-axis (Numerical/Measure)", numeric_cols)
            else:
                st.warning("No numerical columns found for the Y-axis.")
                y_axis = None
            
            # --- Aggregation Function Selection (THE KEY FIX!) ---
            st.subheader("3. Select Aggregation")
            # Define aggregation options based on the chosen Y-axis
            if y_axis:
                agg_function_options = ["Sum", "Mean", "Count", "Median", "Min", "Max"]
                aggregation = st.selectbox("How to aggregate the Y-axis?", agg_function_options)
            else:
                aggregation = "Sum" # Default value

            # --- Data Filtering ---
            st.subheader("4. Filter Your Data")
            selected_filters = {}
            for col in categorical_cols:
                all_options = df[col].unique()
                # To prevent crashing with too many options, we limit the multiselect
                if len(all_options) < 100:
                    selected_options = st.multiselect(f"Filter by {col}", all_options, default=all_options)
                    selected_filters[col] = selected_options
        
        # --- Apply filters to the dataframe ---
        filtered_df = df.copy()
        for col, selected in selected_filters.items():
            filtered_df = filtered_df[filtered_df[col].isin(selected)]

        # --- Display Data and Charts in the main area ---
        st.header("Data Analysis & Visualization")

        # --- Aggregate data before plotting ---
        if x_axis and y_axis:
            st.subheader(f"{aggregation} of {y_axis} by {x_axis}")
            
            agg_map = {'Sum': 'sum', 'Mean': 'mean', 'Count': 'count', 'Median': 'median', 'Min': 'min', 'Max': 'max'}
            agg_func = agg_map.get(aggregation)

            # Perform groupby and aggregation
            aggregated_df = filtered_df.groupby(x_axis)[y_axis].agg(agg_func).reset_index()

            if chart_type == "Bar Chart":
                fig = create_bar_chart(aggregated_df, x_col=x_axis, y_col=y_axis, title=f"{aggregation} of {y_axis} by {x_axis}")
            else: # Line Chart
                fig = create_line_chart(aggregated_df, x_col=x_axis, y_col=y_axis, title=f"{aggregation} of {y_axis} by {x_axis}")
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Please select columns for the X and Y axis in the sidebar to generate a chart.")

        # --- Display Data Overview and Filtered Data ---
        with st.expander("Show Data Tables", expanded=False):
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Original Data Sample")
                st.dataframe(df.head())
            
            with col2:
                st.subheader("Filtered & Aggregated Data")
                if 'aggregated_df' in locals():
                    st.dataframe(aggregated_df)
                else:
                    st.write("Data will be shown here after generating a chart.")

    except Exception as e:
        st.error(f"An error occurred. Please check your CSV file format. Error: {e}")