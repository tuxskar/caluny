__author__ = 'tuxskar'

from django.utils.translation import ugettext as _
from caluny.models import Student, Teacher

class ROLES:
    student = 'STUD'
    teacher = 'TEAC'

USER_ROLES = {
    ROLES.student: [_("Student"), Student],
    ROLES.teacher: [_('Teacher'), Teacher]
    }