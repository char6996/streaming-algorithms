import pandas as pd

def simulate_stream(csv_file):
    """
    Simulates a stream by yielding events one by one from the CSV file.
    Each event includes a UNIX timestamp and item_id.
    """
    df = pd.read_csv(csv_file)

    # Clean column names (strip spaces and lowercase)
    df.columns = df.columns.str.strip().str.lower()

    # Rename itemid to item_id if needed
    if 'itemid' in df.columns:
        df.rename(columns={'itemid': 'item_id'}, inplace=True)

    # Convert timestamp to UNIX time
    if not pd.api.types.is_numeric_dtype(df['timestamp']):
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df.dropna(subset=['timestamp'], inplace=True)
        df['timestamp'] = df['timestamp'].astype('int64') // 10**9

    df.dropna(subset=['item_id'], inplace=True)
    df.sort_values(by='timestamp', inplace=True)

    for _, row in df.iterrows():
        yield {
            'timestamp': int(row['timestamp']),
            'item_id': row['item_id']  # ✅ Fixed key name
        }
