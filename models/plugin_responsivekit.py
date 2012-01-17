from gluon.tools import PluginManager
from gluon import current

"""
Responsivekit configuration:
Here you can change configuration of responsivekit plugin.

Service: PIL / src.sencha.io
* PIL
PIL is required to resize images on your site. 
This works resizing the image on the fly and storing the resized image on disk for future requests.
Images are resized only on multiples of 20px, so a dos attack cannot be accomplished, at least
you can have some tens resized images for each original image.
Please refer to PIL manual for explanation on setting pil_format, pil_quality, pil_optimize, and pil_size.

* src.sencha.io
Use the famous src.sencha.io service, so it works also on evironments in which PIL cannot be installed
pil_* are not used when you choose src.sencha.io.

screensize_filter
It's used to choose wich element of DOM will be used for width reference.
If you have your images in .container and you want your images width no more the .container width
keep the default setting.

screensize_controller, screensize_function
They are used to choose which controller will be called for keeping up with screen size information.
Function should be:

    from plugin_responsivekit import *
    def screensize():
        return set_screen_size()
"""
plugins = PluginManager('responsivekit', service='PIL',
                                            screensize_filter = '.container',
                                            screensize_controller = 'default',
                                            screensize_function = 'screensize',
                                            pil_format='JPEG',
                                            pil_quality=50,
                                            pil_optimize=1,
                                            pil_size=(400,400))
current.plugins = plugins
