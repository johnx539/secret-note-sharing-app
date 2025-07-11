from flask import Flask , render_template , request , redirect , url_for
import uuid
app = Flask(__name__)

secrets = dict()

@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":


        secret_note = request.form["secret_note"]

        secret_id = str(uuid.uuid4())  # Convert UUID to string
        secrets[secret_id] = secret_note  # Now key is also a string

        note_link = "https://secret-note-sharing-app.vercel.app/note/" + secret_id

        return render_template("share_note.html",note_link = note_link)

    return render_template("index.html")
@app.route("/note/<note_id>")
def access_note(note_id):
    # Check if note exists
    if note_id in secrets:
        message = secrets.pop(note_id)  # Deletes after viewing
        return render_template("show_note.html", check_message="exists", secret_note=message)
    else:
        return render_template("show_note.html", check_message="not_exist")
if __name__ == "__main__":
    app.run(debug=True)