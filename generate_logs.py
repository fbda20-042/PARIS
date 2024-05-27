import pandas as pd
import numpy as np

# Define the log file path (assuming it is the same)
log_file_path = 'web_server_logs.csv'

# Generate some example log data
def generate_logs():
    # Create a DataFrame with example log data
    data = {
        'Timestamp': pd.date_range(start='2023-01-01', periods=100, freq='H'),
        'IP': np.random.choice(['192.168.0.1', '192.168.0.2', '192.168.0.3'], size=100),
        'Request': np.random.choice(['/home', '/about', '/contact', '/products'], size=100),
        'Status': np.random.choice([200, 404, 500], size=100),
        'Age': np.random.choice([18, 25, 35, 45, 60], size=100),
        'Gender': np.random.choice(['Male', 'Female'], size=100),
        'Country': np.random.choice(['USA', 'Canada', 'Brazil', 'UK', 'Germany', 'China', 'India', 'Australia', 'South Africa'], size=100),
        'City': np.random.choice(['New York', 'Toronto', 'São Paulo', 'London', 'Berlin', 'Beijing', 'Mumbai', 'Sydney', 'Cape Town'], size=100),
        'Sport': np.random.choice(['Soccer', 'Basketball', 'Baseball', 'Tennis'], size=100)
    }
    df = pd.DataFrame(data)
    df.to_csv(log_file_path, index=False)

# Generate the logs
generate_logs()

# Function to read and analyze web server log data
def analyze_logs():
    # Read web server log data from CSV file
    log_data = pd.read_csv(log_file_path)

    # Ensure necessary columns are present
    required_columns = ['Timestamp', 'IP', 'Request', 'Status', 'Age', 'Gender', 'Country', 'City', 'Sport']
    if not all(column in log_data.columns for column in required_columns):
        raise ValueError("Missing required columns in the log data.")

    # Filter out rows with missing data
    log_data.dropna(subset=required_columns, inplace=True)

    return log_data

# Analyze logs
log_data = analyze_logs()

# Calculate required metrics
total_visits = len(log_data)
unique_visitors = log_data['IP'].nunique()
most_visited_pages = log_data['Request'].value_counts().head(10)
demographics = log_data.groupby(['Age', 'Gender']).size().reset_index(name='Count')
geographic_distribution = log_data.groupby(['Country', 'City']).size().reset_index(name='Count')
sport_popularity = log_data['Sport'].value_counts()

# Add count column to log_data for continent chart
log_data['Count'] = 1

# Save the updated log data with the Count column
log_data.to_csv('web_server_logs_updated.csv', index=False)
