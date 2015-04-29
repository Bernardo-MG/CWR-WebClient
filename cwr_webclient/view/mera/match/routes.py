# -*- encoding: utf-8 -*-
from flask import render_template, Blueprint, current_app


__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

mera_match_blueprint = Blueprint('mera_match', __name__,
                                 template_folder='templates')

REJECTED_EXTENSIONS = set(['html', 'htm', 'php'])

"""
Upload routes.
"""


@mera_match_blueprint.route('/<int:file_id>', methods=['GET'])
def result(file_id):
    match_service = current_app.config['MATCH_SERVICE']

    data = match_service.get_data(file_id)

    return render_template('mera_match.html', file_id=file_id, matches=data)
