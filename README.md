# Meu Site em Flask

Para utiliza-lo: após clonar o repositório, preencha o arquivo config.toml com seus dados e instale o ambiente e dependências com o Poetry.
Crie um arquivo sqlite com o nome meusite.db e crie as seguintes tabelas:
## Tabela Projetos: 
'''SQL
CREATE TABLE "projetos" (
	"id"	INTEGER NOT NULL UNIQUE,
	"nome_projeto"	TEXT NOT NULL,
	"descricao_projeto"	TEXT,
	"link"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
)
'''

## Tabela Blog:
'''SQL
CREATE TABLE "blog" (
	"id"	INTEGER NOT NULL UNIQUE,
	"titulo_post"	TEXT NOT NULL,
	"texto_post"	TEXT,
	"resumo_post"	TEXT,
	"data"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)
'''
Os dados do "titulo_post" devem estar em Markdown.

Alimente com seus dados e ENJOY!

