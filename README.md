# 📊 CSV Data Analyzer & Dashboard

An interactive web application built with Python and Streamlit to automatically analyze, visualize, and filter any CSV dataset. This tool allows users to upload their data and instantly generate insights without writing a single line of code.

**➡️ [Try the Live Demo Here!](YOUR_STREAMLIT_APP_URL_HERE)** 
*(Note: Replace with your actual Streamlit app URL after deployment)*

 
*(Note: Replace this with a real screenshot URL of your app)*


## ✨ Key Features

- **⬆️ Easy CSV Upload:** Upload any CSV file with a simple drag-and-drop interface.
- **👀 Instant Data Overview:** View the first few rows (`.head()`) and key statistics (`.describe()`) of your dataset right after uploading.
- **📈 Dynamic Chart Generation:** Create interactive **Bar Charts** and **Line Charts** on the fly.
- **⚙️ Powerful Aggregation:** Summarize large datasets using functions like **Sum, Mean, Count, and Median** to prevent performance issues and gain meaningful insights.
- **🔍 Smart Filtering:** Filter your data based on categorical columns to drill down into specific segments.
- **🚀 Fast & Responsive:** Built with Streamlit's caching for a smooth and efficient user experience.

## 🛠️ Technology Stack

- **Language:** Python
- **Web Framework:** Streamlit
- **Data Manipulation:** Pandas
- **Interactive Charting:** Plotly

## 🚀 How to Run this Project Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dhanveeryadav-max/CSV-Data-Analyzer-Streamlit.git
    cd CSV-Data-Analyzer-Streamlit
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

Now, open your web browser and go to `http://localhost:8501`.
