from .. import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    filename = db.Column(db.String(120), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False)
    ftp_status = db.Column(db.String(50), default='pending')

    def __repr__(self):
        return f"<Project {self.name}>"
