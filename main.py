from flask import Flask, render_template, send_file, request
from database import db,insert_contact

main = Flask(__name__)

@main.route("/")
def fun():
  jobs = db()
  return render_template('index.html', jobs=jobs)
  
@main.route('/download-resume')
def download_resume():
    resume_path = 'static/Dipin Dawadi Resume Fall 2023.pdf'
    return send_file(resume_path, as_attachment=True)
  
@main.route("/description/<id>")
def description(id):
  jobs = db()
  id=int(id)
  for job in jobs:
    if job['id'] == id:
      des=job['des']
      company=job['company']
      return render_template('description.html', des=des,company=company)
  return "Job not found"

@main.route("/form")
def form():
  return render_template("form.html")

@main.route("/submit-form", methods=["POST"])
def submit_form():
    name = request.form.get("name")
    email = request.form.get("emailAddress")
    message = request.form.get("message")

    if name and email:
        result = insert_contact(name, email, message)
        return result
    else:
        return "Name and email are required fields."


if __name__ == "__main__":
  main.run(host='0.0.0.0', debug=True, port=6564)
