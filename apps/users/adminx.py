import xadmin
from users.models import BannerInfo, EmailVerifyCode
from xadmin import views

class GloblaXadminSetting(object):
    site_title = "网站管理后台"
    site_footer = "中国威武公司"
    menu_style = 'accordion'


class BannerInfoXadmin(object):
    list_display = ['image', 'url', 'add_time']
    search_fields = ['image', 'url']
    list_filter = ['image', 'url']
    model_icon = 'fa fa-picture-o'
class EmailVerifyCodeXadmin(object):
    list_display = ['code', 'email', 'send_type', 'add_time']
    model_icon = 'fa fa-star'

xadmin.site.register(BannerInfo, BannerInfoXadmin)
xadmin.site.register(EmailVerifyCode, EmailVerifyCodeXadmin)
xadmin.site.register(views.CommAdminView, GloblaXadminSetting)