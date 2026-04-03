from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Gestão de tarefas</h1><p>Esqueleto Flask — adicione rotas e templates aqui.</p>"


if __name__ == "__main__":
    app.run(debug=True)
