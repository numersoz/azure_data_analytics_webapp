import plotly.express as px
import pandas as pd
import numpy as np

def line_chart():
    """
        Sample Plotly Line Chart
    """
    df = pd.DataFrame({
        "X": np.linspace(0, 10, 100),
        "Y": np.sin(np.linspace(0, 10, 100))
    })

    fig = px.line(df, x = "X", y = "Y", title = "Line Chart")

    return fig

def bar_chart():
    """
        Sample Plotly Bar Chart
    """

    df = pd.DataFrame({
        "Category": ["A", "B", "C", "D", "E"],
        "Values": np.random.randint(10, 100, size = 5)
    })

    fig = px.bar(df, x = "Category", y = "Values", title = "Bar Chart")

    return fig