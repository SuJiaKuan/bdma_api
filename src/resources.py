import time

from flask_restful import reqparse
from flask_restful import Resource

from config import Config
from errors import ParameterMissing
from assignments import assignment_function_mapping
from models import db
from models import Assignment


class AssignmentSubmission(Resource):

    def _serialize_correctnesses(self, correctnesses):
        return ",".join([
            "1" if c else "0"
            for c in correctnesses
        ])

    def _deserialize_correctnesses(self, correctnesses):
        return [
            True if c == "1" else False
            for c in correctnesses.split(",")
        ]

    def _merge_correctnesses(self, old_correctnesses, new_correctnesses):
        return [
            o or n
            for o, n in zip(old_correctnesses, new_correctnesses)
        ]

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "sid",
            type=str,
        )
        parser.add_argument(
            "ordinal",
            type=int,
            choices=assignment_function_mapping.keys(),
        )

        try:
            args = parser.parse_args()
        except Exception:
            raise ParameterMissing

        query_filter = {}
        if args.sid is not None:
            query_filter["sid"] = args.sid
        if args.ordinal is not None:
            query_filter["ordinal"] = args.ordinal

        assignments = Assignment.query.filter_by(**query_filter).all()

        return [{
            "sid": a.sid,
            "ordinal": a.ordinal,
            "correctnesses": self._deserialize_correctnesses(a.correctnesses),
        } for a in assignments]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "sid",
            type=str,
            required=True,
        )
        parser.add_argument(
            "ordinal",
            type=str,
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

        if args.sid:
            past_assignment = Assignment.query.filter_by(
                sid=args.sid,
                ordinal=args.ordinal,
            ).first()

            if past_assignment is not None:
                updated_correctenesses = self._merge_correctnesses(
                    self._deserialize_correctnesses(
                        past_assignment.correctnesses,
                    ),
                    correctnesses,
                )
                past_assignment.correctnesses = self._serialize_correctnesses(
                    updated_correctenesses,
                )
                db.session.commit()
            else:
                assignment = Assignment(
                    sid=args.sid,
                    ordinal=args.ordinal,
                    correctnesses=self._serialize_correctnesses(correctnesses),
                )
                db.session.add(assignment)
                db.session.commit()

        return {
            "correctnesses": correctnesses,
        }
