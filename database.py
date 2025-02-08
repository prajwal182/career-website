from sqlalchemy import create_engine, text

# Define your database connection URL
# Replace the placeholders with your actual database credentials
db_url = "xyz"

# Create an SQLAlchemy engine
engine = create_engine(db_url)

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
