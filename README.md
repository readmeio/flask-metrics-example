# Flask Metrics Example

A tiny Flask app for testing API Metrics.

[![PyPi](https://img.shields.io/pypi/v/readme-metrics)](https://pypi.org/project/readme-metrics/)

[![](https://d3vv6lp55qjaqc.cloudfront.net/items/1M3C3j0I0s0j3T362344/Untitled-2.png)](https://readme.io)

> Disclaimer: My Python knowledge is abysmal so apologies in advance. This is assuming you're running macOS and that you're able to run the command `python3` in your terminal.

## Setup and Installation

> Mostly stolen from [the Flask docs](https://flask.palletsprojects.com/en/1.1.x/installation/)

Clone this repository! Once inside it, run the following to set up and activate your virtual environment and install your dependencies:
```
$ python3 -m venv venv
$ . venv/bin/activate
```

Next, install the dependencies (while still inside your virtual environment):
```
$ pip3 install Flask readme-metrics
```

Next, populate your [ReadMe Project API Key](https://docs.readme.com/developers/docs/authentication#api-key-quick-start) in `hello.py`.

Once you've done that, you'll need to tell your terminal the application to work with by exporting the `FLASK_APP` environment variable:
```
$ export FLASK_APP=hello.py
```

You're most likely running this in an environment where you'll want debug mode and development features! Simply set the `FLASK_ENV` variable:
```
$ export FLASK_ENV=development
```

## Starting The Web Server
And finally... start the Flask app!
```
$ python3 -m flask run
```

Now, simply send requests by going to http://127.0.0.1:5000 in your browser, or by running cURL commands like:
```
curl http://127.0.0.1:5000
curl -X POST http://127.0.0.1:5000
```