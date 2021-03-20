from errors import InvalidAnswersFormat
from utils import str2int


def correct_assignment1(answers):
    if len(answers) != 4:
        raise InvalidAnswersFormat

    return [
        str2int(answers[0]) == 50,
        str2int(answers[1]) == 99,
        str2int(answers[2]) == 70,
        answers[3] == "Regirock",
    ]


assignment_function_mapping = {
    1: correct_assignment1,
}
