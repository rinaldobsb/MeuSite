from typing import Dict, List

from flask import Blueprint, redirect, render_template

from data import dados_do_site
from sql.model_pag_inicial import ModelBlog

blog_app = Blueprint("blog", __name__, template_folder="templates", url_prefix="/blog")

@blog_app.route("/")
def all_posts():
    posts: List[Dict] = ModelBlog("meusite.db").retrive_all_posts()
    dados = dados_do_site["blog"]
    return render_template("blog_home.html", posts=posts, dados=dados)

@blog_app.route("/<int:id>")
def one_post(id):
    post: Dict = ModelBlog("meusite.db").retrive_one_post(id=id)
    dados = dados_do_site["blog"]
    return render_template("post.html", post=post, dados=dados)