from flask_restful import reqparse
from flask_restful import Resource

from errors import ParameterMissing


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
            choices=(
                1,
            ),
            required=True,
        )

        try:
            args = parser.parse_args()
        except Exception:
            raise ParameterMissing

        return {
        }
