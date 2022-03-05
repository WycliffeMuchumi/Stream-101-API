from flask import jsonify, make_response, request, abort
from app.api.channels import blueprint as channels
from app.api.channels.models.channels import Channels

"""
    Getting all channels
"""

@channels.route('/', methods = ['GET'])
def get():
    channels = Channels.query.all()
    return channels_schema.jsonify(channels), 200
  