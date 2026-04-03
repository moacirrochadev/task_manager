from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Lista global em memória; cada tarefa: {"id", "texto", "feito"}
tasks: list[dict] = []
_next_id = 1


def adicionar_tarefa(texto: str) -> None:
    global _next_id
    texto = texto.strip()
    if not texto:
        return
    tasks.append({"id": _next_id, "texto": texto, "feito": False})
    _next_id += 1


def completar(task_id: int) -> None:
    for t in tasks:
        if t["id"] == task_id:
            t["feito"] = True
            break


@app.route("/")
def index():
    """Página principal: lista de tarefas + formulário para nova tarefa."""
    ordenadas = sorted(tasks, key=lambda t: (t["feito"], t["id"]))
    return render_template("index.html", tasks=ordenadas)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    adicionar_tarefa(request.form.get("texto", ""))
    return redirect(url_for("index"))


@app.route("/completar/<int:task_id>", endpoint="completar")
def redirecionar_apos_completar(task_id: int):
    completar(task_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
