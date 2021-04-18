from errors import InvalidAnswersFormat
from utils import str2float
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


def formalize_midterm_section1(answers):
    if answers is None:
        return [None] * 10

    if len(answers) != 10:
        raise InvalidAnswersFormat

    return [str(a) for a in answers]


def correct_midterm_section2(answers):
    if len(answers) != 3:
        raise InvalidAnswersFormat

    return [
        str2int(answers[0]) == 699,
        str2int(answers[1]) == 165,
        abs(str2float(answers[2]) - 384.4969696969697) <= 0.01,
    ]


def formalize_midterm_section2(answers):
    if answers is None:
        return [None] * 3

    if len(answers) != 3:
        raise InvalidAnswersFormat

    return [
        str2int(answers[0]),
        str2int(answers[1]),
        str2float(answers[2]),
    ]


def correct_midterm_section3(answers):
    if len(answers) != 2:
        raise InvalidAnswersFormat

    return [
        answers[0] == "這世界上最不可愛的就是你。我每次看到你，內心就難過到不行"
                      "。好想好想要，每天都跟你一起上學，牽著你不可愛的小手，一"
                      "起難過的轉圈圈。啊！到底要如何，才能馬上就與你見面？讓我"
                      "捏捏你不可愛的小臉，摸摸不可愛的秀髮，玩玩不可愛的小貓咪"
                      "呢？",
        str2int(answers[1]) == 96,
    ]


def formalize_midterm_section3(answers):
    if answers is None:
        return [None] * 2

    if len(answers) != 2:
        raise InvalidAnswersFormat

    return [
        str(answers[0]),
        str2int(answers[1]),
    ]


def correct_midterm_section4(answers):
    if len(answers) != 3:
        raise InvalidAnswersFormat

    return [
        answers[0] == "PSG Maple",
        abs(str2float(answers[1]) - 4.45887564208364) <= 0.01,
        answers[2] == "PSG Talon",
    ]


def formalize_midterm_section4(answers):
    if answers is None:
        return [None] * 3

    if len(answers) != 3:
        raise InvalidAnswersFormat

    return [
        str(answers[0]),
        str2float(answers[1]),
        str(answers[2]),
    ]


def correct_midterm_section5(answers):
    if len(answers) != 4:
        raise InvalidAnswersFormat

    return [
        str2int(answers[0]) == 994,
        str2int(answers[1]) == 109,
        abs(str2float(answers[2]) - 0.6535362578334826) <= 0.01,
        answers[3] == "Lunalight Leo Dancer",
    ]


def formalize_midterm_section5(answers):
    if answers is None:
        return [None] * 4

    if len(answers) != 4:
        raise InvalidAnswersFormat

    return [
        str2int(answers[0]),
        str2int(answers[1]),
        str2float(answers[2]),
        str(answers[3]),
    ]


def correct_midterm_section6(answers):
    if len(answers) != 3:
        raise InvalidAnswersFormat

    return [
        abs(str2float(answers[0]) - (-0.7784267838977756)) <= 0.01,
        abs(str2float(answers[1]) - (-6.475517953250464)) <= 0.01,
        answers[2] == "displacement",
    ]


def formalize_midterm_section6(answers):
    if answers is None:
        return [None] * 3

    if len(answers) != 3:
        raise InvalidAnswersFormat

    return [
        str2float(answers[0]),
        str2float(answers[1]),
        str(answers[2]),
    ]


midterm_function_mapping = {
    "correct": {
        1: correct_midterm_section1,
        2: correct_midterm_section2,
        3: correct_midterm_section3,
        4: correct_midterm_section4,
        5: correct_midterm_section5,
        6: correct_midterm_section6,
    },
    "formalize": {
        1: formalize_midterm_section1,
        2: formalize_midterm_section2,
        3: formalize_midterm_section3,
        4: formalize_midterm_section4,
        5: formalize_midterm_section5,
        6: formalize_midterm_section6,
    },
}

