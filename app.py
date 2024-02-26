from flask import Flask, render_template, request, jsonify
import json
from health_indicator import HealthIndicator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_health', methods=['POST'])
def calculate_health():
    data = request.get_json()
    health_indicator = HealthIndicator(data)
    overall_score, push_up_norm, pull_up_norm, squat_norm, fivekm_time_norm, crunches_norm = health_indicator.overall_score()
    result = {
        'overall_score': overall_score,
        'push_up': push_up_norm,
        'pull_up': pull_up_norm,
        'squat': squat_norm,
        'fivekm_time': fivekm_time_norm,
        'crunches': crunches_norm
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
