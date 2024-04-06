from datetime import date
from typing import Dict

from flask import Flask, render_template, url_for, render_template_string
import markdown

from blog.blog import blog_app
from data import dados_do_site
from projects.projects import project_app
from sql.model_pag_inicial import ModelBlog, ModelProjects

app = Flask(__name__)

@app.template_filter("transforma_data")
def transforma_data(isoformat):
    obj_data = date.fromisoformat(isoformat)
    return obj_data.strftime("%d/%m/%Y")

@app.template_filter("markdown")
def markdown_to_html(markdown_string):
    html = markdown.markdown(markdown_string)
    return html

@app.route('/')
def index():
    dados = dados_do_site["home"]
    projects = ModelProjects("meusite.db").return_3_projects()
    posts = ModelBlog("meusite.db").return_3_post()
    return render_template('index.html', dados=dados, projects=projects, posts = posts)


app.register_blueprint(project_app)
app.register_blueprint(blog_app)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 