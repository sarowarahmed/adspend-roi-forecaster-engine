# 🔖 Advertising Sales Predictor

An app powered by a Machine Learning model, to forecast sales based on TV, Newspaper, and Online Advertising

## Demo App
```
├── data/               # Generated CSVs
├── notebooks/          # Exploratory Data Analysis (EDA)
├── scripts/            # generate_data.py
├── src/                # Core logic (pipeline.py, optimizer.py)
├── tests/              # Pytest for your data validation
├── app.py              # Main Streamlit Entrypoint
├── Dockerfile          # Containerization
└── README.md           # The "Sales Pitch" for your project

/app
   app.py
   pages/
      optimizer.py
      model_health.py

/src
   data_generator.py
   train.py
   optimize.py
   validate.py

/models
   pipeline.pkl
   surrogate_model.pkl

/mlruns
/tests
```
