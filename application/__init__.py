from flask import Flask
from application.config import db_config
import os

__author__ = 'leimiaomiao'

web_root = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))

app = Flask(
    __name__,
    static_folder=os.path.abspath(os.path.join(web_root, 'static')),
    static_url_path="",
    template_folder=os.path.abspath(os.path.join(web_root, 'templates'))
)

app.config.from_object(db_config)


