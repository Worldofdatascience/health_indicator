from flask import Flask, render_template, request, jsonify
import json
from health_indicator import HealthIndicator
from flask_sqlalchemy import SQLAlchemy
import urllib.parse
from db_config import db_config

app = Flask(__name__, static_url_path='/static')


# Encode the password for use in the URI
encoded_password = urllib.parse.quote_plus(db_config['password'])

# Construct the database URI using the configuration dictionary
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{db_config['user']}:{encoded_password}@{db_config['host']}/{db_config['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class HealthIndicatorr(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    week_number = db.Column(db.Integer)
    current_date_now = db.Column(db.DateTime)
    overall_score = db.Column(db.Float)
    push_up = db.Column(db.Float)
    pull_up = db.Column(db.Float)
    squat = db.Column(db.Float)
    fivekm_time = db.Column(db.Float)
    crunches = db.Column(db.Float)
    push_up_norm = db.Column(db.Float)
    pull_up_norm = db.Column(db.Float)
    squat_norm = db.Column(db.Float)
    fivekm_time_norm = db.Column(db.Float)
    crunches_norm = db.Column(db.Float)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_health', methods=['POST'])
def calculate_health():
    data = request.get_json()
    health_indicator = HealthIndicator(data)
    result = health_indicator.overall_score()

    return jsonify(result)


@app.route('/add_to_data', methods=['POST'])
def add_to_data():
    data = request.get_json()
    health_indicator = HealthIndicator(data)
    result = health_indicator.overall_score()

    health_indicator = HealthIndicatorr(
        overall_score=result['overall_score'],
        push_up_norm=result['push_up_norm'],
        pull_up_norm=result['pull_up_norm'],
        squat_norm=result['squat_norm'],
        fivekm_time_norm=result['fivekm_time_norm'],
        crunches_norm=result['crunches_norm'],
        current_date_now = result['current_date'],
        week_number = result['week_number'],
        push_up = data['push_up'],
        pull_up = data['pull_up'],
        squat = data['squat'],
        crunches = data['crunches'],
        fivekm_time = data['fivekm_time']
    )

    db.session.add(health_indicator)
    db.session.commit()
    result = jsonify({'success': True})

    return result


@app.route('/display_database', methods=['POST'])
def displayDatabase():
    # Retrieve all records from the HealthIndicatorr table
    result = HealthIndicatorr.query.all()

    # Convert SQLAlchemy model instances to dictionaries
    result = [
        {
            'id': item.id,
            'week_number': item.week_number,
            'current_date_now': item.current_date_now.isoformat() if item.current_date_now else None,
            'overall_score': item.overall_score,
            'push_up': item.push_up,
            'pull_up': item.pull_up,
            'squat': item.squat,
            'fivekm_time': item.fivekm_time,
            'crunches': item.crunches,
            'push_up_norm': item.push_up_norm,
            'pull_up_norm': item.pull_up_norm,
            'squat_norm': item.squat_norm,
            'fivekm_time_norm': item.fivekm_time_norm,
            'crunches_norm': item.crunches_norm
        }
        for item in result
    ]

    # Return the result as JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
