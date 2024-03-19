import tomllib
from typing import Dict

with open("configs.toml", "rb") as f:
    dados_do_site: Dict = tomllib.load(f)