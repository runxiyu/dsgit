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
import werkzeug.security
import werkzeug.middleware.proxy_fix

response_t: typing.TypeAlias = typing.Union[werkzeug.Response, flask.Response, str]

VERSION = """dsgit v0.1

License: GNU Affero General Public License v3.0 or later
URL: https://sr.ht/~runxiyu/dsgit"""

URL_PREFIX = "/_"

bp = flask.Blueprint("dsgit", __name__, url_prefix=URL_PREFIX, template_folder="dstmpl")


@bp.route("/", methods=["GET"])
def index() -> response_t:
    return flask.Response(flask.render_template("index.html"))


def makeapp() -> flask.Flask:
    app = flask.Flask(__name__)
    app.wsgi_app = werkzeug.middleware.proxy_fix.ProxyFix(  # type: ignore
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )

    # NOTE: All routes registered here should NOT be actually called in
    #       production (the web server acting as the reverse proxy should be
    #       configured to serve them as static files which would be much more
    #       efficient than passing it through flask); however please don't
    #       delete them as they are useful in development, and more importantly,
    #       because they make url_for work in templates.

    # TODO: I'll get the paths right when I learn how to use Flask's model for
    #       app configurations.

    @app.route("/", methods=["GET"])
    def external_index() -> response_t:
        return flask.send_from_directory("../dstest", "index.html")

    @app.route("/<path:path>", methods=["GET"])
    def external_path(path: str) -> response_t:
        joined_path = werkzeug.security.safe_join("../dstest", path)
        if not joined_path:
            return flask.Response("Illegal path", status=403)
        if os.path.isdir(joined_path):
            path = os.path.join(path, "index.html")
        return flask.send_from_directory("../dstest", path)

    @app.route(URL_PREFIX.rstrip("/") + "/static/<path:path>", methods=["GET"])
    def dsstatic(path: str) -> response_t:
        return flask.send_from_directory("dsstatic", path)

    app.register_blueprint(bp, url_prefix=URL_PREFIX)
    # It is not necessary to pass url_prefix here as the blueprint was
    # initialized with url_prefix, but I guess this reminds me when I try to
    # remember how to set the prefix when copying it into a production
    # environment.

    # app.config["MAX_CONTENT_LENGTH"] = MAX_REQUEST_SIZE
    # app.config["SESSION_TYPE"] = "filesystem"
    return app


if __name__ == "__main__":
    makeapp().run(port=8080, debug=True)
