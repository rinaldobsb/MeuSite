from typing import Dict, List

from flask import Blueprint, redirect, render_template

from data import dados_do_site
from sql.model_pag_inicial import ModelProjects

project_app = Blueprint("projetos", __name__, template_folder="templates", url_prefix="/projects")

@project_app.route("/")
def all_projects():
    projects: List[Dict] = ModelProjects("meusite.db").retrive_all_projects()
    dados = dados_do_site["projetos"]
    return render_template("projetos_home.html", projects=projects, dados=dados)

@project_app.route("/<int:id>")
def one_project(id):
    project: Dict = ModelProjects("meusite.db").retrive_one_project(id=id)
    dados = dados_do_site["projetos"]
    return render_template("project.html", project=project, dados=dados)