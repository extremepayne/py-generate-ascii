# py-generate-ascii

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![Travis CI build](https://travis-ci.org/extremepayne/py-generate-ascii.svg?branch=master)](https://travis-ci.org/extremepayne/py-generate-ascii)

> Generates Ascii art from grayscale image


## This is a work in progress
So it dosen't work yet.

## Viewing the completed art
Be sure to use Courier. You can view text in courier like this (on a windows computer):


![Win7 Notepad Format->font](images/Notepad1.JPG)
![Win7 Notepad change font to Courier](images/Notepad2.JPG)

## How to create a suitable image
Any image *should* work, but it's best if you make your image the right size and format first. Below is an example along with links to online tools that do these things, you could probably find similar tools in an advanced photo editor (but I didn't bother because I'm not into advanced photo editing).

If you have an idea for how to automate these as part of the program, PRs are welcome!

Start with an image like the one below:

![full color image](images/python-full-color.jpg)

Then [make it grayscale](https://onlinejpgtools.com/convert-jpg-to-grayscale), like so:

![grayscale image](images/python.jpg)

[Pixelate it](https://pinetools.com/pixelate-effect-image) (here I used 8-wide pixels):

![Pixelated grayscale image](images/python-pixelated.jpg)

[Resize it](https://onlinejpgtools.com/resize-jpg) so the large pixels are now 1 pixel (so this 400 pixel wide image is resized to 50 wide in our case, since we used 8-wide pixels):

![Small pixelated grayscale image](images/python-pix-small.jpg)

[Change it into a png](https://onlinepngtools.com/convert-jpg-to-png):

![Small pixelated grayscale image (png)](images/python-pix-small.png)

Finally, with a [transparent background](https://onlinepngtools.com/create-transparent-png):

![Transparent background small pixelated grayscale image](images/python-pix-sm-transparent.png)
