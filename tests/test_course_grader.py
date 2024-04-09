import pytest
from course_grader import convert_to_letter_grade


# TODO-1: Add test_exact_grade_boundaries() function
def test_exact_grade_boundaries():
    assert convert_to_letter_grade(0) == 'F', "Test failed: convert_to_letter_grade(0) should return 'F'"
    assert convert_to_letter_grade(59) == 'F', "Test failed: convert_to_letter_grade(59) should return 'F'"
    assert convert_to_letter_grade(60) == 'D', "Test failed: convert_to_letter_grade(60) should return 'D'"
    assert convert_to_letter_grade(69) == 'D', "Test failed: convert_to_letter_grade(69) should return 'D'"
    assert convert_to_letter_grade(70) == 'C', "Test failed: convert_to_letter_grade(70) should return 'C'"
    assert convert_to_letter_grade(79) == 'C', "Test failed: convert_to_letter_grade(79) should return 'C'"
    assert convert_to_letter_grade(80) == 'B', "Test failed: convert_to_letter_grade(80) should return 'B'"
    assert convert_to_letter_grade(89) == 'B', "Test failed: convert_to_letter_grade(89) should return 'B'"
    assert convert_to_letter_grade(90) == 'A', "Test failed: convert_to_letter_grade(90) should return 'A'"
    assert convert_to_letter_grade(100) == 'A', "Test failed: convert_to_letter_grade(100) should return 'A'"

# TODO-2: Add test_invalid_numerical_score() function
def test_invalid_numerical_score():
    with pytest.raises(ValueError, match="Score must be between 0 and 100"):
        convert_to_letter_grade(-50)
    
    with pytest.raises(ValueError, match="Score must be between 0 and 100"):
        convert_to_letter_grade(150)

# TODO-3: Add test_non_numeric_input() function
def test_non_numeric_input():
    with pytest.raises(TypeError, match="Score must be a numeric value"):
        convert_to_letter_grade("test string")

    with pytest.raises(TypeError, match="Score must be a numeric value"):
        convert_to_letter_grade([91, 92, 93])

    with pytest.raises(TypeError, match="Score must be a numeric value"):
        convert_to_letter_grade(None)