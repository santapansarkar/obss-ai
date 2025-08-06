from flask import Flask, jsonify
from controllers.category_controller import CategoryController
from controllers.events_subscription_controller import EventsSubscriptionController
from controllers.export_job_controller import ExportJobController
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize controllers
category_controller = CategoryController()
events_subscription_controller = EventsSubscriptionController()
export_job_controller = ExportJobController()

@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(category_controller.get_all_categories())

@app.route('/events/subscription', methods=['POST'])
def subscribe_event():
    return jsonify(events_subscription_controller.subscribe_event()), 201

@app.route('/export/job', methods=['POST'])
def create_export_job():
    return jsonify(export_job_controller.create_export_job()), 201

if __name__ == '__main__':
    app.run(debug=True)