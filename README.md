# Responsivekit for web2py !
## unifying my personal efforts for web2py responsiveness

Here you can find a comprehensive plugin for responsive design in web2py.
It's not so complete right now, but I plan adding more features.

It's based on my previuos work (web2py-responsive-tables) which it incorporates new features like responsive images.

It's a web2py plugin, so to use simply install it as any other plugin.

### Features
####Responsive Tables

If you want to use responsive tables in a custom layout, you have to include this code:

	<!--[if !IE]><!-->
	<link rel="stylesheet" type="text/css" href="{{=URL('static','plugin_layout_responsivetables/responsive-tables.css')}}" />
	<script src="{{=URL('static','plugin_layout_responsivetables/responsive-tables.js')}}"></script>
	<!--<![endif]-->

It's important to include conditional directives for IE, because IE doesn't supports this responsive tables design, so it's disabled.

Plugin works changing table's aspect on the fly when the resolution of target device is smaller than 700 pixels, it uses a combination of css media queries and javascript to accomplish the goal. If you want to change the resolution you have to edit both the css and the javascript (replacing 700 with your desired value).

#### Responsive Images
Once the plugin is installed, you have a new model, plugin_responsivekit.py. Within this, you can find plugin default parameters.

##### Service: PIL / src.sencha.io
* PIL:
is required if you want image resizing on your local site. 
This works resizing the image on the fly and storing the resized image on disk for future requests.
Images are resized only on multiples of 20px, so a dos attack cannot be accomplished, at least
you can have some tens resized images for each original image.
Please refer to PIL manual for explanation on setting pil_format, pil_quality, pil_optimize, and pil_size.

* src.sencha.io:
Use the famous src.sencha.io service, so it works also on evironments in which PIL cannot be installed.
pil_* parameters are not used when you choose src.sencha.io.

##### screensize_filter
It's used to choose wich element of DOM will be used for width reference.
If you have your images in .container and you want your images width no more the .container width, you can stick with the default setting.

##### screensize_controller, screensize_function
They are used to choose which controller will be called for keeping up with screen size information.
Function should be:

    from plugin_responsivekit import *
    def screensize():
        return set_screen_size()

This function is called by an ajax script on page load and on page resize and it gets the device resolution guessed by a jquery script.
Device size will be used by responsive image helper **RIMG** to build an image with the desired size.

##### RIMG helper

To make an image responsive, simply put the url in a **RIMG** tag like this:

	#in a view
	{{from plugin_responsivekit import *}}
	{{=IMG(_src=RIMG(URL('static','images/test.jpg')))}}
	
	#in a controller
	from plugin_responsivekit import *
	def test():
		image=IMG(_src=RIMG(URL('static','images/test.jpg')))
		return dict(image=image)

### Live demo
You can find it [here](http://angelo.fluxflex.com/responsivekit)

# License
plugin_responsivekit is Licensed under the **LGPL license version 3** (http://www.gnu.org/licenses/lgpl.html)

