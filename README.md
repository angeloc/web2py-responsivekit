# Responsivekit for web2py !
## unifying my personal efforts for web2py responsiveness

Here you can find a comprehensive plugin for responsive design in web2py.
It's not so somplete right now, but I planned adding more features.

It's based on my previuos work (web2py-responsive-tables) which it incorporates and new features like responsive images.

It's apckage like a plugin, so to use simply install it as any other plugin.

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


### Live demo
You can find it [here](http://angelo.fluxflex.com/responsivekit)
