from flask import jsonify,g
from app import db
from app.api import bp
from app.api.auth import basic_auth,token_auth

@bp.route('/tokens',methods=['POST'])
@basic_auth.login_required
def get_token():
    token = g.current_user.get_token()
    db.session.commit()
    return jsonify({'token':token})

# 撤销token
@bp.route('/tokens',methods=['DELETE'])
@token_auth.login_required
def revoken_token():
    g.current_user.revoke_token()
    db.session.commit()
    return '',204