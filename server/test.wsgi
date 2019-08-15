from time import sleep

import flask

app = flask.Flask(__name__)


@app.route("/delay/<int:amount>/<path:ignore>")
def delay(amount, ignore):
    sleep(amount)
    body = """\
Delayed: {}
""".format(amount)
    r = flask.make_response(body)
    return r


application = app