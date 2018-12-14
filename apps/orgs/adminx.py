import xadmin
from orgs.models import CityInfo, OrgInfo, TeacherInfo


class CityInfoXadmin(object):
    list_display = ['name', 'add_time']
    model_icon = 'fa fa-filter'


class OrgInfoXadmin(object):
    list_display = ['image', 'name', 'course_num', 'study_num', 'love_num', 'click_num', 'category']
    model_icon = 'fa fa-hotel'

class TeacherInfoXadmin(object):
    list_display = ['image', 'name', 'work_year', 'work_position', 'work_style', 'work_company', 'age', 'gender', 'love_num']
    model_icon = 'fa fa-tty'
xadmin.site.register(CityInfo, CityInfoXadmin)
xadmin.site.register(OrgInfo, OrgInfoXadmin)
xadmin.site.register(TeacherInfo, TeacherInfoXadmin)