# About this site



Christina Koch's blog, a subpage of http://christinalk.github.io.



# About pelican



* What you need:


	pip install pelican markdown

	pip install ghp-import



See: https://github.com/getpelican/pelican and https://github.com/davisp/ghp-import

* Site install: Make directory + corresponding github repo for blog 
content.  From that directory run `pelican-quickstart`.  


See: http://docs.getpelican.com/en/3.4.0/quickstart.html


* Produce: Write posts in markdown in the `content` folder.  Use 
yaml-like headers. 


See: http://docs.getpelican.com/en/3.4.0/content.html and http://assemble.io/docs/YAML-front-matter.html


* Publish: Run the following sequence to publish (I turned this into a 
bash 
script):


	pelican -o output -s pelicanconf.py

	ghp-import output

	git push origin gh-pages



See: http://docs.getpelican.com/en/3.4.0/tips.html

* Themes: `pelican-themes` allows you to manage themes.  To add a theme, simply add `THEME = "theme name"` to the 
`pelicanconf.py` file.  


See: http://docs.getpelican.com/en/3.4.0/settings.html#themes,  http://docs.getpelican.com/en/3.4.0/pelican-themes.html, and https://github.com/getpelican/pelican-themes
