from flask import Flask, render_template, request, redirect, flash, url_for
from models import db, Info
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            name = request.form['name']
            rate = float(request.form['rate'])
            gst = float(request.form['gst'])
            net_rate = float(request.form['net_rate'])
            mrp = float(request.form['mrp'])

            item = Info(name, rate, gst, net_rate, mrp)
            db.session.add(item)
            db.session.commit()
            flash("Entry has been created successfully!", "success")
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
        return redirect(url_for("index"))
    return render_template("index.html")

@app.route("/view", methods=["GET"])
def view():
    query = request.args.get("q", "").strip()
    if query:
        items = Info.query.filter(Info.name.ilike(f"%{query}%")).all()
    else:
        items = Info.query.all()
    return render_template("view.html", items=items, search_query=query)

if __name__ == "__main__":
    app.run(debug=True)