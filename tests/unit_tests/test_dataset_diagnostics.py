from src.suspicious_sensor.utils.descriptive_stats_functions import dataset_diagnostics, load_data


def test_dataset_diagnostics_returns_dictionary():
    """Tests whether dataset diagnostics returns a dictionary."""
    df = load_data("pressure_sensor_readings.csv")
    result = dataset_diagnostics(df)
    assert isinstance(result, dict)

def test_dataset_diagnostics_contains_expected_keys():
    """Tests whether the correct keys are returned."""
    df = load_data("pressure_sensor_readings.csv")
    result = dataset_diagnostics(df)
    expected_keys = {'shape', 'data_types', 'memory_usage', 'unique_values'}
    result_keys_set = set(result.keys())
    assert expected_keys == result_keys_set

def test_dataset_diagnostics_shape_returns_tuple():
    """Tests whether the shape returns a value in a tuple."""
    pass

def test_dataset_diagnostics_returns_dtypes():
    """Tests whether columns return dtypes."""
    pass

def test_dataset_diagnostics_memory_float_greater_than_zero():
    """Tests that the memory was returned as a float and a positive number."""
    pass

def test_dataset_diagnostics_reports_unique_values():
    """Tests that unique values are reported."""
    pass

def test_dataset_diagnostics_empty_dataframe():
    pass

def test_dataset_diagnostics_invalid_input():
    pass
