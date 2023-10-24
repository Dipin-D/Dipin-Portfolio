import os
from sqlalchemy import create_engine, text

my_secret = os.environ['password']

db_url = f"mysql+pymysql://09s5bxg4wen2627y77py:{my_secret}@aws.connect.psdb.cloud/portfolio?charset=utf8mb4"

engine = create_engine(db_url, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})

def db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))

        jobs = []
        for row in result:
            job = row._asdict()
            jobs.append(job)

        return jobs

def insert_contact(name, email, message):
    with engine.connect() as conn:
        query = text("INSERT INTO contacts (name, email, message) VALUES (:name, :email, :message)")
        conn.execute(query, {"name": name, "email": email, "message": message})

    return "Form submitted successfully!"

if __name__ == "__main__":
    jobs = db()
