import xadmin
from courses.models import CourseInfo, LessonInfo, VideoInfo, SourceInfo

# Create your models here.
class CourseInfoXadmin(object):
    list_display = ['image', 'name', 'study_time', 'study_num', 'level', 'love_num', 'click_num', 'desc', 'detail', 'categaty', 'course_notice', 'course_need',
                    'teacher_tell', 'orginfo', 'teacherinfo', 'add_time']
    model_icon = 'fa fa-taxi'
class LessonInfoXadmin(object):
    list_display = ['name', 'add_time', 'courseinfo']
    model_icon = 'fa fa-shield'

class VideoInfoXadmin(object):
    list_display = ['name', 'study_time', 'study_url', 'lessinfoinfo', 'add_time']
    model_icon = 'fa fa-sort'

class SourceInfoXadmin(object):
    list_display = ['name', 'download', 'courseinfo',  'add_time']
    model_icon = 'fa fa-thumb-tack'
xadmin.site.register(CourseInfo, CourseInfoXadmin)
xadmin.site.register(LessonInfo, LessonInfoXadmin)
xadmin.site.register(VideoInfo, VideoInfoXadmin)
xadmin.site.register(SourceInfo, SourceInfoXadmin)