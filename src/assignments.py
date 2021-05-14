from errors import InvalidAnswersFormat
from utils import str2float
from utils import str2int


def correct_assignment_demo(answers):
    if len(answers) != 3:
        raise InvalidAnswersFormat

    return [
        str2int(answers[0]) == 9487,
        abs(str2float(answers[1]) - 9487.9487) <= 0.01,
        answers[2] == "Joe 487",
    ]


assignment_function_mapping = {
    "demo": correct_assignment_demo,
}
