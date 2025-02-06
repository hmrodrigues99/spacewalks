
import pytest
from eva_data_analysis import text_to_duration
from eva_data_analysis import calculate_crew_size

def test_calculate_screw_size ():
    """
    Test the calculate_crew_size function with different crew inputs
    """
    
    # Typical value 1 - a crew with 4 members
    actual_result = calculate_crew_size("Hugo;Carolina;Beatriz;Ivan")
    expected_result = 4
    assert actual_result == expected_result
    
    # Typical value 2 - a crew with 1 lonely member
    actual_result = calculate_crew_size("Diogo")
    expected_result = 1
    assert actual_result == expected_result

    # Typical value 3 - Empty crew
    actual_result = calculate_crew_size("")
    expected_result = None
    assert actual_result == expected_result


def test_text_to_duration_float():
    """
    Test that text_to_duration returns the correct value for a float input
    (non-zero component)
    """
    assert text_to_duration("10:20") == pytest.approx(10.3333333)


def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10