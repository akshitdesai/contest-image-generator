import os
import imgkit
import argparse

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--platform", required=True, help = "Contest Platform for ex:- cc, cf, he, hr, sp")
parser.add_argument("-n", "--name", required=True, help = "Contest Name")
parser.add_argument("-t", "--time", required=True, help = "Contest Time for ex:- 7:30 PM")
parser.add_argument("-d", "--date", required=True, help = "Contest Date for ex:- 31/12/2020")
parser.add_argument("-du", "--duration", required=True, help = "Contest Duration, for ex:- 10 Days, 3 Hours")

HTML_FOR_IMAGE = """
<html>
	<head>
		<title>Home</title>
		<meta charset="utf-8" />
		<meta name="imgkit-format" content="png"/>
	</head>
	<body>
		<div class="bg-text">
            <img class="img"  src="{}/{}.png" height="110" width="110" alt="Host Photo">

            <h1 class="heading"> {} </h1>
            <p> <span class="gg"> Date 📅: </span> {} </p>
            <p> <span class="gg"> Time ⏰: </span> {} </p>
            <p> <span class="gg"> Duration ⌛: </span> {} </p>
            
            </br>

            <p> < ALL THE BEST > </p>
            <p> < HAPPY CODING > </p>
            

            <p class="footer">
                Contribute to Project:- 
                <a href="github.com/codestromer/">github.com/codestromer/contest-image-generator</a>
            </p>
        </div>
    </body>
</html>
"""

CSSFILE = "{}/main.css".format(BASE_DIR)

# Try diffrent height and width for desired output
OPTIONS = {'width': 400, 'height':1000}

if __name__ == "__main__":


	args = parser.parse_args()
	contest_host = args.platform
	contest_name = args.name
	contest_time = args.time
	contest_date = args.date
	contest_duration = args.duration

	HTML_FOR_IMAGE = HTML_FOR_IMAGE.format(BASE_DIR, 
									   contest_host.upper(),
									   contest_name, 
									   contest_date,
									   contest_time,
									   contest_duration)

	output_file_name = '{}.png'.format(contest_name)

	imgkit.from_string(HTML_FOR_IMAGE, output_file_name, options=OPTIONS, css = CSSFILE)