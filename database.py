from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://wf5ojfa99wphg56c2lr5:pscale_pw_3WqOz6FRTPcfXfVZr6xgehvF1wfEYoV2oOT45ZVSdxj@aws.connect.psdb.cloud/portfolio?charset=utf8mb4",
                      connect_args={
                        "ssl": {
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })

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
