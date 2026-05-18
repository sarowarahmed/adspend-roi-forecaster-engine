import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import joblib

from sklearn.metrics import (
    mean_absolute_error,
    r2_score
)

from src.train import load_data
from src.features import engineer_features
from src.generate_data import generate_data


# -----------------------------------
# Page Config
# -----------------------------------
st.set_page_config(
    page_title="Model Health Dashboard",
    page_icon="🩺",
    layout="wide"
)


# -----------------------------------
# Load Models + Metadata
# -----------------------------------
ridge_pipeline = joblib.load(
    "models/ridge_pipeline.pkl"
)

metadata = joblib.load(
    "models/metadata.pkl"
)

feature_cols = metadata[
    "feature_names"
]