import logging

from flask import Flask
from flask import abort, jsonify
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.utils import redirect

from conf.config import LOGFILE_PATH
from redirect.controller.redis_urls import get_hash
from redirect.controller.redis_urls import get_url

app = Flask(__name__, static_url_path='/static')
app.config.from_object("conf.config")


@app.route('/')
def index():
    """Main form."""

    return render_template('index.html')


@app.route('/get_new_url/', methods=['POST'])
def get_new_url():
    """Method for getting new url for user-given url."""

    user_url = request.form.get('url', '')
    if len(user_url.strip()) == 0:
        return jsonify({'error': u'Enter url firstly…'})

    _hash = get_hash(user_url)
    new_url = url_for('.redirect_',
                      url_hash=_hash,
                      _external=True)

    return jsonify({'new_url': new_url})


@app.route('/redirect/<url_hash>', methods=['GET'])
def redirect_(url_hash):
    url = get_url(url_hash)
    if url is None:
        abort(404)

    return redirect(url)
