from flask_restful import reqparse
from flask_restful import Resource

from errors import ParameterMissing
from assignments import assignment_function_mapping


class AssignmentSubmission(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "sid",
            type=str,
            required=True,
        )
        parser.add_argument(
            "ordinal",
            type=int,
            choices=assignment_function_mapping.keys(),
            required=True,
        )
        parser.add_argument(
            "answers",
            required=True,
            action="append",
        )

        try:
            args = parser.parse_args()
        except Exception:
            raise ParameterMissing

        correctnesses = assignment_function_mapping[args.ordinal](args.answers)

        return {
            "correctnesses": correctnesses,
        }
