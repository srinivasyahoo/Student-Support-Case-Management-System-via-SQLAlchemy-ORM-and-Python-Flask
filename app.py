import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# SQLALCHEMY_DATABASE_URI: The database URI to specify the database you want to establish a connection with
app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'support_service.db')

# SQLALCHEMY_TRACK_MODIFICATIONS: A configuration to enable or disable tracking modifications of objects.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database table for Student Support Requests represented by a model
class SupportRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Support Request ID
    student_id = db.Column(db.String(50), nullable=False)
    student_name = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    support_category = db.Column(db.String(50), nullable=False)  # Academic, Financial, Wellbeing, etc.[cite: 1]
    support_request_description = db.Column(db.Text, nullable=False)
    submission_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    case_status = db.Column(db.String(50), nullable=False, default='New')  # New, In Progress, Awaiting Student, Closed[cite: 1]
    internal_staff_notes = db.Column(db.Text)
    last_updated_date = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    assigned_support = db.Column(db.String(100))

    def __repr__(self):
        return f'<SupportRequest {self.id} - {self.student_name}>'


@app.route('/')
def index():
    support_requests = SupportRequest.query.all()
    return render_template('index.html', support_requests=support_requests)


@app.route('/<int:request_id>/')
def support_request_detail(request_id):
    support_request = SupportRequest.query.get_or_404(request_id)
    return render_template('support_request.html', support_request=support_request)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == "POST":
        student_id = request.form['student_id']
        student_name = request.form['student_name']
        course = request.form['course']
        support_category = request.form['support_category']
        support_request_description = request.form['support_request_description']
        case_status = request.form.get('case_status', 'New')
        internal_staff_notes = request.form.get('internal_staff_notes', '')
        assigned_support = request.form.get('assigned_support', '')

        support_req = SupportRequest(
            student_id=student_id,
            student_name=student_name,
            course=course,
            support_category=support_category,
            support_request_description=support_request_description,
            case_status=case_status,
            internal_staff_notes=internal_staff_notes,
            assigned_support=assigned_support
        )
        db.session.add(support_req)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:request_id>/edit/', methods=('GET', 'POST'))
def edit(request_id):
    support_request = SupportRequest.query.get_or_404(request_id)

    if request.method == 'POST':
        support_request.student_id = request.form['student_id']
        support_request.student_name = request.form['student_name']
        support_request.course = request.form['course']
        support_request.support_category = request.form['support_category']
        support_request.support_request_description = request.form['support_request_description']
        support_request.case_status = request.form['case_status']
        support_request.internal_staff_notes = request.form['internal_staff_notes']
        support_request.assigned_support = request.form['assigned_support']

        db.session.add(support_request)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', support_request=support_request)


@app.post('/<int:request_id>/delete/')
def delete(request_id):
    support_request = SupportRequest.query.get_or_404(request_id)
    db.session.delete(support_request)
    db.session.commit()
    return redirect(url_for('index'))