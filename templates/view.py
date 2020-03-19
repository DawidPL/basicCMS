import locale
import sys
 
def view_locale(request):
    loc_info = "getlocale: " + str(locale.getlocale()) + \
        "<br/>getdefaultlocale(): " + str(locale.getdefaultlocale()) + \
        "<br/>fs_encoding: " + str(sys.getfilesystemencoding()) + \
        "<br/>sys default encoding: " + str(sys.getdefaultencoding())
        "<br/>sys default encoding: " + str(sys.getdefaultencoding())
    return HttpResponse(loc_info)