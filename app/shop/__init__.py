from flask import Blueprint

bp = Blueprint("shop", __name__)

from . import routes  # noqa: E402, F401