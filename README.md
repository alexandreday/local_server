## Description
Portable Python 3 script (Mac OS/Linux) for running a local server and visualizing a website/html page. Once
the page is generated, the server is shutdown and cleaned. This allows for rapid reuse for modifications or for generating another independent
website.

## Example of use:
Suppose you have the following directory structure:
```
website/
       index.html
       style/
            style.css
```
To render the website, copy `custom_server.py`to the `website/` directory and run the following command
from within that directory:
```
python custom_server.py
```
This should open up your browser and render your website. If you use something different than `index.html`, you can
alternatively use:
```
python custom_server.py foo.html
```
If you want to render `foo.html`.
