# TODO-1: add convert_to_letter_grade(score) function
    
def convert_to_letter_grade(score):
    """
    Converts a numeric score to its corresponding letter grade.

    Args:
        score (float or int): The numerical score to be converted.
        
    Returns:
        str: A string representing the letter grade equivalent of the input score.
            Possible return values include "A", "B", "C", "D", and "F"

    Raises:
        ValueError: If the input score is outside the range of 0 to 100.
        TypeError: If the input score is not an int or float.
    """
    # check if the user input for score is an integer or float type
    if not isinstance(score, (int, float)):
        # raise the TypeError with appropriate message if it's not per lab instructions
        raise TypeError("Score must be a numerical value")
    
    # check if the user input is between 0 and 100
    if score < 0 or score > 100:
        # raise the ValueError with appropiate message if it's not per lab instructions 
        raise ValueError("Score must be between 0 and 100")
    
    # determine the letter grade based on provided score
    # if score is 90 - 100, return A
    if score >= 90:
        return 'A'
    # if score is 80 - 89, return B
    elif score >= 80:
        return 'B'
    # if score is 70 - 79, return C
    elif score >= 70:
        return 'C'
    # if score is 60 - 69, return D
    elif score >= 60:
        return 'D'
    # if score is below a 60, return F
    else:
        return 'F'
    
