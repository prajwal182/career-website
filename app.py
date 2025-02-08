from flask import Flask, render_template, jsonify
from database import load_jobs_db

app = Flask(__name__)

@app.route("/")
def hello_tech():
    # Fetch jobs from the database
    jobs = load_jobs_db()
    return render_template('home.html', jobs=jobs, company_name='Tech')

@app.route("/api/jobs")
def job_lists():
    # Fetch jobs from the database and return as JSON
    jobs = load_jobs_db()  # Use the function to fetch jobs
    return jsonify(jobs)  # Return the list of jobs as JSON

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
