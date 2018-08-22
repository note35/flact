from flask import Blueprint, render_template  # type: ignore


base_blueprint = Blueprint('base', __name__)


@base_blueprint.route('/', methods=['GET'])
def main():
    return render_template(
        'index.html',
        title='Example',
        jsx_path='Base',
        components=['Navigator', 'Content'],
        common_components=['Footer']
    )
