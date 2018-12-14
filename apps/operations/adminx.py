import xadmin
# Create your models here.
from operations.models import UserLove, UserComment, UserMessage, UserAsk, UserCourse
class UserAskXadmin(object):
    list_display = ['name', 'phone', 'course']
    model_icon = 'fa fa-info'
class UserLoveXadmin(object):
    list_display = ['love_man', 'love_id', 'love_type', 'love_status']
    model_icon = 'fa fa-legal'

class UserCourseXadmin(object):
    list_display = ['study_man', 'study_course', 'add_time']
    model_icon = 'fa fa-minus'
class UserCommentXadmin(object):
    list_display = ['comment_man', 'comment_course', 'comment_content', 'add_time']
    model_icon = 'fa fa-phone'
class UserMessageXadmin(object):
    list_display = ['message_man', 'message_content', 'message_state', 'add_time']
    model_icon = 'fa fa-server'

xadmin.site.register(UserAsk, UserAskXadmin)
xadmin.site.register(UserLove, UserLoveXadmin)
xadmin.site.register(UserCourse, UserCourseXadmin)
xadmin.site.register(UserComment, UserCommentXadmin)
xadmin.site.register(UserMessage, UserMessageXadmin)