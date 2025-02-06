
import pytest
from eva_data_analysis import text_to_duration
from eva_data_analysis import calculate_crew_size

@pytest.mark.parametrize("input_value, expected_result", [
    ("Hugo;Carolina;Beatriz;Ivan;", 4),  # Typical value 1 - a crew with 4 members
    ("Diogo;", 1),  # Typical value 2 - a crew with 1 lonely member
    ("", None),  # Typical value 3 - Empty crew
])
def test_calculate_screw_size(input_value, expected_result):
    """
    Test the calculate_crew_size function with different crew inputs
    It uses a decorator at the top to use different inputs
    """
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result


def test_text_to_duration_float():
    """
    Test that text_to_duration returns the correct value for a float input
    (non-zero component)
    """
    assert text_to_duration("10:20") == pytest.approx(10.3333333)


def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10