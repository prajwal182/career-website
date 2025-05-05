import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()

# Load from environment variable
db_url = os.environ.get("DATABASE_URL")




# Create an SQLAlchemy engine
engine = create_engine(db_url)


# You must have `mysql-connector-python` installed
# pip install mysql-connector-python

engine = create_engine(
    db_url,
    connect_args={
        "ssl_disabled": False  # Enforces SSL usage
    }
)


# Using engine.connect() to establish a connection
#with engine.connect() as conn:
    # Execute your query
#    result = conn.execute(text("SELECT * FROM jobs"))
    
#    result_dicts = []
#    for row in result.all():
#        result_dicts.append((row))
        
#    print(result_dicts)


# Function to load jobs from the database
def load_jobs_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in result.all():
        job_dict = dict(row._mapping)
        jobs.append(job_dict)
    return jobs
