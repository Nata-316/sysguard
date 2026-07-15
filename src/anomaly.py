import json
import numpy as np
from sklearn.ensemble import IsolationForest
from pathlib import Path

LOG_FILE = Path(__file__).parent.parent / 'logs' / 'sysguard.log'
def load_data():
    data = []
    with open(LOG_FILE, 'r') as f:
        for line in f:
            try:
                entry = json.loads(line)
                if 'cpu' in entry:
                    data.append([
                        entry['cpu'],
                        entry['memory_percent'],
                        entry['disk_percent'],
                        entry['network_sent'],
                        entry['network_recv']
                    ])
            except json.JSONDecodeError:
                continue
    return data

def train_model(data):
    X = np.array(data)
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(X)
    return model

def detect(model, reading):
    X = np.array([[
        reading['cpu'],
        reading['memory_percent'],
        reading['disk_percent'],
        reading['network_sent'],
        reading['network_recv']
    ]])
    prediction = model.predict(X)
    return prediction[0] == -1

if __name__ == "__main__":
    data = load_data()
    print(f"Loaded {len(data)} readings")
    if len(data) >= 10:
        model = train_model(data)
        print("Model trained successfully")
    else:
        print("Not enough data yet — need at least 10 readings")