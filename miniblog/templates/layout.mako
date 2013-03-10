<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<!--

	Design by Free CSS Templates
	http://www.freecsstemplates.org
	Released for free under a Creative Commons Attribution License

	Name       : Temporary Issue
	Version    : 1.0
	Released   : 20130222

-->
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta name="keywords" content="" />
		<meta name="description" content="" />
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<title>Temporary Issue by FCT</title>
		<link href="http://fonts.googleapis.com/css?family=Arvo" rel="stylesheet" type="text/css" />
		<link href="http://fonts.googleapis.com/css?family=Bitter" rel="stylesheet" type="text/css" />
		<link rel="stylesheet" type="text/css" href="/static/style.css" />
	</head>
	<body>
		<div id="outer">
			<div id="header">
				<div id="logo">
					<h1>
						<a href="#">Javex' Blog</a>
					</h1>
				</div>
				<div id="search">
					<form action="${request.route_url('search')}" method="get">
						<fieldset>
							<input class="text" name="search" size="40" maxlength="128" />
						</fieldset>
					</form>
				</div>
				<div id="nav">
					<ul>
						<li class="first">
							<a href="${request.route_url('home')}">Blog</a>
						</li>
						<li>
							<a href="${request.route_url('add_entry')}">Add Entry</a>
						</li>
						<li class="last">
							<a href="${request.route_url('about')}">About</a>
						</li>
					</ul>
				</div>
			</div>
			<div id="main">
				<div id="content">
					${self.body()}
					
					
					
					<!--<div id="box1">
					
						<h2>
							Welcome to Temporary Issue
						</h2><img class="left" src="static/images/pic1.jpg" width="180" height="220" alt="" />
						<p>
							This is <strong>Temporary Issue</strong>, a three column CSS template designed by
							<a href="http://www.freecsstemplates.org/">FCT</a> with photos from 
							<a href="http://www.pdphoto.org/">PDPhoto</a>. It's released (for free) under the
							<a href="http://www.freecsstemplates.org/license/">Creative Commons Attribution 3.0 license</a>,
							so feel free to use it for any personal or commercial work, just keep our footer credit links intact.
							Hit up our <a href="http://www.freecsstemplates.org/">website</a> for more awesomely
							cool free templates, and follow us on <a href="http://twitter.com/freecsstemplate">Twitter</a>
							(<a href="http://twitter.com/freecsstemplate">@freecsstemplate</a>) for updates, announcements, and other
							mildly interesting ramblings.
						</p>
					</div>
					<div id="box2">
						<h3>
							Interdum praesent non integer
						</h3>
						<p>
							Urna porttitor varius dictum. Risus fringilla tristique dignissim vel vel lorem pharetra. Semper praesent 
							curabitur faucibus suscipit scelerisque luctus. Pellentesque imperdiet viverra aliquet. Nisi lectus sollicitudin 
							phasellus. Montes nullam mollis malesuada interdum. Integer nec sed fringilla aenean luctus blandit suscipit. 
							Eleifend curabitur accumsan aenean lorem ipsum dolore.
						</p>
						<ul class="dateList">
							<li class="first">
								<a href="#">Porta viverra consequat pulvinar ante pretium</a>
								<span class="date">&mdash; 3 hours ago</span>
							</li>
							<li>
								<a href="#">Sed etiam integer veroeros metus leo volutpat aliquet</a>
								<span class="date">&mdash; 18 hours ago</span>
							</li>
							<li>
								<a href="#">Turpis facilisis vel praesent odio vivamus diam primis</a>
								<span class="date">&mdash; Yesterday</span>
							</li>
							<li>
								<a href="#">Fringilla velit vitae hendrerit malesuada phasellus</a>
								<span class="date">&mdash; 2 days ago</span>
							</li>
							<li class="last">
								<a href="#">Ipsum orci faucibus mus mollis porta ante aliquam</a>
								<span class="date">&mdash; 4 days ago</span>
							</li>
						</ul>
					</div>
					-->
					<br class="clear" />
				</div>
				<div id="sidebar2">
					<h3>
						Posuere pretium
					</h3>
					<ul>
						<li class="first">
							<a href="#">Lacinia amet et curae sed pellentesque</a>
						</li>
						<li>
							<a href="#">Vitae a nisi rhoncus sociis veroeros</a>
						</li>
						<li>
							<a href="#">Urna amet ornare?</a>
						</li>
						<li>
							<a href="#">Aliquam lorem ipsum</a>
						</li>
						<li>
							<a href="#">Ipsum pulvinar neque gravida aliquam</a>
						</li>
						<li>
							<a href="#">Blandit purus lectus sed semper</a>
						</li>
						<li>
							<a href="#">Lorem ipsum et dolor</a>
						</li>
						<li>
							<a href="#">Varius placerat amet consequat duis</a>
						</li>
						<li>
							<a href="#">Nulla purus cras amet aliquam nullam</a>
						</li>
						<li>
							<a href="#">Sodales mus et vitae</a>
						</li>
						<li class="last">
							<a href="#">Nisl mus nulla morbi</a>
						</li>
					</ul>
				</div>
				<div id="sidebar1">
					<h3>
						Curabitur ante
					</h3>
					<p>
						Sociis proin quisque id magna felis sed sapien. Primis vel varius nulla. Mollis sollicitudin.
					</p>
					<h3>
						Sed fermentum
					</h3>
					<ul>
						<li class="first">
							<a href="#">Lacinia amet et curae sed pellentesque</a>
						</li>
						<li>
							<a href="#">Vitae a nisi rhoncus sociis veroeros</a>
						</li>
						<li>
							<a href="#">Urna amet ornare?</a>
						</li>
						<li>
							<a href="#">Aliquam lorem ipsum</a>
						</li>
						<li>
							<a href="#">Ipsum pulvinar neque gravida aliquam</a>
						</li>
						<li>
							<a href="#">Blandit purus lectus sed semper</a>
						</li>
						<li>
							<a href="#">Lorem ipsum et dolor</a>
						</li>
						<li class="last">
							<a href="#">Varius placerat amet consequat duis</a>
						</li>
					</ul>
				</div>
				<br class="clear" />
			</div>
			<div id="footer">
				<div id="footerContent">
					<h3>
						Suspendisse non commodo
					</h3>
					<p>
						Nisl iaculis arcu cubilia vitae. Suspendisse proin enim feugiat aenean aliquet proin quam. Risus 
						placerat nisl sapien donec velit ornare cursus. Massa rhoncus fringilla eu aliquam. Facilisis orci 
						tristique iaculis ridiculus tellus. Odio nibh mauris velit nullam. Placerat hendrerit montes ligula 
						aenean cras. Eget augue tempus ipsum feugiat. Curae pellentesque penatibus dis velit. Augue felis 
						nisl vel natoque duis mollis diam. Nullam sollicitudin massa curabitur. Lorem ipsum dolor sit amet
						nullam consequat etiam arcu cubilia cursus massa eu aliquam. Orci tristique velit nullam sed
						etiam tellus odio nibh mauris.
					</p>
				</div>
				<div id="footerSidebar2">
					<h3>
						Turpis mus elit
					</h3>
					<ul>
						<li class="first">
							<a href="#">Felis duis aliquam</a>
						</li>
						<li>
							<a href="#">Convallis sed auctor</a>
						</li>
						<li>
							<a href="#">Blandit sed tempus</a>
						</li>
						<li class="last">
							<a href="#">Duis et hendrerit</a>
						</li>
					</ul>
				</div>
				<div id="footerSidebar1">
					<h3>
						Etiam mollis
					</h3>
					<ul>
						<li class="first">
							<a href="#">Sed lacinia cubilia</a>
						</li>
						<li>
							<a href="#">Risus euismod fusce</a>
						</li>
						<li>
							<a href="#">Malesuada molestie</a>
						</li>
						<li class="last">
							<a href="#">Felis dolore nullam</a>
						</li>
					</ul>
				</div>
			</div>
		</div>
		<div id="copyright">
				&copy; Your Site Name | Design by <a href="http://www.freecsstemplates.org/">FCT</a>
		</div>
	</body>
</html>





<body>
	<ul>
	<li><a href="/">Home</a></li>
	<li><a href="/add">Add Entry</a></li>
	</ul>
	
	<div>
		${self.body()}
	</div>
</body>