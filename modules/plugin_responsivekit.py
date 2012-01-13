from gluon import *
from PIL import Image
import os

def set_screen_size():
    size = (int(current.request.args[0]) / 20 * 20)
    print size
    current.session.plugin_responsivekit_width = (size , size)

def RIMG(url):
    plugins = current.plugins
    service = plugins.responsivekit.service
    if service == 'PIL':
        return resize_with_pil(url)
    if service == 'src.sencha.io':
        return resize_with_sencha(url)

def resize_with_sencha(url):
    size = get_screen_size()
    newurl = current.request.env.http_host + url
    if not size:
        return 'http://src.sencha.io/http://%s' % newurl
    else:
        return 'http://src.sencha.io/%s/http://%s' % (size[0], newurl)
    

def resize_with_pil(url):
    plugins = current.plugins
    apppath = current.request.folder
    filepath = os.path.normpath(apppath + "/../" + url)
    file = os.path.splitext(filepath)[0]
    imgpath = os.path.splitext(url)[0]
    newext = plugins.responsivekit.pil_format
    
    size = get_screen_size()
    if not size:
        return url
        
    respimgfile = "%s.%s.%s" % (file, size[0], newext)
    respimgpath = "%s.%s.%s" % (imgpath, size[0], newext)
    if os.path.exists(respimgfile): 
        return respimgpath
        
    im = Image.open(filepath)
    im.thumbnail(size)
    im.save(respimgfile, format=plugins.responsivekit.pil_format,
                        quality=plugins.responsivekit.pil_quality,
                        optimize=plugins.responsivekit.pil_optimize)
    return respimgpath

def get_screen_size():
    size = current.session.plugin_responsivekit_width
    is_mobile = current.request.user_agent().is_mobile
    if (not size and not is_mobile) or (size and size[0] > 700):
        return None
    elif not size and is_mobile:
        size = plugins.responsivekit.pil_size
    return size
