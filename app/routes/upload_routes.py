from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import datetime
from .. import db
from ..models.project import Project
import os

upload_bp = Blueprint('upload', __name__, url_prefix="/upload")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@upload_bp.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files.get("file")
        project_name = request.form.get("project_name")

        if not file or file.filename == "":
            flash("Nenhum arquivo selecionado!", "error")
            return redirect(url_for("upload.upload_file"))

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        new_project = Project(
            name=project_name,
            filename=file.filename,
            upload_date=datetime.now()
        )
        db.session.add(new_project)
        db.session.commit()

        flash("Upload realizado com sucesso!", "success")
        return redirect(url_for("upload.upload_file"))

    return render_template("upload.html")
