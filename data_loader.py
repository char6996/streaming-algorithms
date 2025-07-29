import pandas as pd

def load_events(file_path):
    df = pd.read_csv(file_path)
    
    # Rename columns for consistency with code
    df.rename(columns={
        'visitorid': 'user_id',
        'event': 'event_type',
        'itemid': 'item_id'
    }, inplace=True)
    
    # Drop rows with any missing values in essential columns
    df = df.dropna(subset=['user_id', 'timestamp', 'event_type', 'item_id'])
    df['user_id'] = df['user_id'].astype(int)
    df['item_id'] = df['item_id'].astype(int)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    
    return df
