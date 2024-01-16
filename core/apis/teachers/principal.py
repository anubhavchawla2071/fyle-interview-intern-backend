from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
# from core.models.assignments import Assignment
from core.models.teachers import Teacher
from .schema import TeacherSchema

principal_teacher_resources = Blueprint('principal_teacher_resources', __name__)

@principal_teacher_resources.route('/', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of assignments"""
    principal_assignments = Teacher.get_all_teachers()
    principal_assignments_dump = TeacherSchema().dump(principal_assignments, many=True)
    return APIResponse.respond(data=principal_assignments_dump)