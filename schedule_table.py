from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class TimeFrame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timef = db.Column(db.String(256))
    monday = db.Column(db.String(256))
    tuesday = db.Column(db.String(256))
    wednesday = db.Column(db.String(256))
    thursday = db.Column(db.String(256))
    friday = db.Column(db.String(256))
    saturday = db.Column(db.String(256))


db.create_all()


@app.route('/')
def index():
    shed = TimeFrame.query
    return render_template('schedule_table.html', title='Table',
                           timefr=shed)


if __name__ == '__main__':
    app.run()
