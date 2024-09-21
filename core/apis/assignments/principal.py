@app.route('/principal/assignments', methods=['GET'])
def list_principal_assignments():
    assignments = Assignment.query.filter(Assignment.state.in_(['SUBMITTED', 'GRADED'])).all()
    return jsonify({'data': [assignment.to_dict() for assignment in assignments]})
