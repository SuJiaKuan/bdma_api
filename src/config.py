import os


class Config(object):
    API_VERSION = 'v1'
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    MIDTERM_MEMBERS = [
        "107810040",
        "106320202",
        "108830040",
        "108332043",
        "107331002",
        "107830013",
        "107830017",
        "107830023",
        "107830039",
        "107830050",
        "107830054",
        "106331039",
        "106331040",
        "106830031",
        "106830046",
        "106830052",
        "106340118",
        "106370138",
        "107440014",
        "108AC1008",
    ] + [
        "aintut_midterm_{}".format(idx)
        for idx in range(10)
    ]
