from errors import InvalidAnswersFormat
from utils import str2int


def correct_midterm_section1(answers):
    if len(answers) != 10:
        raise InvalidAnswersFormat

    norm_answers = [a.upper().strip() for a in answers]

    return [
        norm_answers[0].upper() == "A",
        norm_answers[1].upper() == "A",
        norm_answers[2].upper() == "D",
        norm_answers[3].upper() == "D",
        norm_answers[4].upper() == "C",
        norm_answers[5].upper() == "C",
        norm_answers[6].upper() == "A",
        norm_answers[7].upper() == "C",
        norm_answers[8].upper() == "C",
        norm_answers[9].upper() == "B",
    ]


midterm_function_mapping = {
    1: correct_midterm_section1,
}

