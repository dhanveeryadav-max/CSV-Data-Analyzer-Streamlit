import plotly.express as px

def create_bar_chart(df, x_col, y_col, title):
    """
    Creates an interactive bar chart using Plotly.
    
    Args:
        df (pd.DataFrame): The dataframe to plot.
        x_col (str): The column for the x-axis (usually categorical).
        y_col (str): The column for the y-axis (usually numerical).
        title (str): The title of the chart.
        
    Returns:
        A Plotly figure object.
    """
    fig = px.bar(df, x=x_col, y=y_col, title=title, template="seaborn")
    return fig

def create_line_chart(df, x_col, y_col, title):
    """
    Creates an interactive line chart using Plotly.
    
    Args:
        df (pd.DataFrame): The dataframe to plot.
        x_col (str): The column for the x-axis (often time-based or numerical).
        y_col (str): The column for the y-axis (numerical).
        title (str): The title of the chart.
        
    Returns:
        A Plotly figure object.
    """
    fig = px.line(df, x=x_col, y=y_col, title=title, template="seaborn")
    return fig