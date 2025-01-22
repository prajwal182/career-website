from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title':'Data Analyst',
        'location':'Bengluru',
        'salary':'Rs.12,00,000'
    },
    {
        'id': 2,
        'title':'Data Scientist',
        'location':'Bengluru',
        'salary':'Rs.10,00,000'
    },
    {
        'id': 3,
        'title':'Frontend Engg',
        'location':'Remote',
        
    },
    {
        'id': 4,
        'title':'Backend Engg',
        'location':'USA',
        'salary':'$120,000'
    }
]

@app.route("/")
def helloworld():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def job_lists():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
