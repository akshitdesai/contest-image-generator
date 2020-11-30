# contest-image-generator
Generate image from given data of competitve coding contest

## installation
1. [Install imgkit](https://pypi.org/project/imgkit/):
`pip install imgkit`

2. Install wkhtmltopdf:
* for Debian/Ubuntu:`sudo apt-get install wkhtmltopdf`
* for MacOSX: `brew install wkhtmltopdf`
* for Windows and other options: check [wkhtmltopdf homepage](http://wkhtmltopdf.org/) for binary installers or [wiki page](https://github.com/pdfkit/pdfkit/wiki/Installing-WKHTMLTOPDF).


## Run
run python code as:-

`python geneate-image.py -p codechef -n "April Long 2020" -t "7:30 PM" -d 31/12/2020 -du "10 days"`

for understanding command line args
`python geneate-image.py -h`

## output
<img src="https://github.com/codestromer/contest-image-generator/blob/main/April%20Long%202020.png" alt="" width="250"/>
