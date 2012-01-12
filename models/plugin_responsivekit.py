from gluon.tools import PluginManager
from gluon import current

plugins = PluginManager('responsivekit', service='PIL',
                                            pil_format='JPEG',
                                            pil_quality=50,
                                            pil_optimize=1,
                                            pil_size=(300,300))
current.plugins = plugins