#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2024 Runxi Yu <https://runxiyu.org/>
# Upstream: https://git.sr.ht/~runxiyu/dsgit

from __future__ import annotations
import typing
import time
import os
import json
import sys
import traceback
import pathlib
import tempfile
import shutil
import datetime
import zoneinfo

import flask
import werkzeug
import werkzeug.middleware.proxy_fix

response_t: typing.TypeAlias = typing.Union[werkzeug.Response, flask.Response, str]

VERSION = """dsgit v0.1

License: GNU Affero General Public License v3.0 or later
URL: https://sr.ht/~runxiyu/dsgit"""

URL_PREFIX = "/"

bp = flask.Blueprint('dsgit', __name__, url_prefix=URL_PREFIX)

@bp.route("/", methods=["GET"])
def index():
    return flask.Response("Hello", mimetype="text/plain")


def makeapp() -> flask.Flask:
    app = flask.Flask(__name__)
    app.wsgi_app = werkzeug.middleware.proxy_fix.ProxyFix(  # type: ignore
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )
    app.register_blueprint(bp)
    # app.config["MAX_CONTENT_LENGTH"] = MAX_REQUEST_SIZE
    # app.config["SESSION_TYPE"] = "filesystem"
    return app


# use app.register_blueprint(bp, url_prefix="/something/") when importing externally

if __name__ == "__main__":
    makeapp().run(port=8080, debug=True)
