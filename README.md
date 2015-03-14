# About this site

Christina Koch's blog, a subpage of http://christinalk.github.io.

# About publishing with pelican (notes for self)

* Install tools:

	pip install pelican markdown [1][pelican]

	pip install ghp-import [2][ghp-import]

[pelican]: https://github.com/getpelican/pelican
[ghp-import]: https://github.com/davisp/ghp-import

* Create site: Make directory on local computer, link to corresponding github repo.  From that directory run `pelican-quickstart`.  [3][quickstart]  

[quickstart]: http://docs.getpelican.com/en/3.4.0/quickstart.html

* Create content: Write posts in markdown in the `content` folder. [4][content]  Use 
yaml-like headers. [5][yaml]

[content]: http://docs.getpelican.com/en/3.4.0/content.html
[yaml]: http://assemble.io/docs/YAML-front-matter.html

* Publish content: Run the following sequence to publish [6][tips] (I turned this into a 
bash script [7][bash]).  This assumes your github repo is `origin`:

~~~
	pelican -o output -s pelicanconf.py
	ghp-import output
	git push origin gh-pages
~~~

The pelican command runs through the `content` directory, rendering the markdown source files into html in the `output` directory.  `ghp-import` takes care of committing these html files to your `gh-pages` branch.  

[bash]: publish.sh
[tips]: http://docs.getpelican.com/en/3.4.0/tips.html

* Themes: `pelican-themes` allows you to manage themes.  To add a theme, simply add `THEME = "theme name"` to the 

`pelicanconf.py` file.  

See: http://docs.getpelican.com/en/3.4.0/settings.html#themes,  http://docs.getpelican.com/en/3.4.0/pelican-themes.html, and https://github.com/getpelican/pelican-themes

* Other miscellaney: The `ghp-import` command only commits to your `gh-pages` branch.  
I commit all my original markdown source files to `master`, but have a `.gitignore` in the `master` branch that excludes the automatically generated `output` and `cache` folder, since those are being committed on `gh-pages`.  
