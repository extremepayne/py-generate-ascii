# py-generate-ascii

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) ![GitHub top language](https://img.shields.io/github/languages/top/extremepayne/HighScor.svg) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![Travis CI build](https://travis-ci.org/extremepayne/py-generate-ascii.svg?branch=master)](https://travis-ci.org/extremepayne/py-generate-ascii)

> Generates Ascii art from grayscale image


## Overview 
This repo isd a tool to transform an image into ASCII art. Follow these steps to generate the art:
1. Choose an image
2. See the section below "How to create a suitable image" and change the image as shown to make it easier for the generator to generate good art.
3. Save that changed image as a png.
4. Run main.py
5. Input the path to your image
6. Open `output.txt` with notepad or a similar application and follow the steps in the section "Viewing the completed art" to change the font to courier.
7. Yay! You did it!

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

In fact, you may want to change the aspect ratio of the image since courier characters aren't square.

[Change it into a png](https://onlinepngtools.com/convert-jpg-to-png):

![Small pixelated grayscale image (png)](images/python-pix-small.png)

Finally, with a [transparent background](https://onlinepngtools.com/create-transparent-png) (you will want to lower the "match similar colors" percentage, I used 2.5%):

![Transparent background small pixelated grayscale image](images/python-pix-sm-transparent.png)
