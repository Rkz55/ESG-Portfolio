# ESG Portfolio Analysis Dashboard

This Streamlit application provides an interactive dashboard for analyzing ESG (Environmental, Social, and Governance) performance of investment funds and companies.

## Features

- Interactive ESG metrics visualization
- Comparative analysis between funds and companies
- Financial and extra-financial performance tracking
- Dynamic filtering and data exploration
- Responsive and user-friendly interface

## Setup

1. Clone this repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application locally:
```bash
streamlit run app.py
```

## Deployment to Streamlit Community Cloud

1. Push your code to GitHub

2. Go to [Streamlit Community Cloud](https://share.streamlit.io/)

3. Sign in with your GitHub account

4. Click "New app"

5. Select your repository, branch, and the main file (app.py)

6. Click "Deploy"

## Data

The current version uses sample data for demonstration purposes. To use real data:

1. Replace the sample data in the `load_data()` function in `app.py`
2. Update the metrics and visualizations according to your data structure

## Contributing

Feel free to submit issues and enhancement requests! 