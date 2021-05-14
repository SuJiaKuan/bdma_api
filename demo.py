import json
import requests


API_URL = "https://bdma-api.herokuapp.com"
API_VERSION = "v1"


def submit_answers(
    sid,
    ordinal,
    answers,
    api_url=API_URL,
    api_version=API_VERSION,
):
    request_url = "{}/{}/assignments".format(api_url, api_version)

    res = requests.post(request_url, data={
        "sid": sid,
        "ordinal": ordinal,
        "answers": answers,
    })

    data = res.json()

    if res.status_code >= 400:
        print("\x1b[31m{}\x1b[0m".format(json.dumps(data, indent=4)))
        return

    correctnesses =data["correctnesses"]
    for answer, correctness in zip(answers, correctnesses):
        passd_text = \
            "[\033[92mPASS\x1b[0m]" if correctness else "[\x1b[31mFAIL\x1b[0m]"
        print("{} Your answer: {}".format(passd_text, answer))


def query_assignments(
    sid,
    api_url=API_URL,
    api_version=API_VERSION,
):
    request_url = "{}/{}/assignments".format(api_url, api_version)

    res = requests.get(request_url, params={
        "sid": sid,
    })

    data = res.json()

    if res.status_code >= 400:
        print("\x1b[31m{}\x1b[0m".format(json.dumps(data, indent=4)))
        return

    assignments = sorted(data, key=lambda d: d["ordinal"])

    for assignment in assignments:
        ordinal = assignment["ordinal"]
        correctnesses = " ".join([
            "\033[92mPASS\x1b[0m" if c else "\x1b[31mFAIL\x1b[0m"
            for c in assignment["correctnesses"]
        ])
        print("Assignment {}: {}".format(ordinal, correctnesses))


def main():
    submit_answers("user_0", "demo", [9487, 9487.9487, "Joe 487"])
    query_assignments("user_0")


if __name__ == "__main__":
    main()
