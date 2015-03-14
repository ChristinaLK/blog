## About this site

Christina Koch's [blog][blog-link], a subpage of http://christinalk.github.io.

Powered by [pelican][pelican], currently using the [pelipress][pelipress] theme.  

[blog-link]: http://christinalk.github.io/blog
[pelican]: https://github.com/getpelican/
[pelipress]: https://github.com/jjimenezlopez/pelipress

## About publishing with pelican

#### Install tools

Install pip (python package installer) if it isn't already.  Then run: 

~~~
pip install pelican markdown 
pip install ghp-import
~~~
	
[[pelican markdown]][pelican]
[[ghp-import]][ghp-import]
	
[pelican]: https://github.com/getpelican/pelican
[ghp-import]: https://github.com/davisp/ghp-import

####Create site

Make directory on local computer, link to corresponding github repo.  From that directory run `pelican-quickstart`.  [[Documenation]][quickstart]  

[quickstart]: http://docs.getpelican.com/en/3.4.0/quickstart.html

#### Create content

Write posts in markdown in the `content` folder. [[Documentation]][content]  Use 
yaml-like headers. [[yaml list]][yaml]

[content]: http://docs.getpelican.com/en/3.4.0/content.html
[yaml]: http://assemble.io/docs/YAML-front-matter.html

####Publish content

Run the following sequence to publish [[Documentation]][tips] (I turned this into a 
bash script [[here]][bash]).  This assumes your github repo is `origin`:

~~~
	pelican -o output -s pelicanconf.py
	ghp-import output
	git push origin gh-pages
~~~

The pelican command runs through the `content` directory, rendering the markdown source files into html in the `output` directory.  `ghp-import` takes care of committing these html files to your `gh-pages` branch.  

[bash]: publish.sh
[tips]: http://docs.getpelican.com/en/3.4.0/tips.html

####Themes 

Pelican's theme documentation is [[here]][theme-docs]

Pelican has many community-made, ready-to-run themes [[here]][themes]  Download the repository of available themes with a recursive git clone.  
~~~
git clone --recursive https://github.com/getpelican/pelican-themes
~~~

There are two ways to iinstall and use themes.  
1. Simply add the path to the theme directory to the `pelicanconf.py` file.  
~~~
THEME = "path/to/theme_name"
~~~
2. Use the `pelican-themes` tool.  See [[documentation]][pelican-themes] or run `pelican-themes --help`.  Install a theme from a location (will save it in your themes-path) using the `-i` option, then simply put the name of the theme in the `pelicanconf.py` file.  
~~~
THEME = "theme_name"
~~~

[theme-docs]: http://docs.getpelican.com/en/3.4.0/settings.html#themes
[themes]: https://github.com/getpelican/pelican-themes
[pelican-themes]: http://docs.getpelican.com/en/3.4.0/pelican-themes.html

####Other miscellaney

The `ghp-import` command only commits to your `gh-pages` branch.  I commit all my original markdown source files to `master`, but have a `.gitignore` in the `master` branch that excludes the automatically generated `output` and `cache` folder, since those are being committed on `gh-pages`.  
