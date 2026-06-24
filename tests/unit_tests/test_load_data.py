from src.suspicious_sensor.utils.descriptive_stats_functions import load_data
import pandas as pd

def test_load_data():
    """Test loading data."""
    result = load_data("pressure_sensor_readings.csv")
    assert isinstance(result, pd.DataFrame)
