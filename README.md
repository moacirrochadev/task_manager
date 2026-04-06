# Planner de Tarefas

Aplicação web simples para gerenciar uma lista de tarefas: adicionar itens, marcar como concluídos, limpar a lista e visualizar tarefas pendentes antes das concluídas. Projeto pensado para estudo de **Flask**, **rotas**, **templates Jinja2**, **formulários** e interface responsiva.

## Funcionalidades

- Página principal com lista de tarefas e formulário de nova tarefa
- Ordenação: tarefas **não concluídas** aparecem antes das **concluídas**
- Conclusão de tarefa por link (rota com `id`)
- Limpeza da lista inteira (POST dedicado)
- Interface com **CSS3**, fonte **Inter**, ícones **Lucide** (bundle local em `static/js/`) e **favicon** SVG
- Layout **responsivo**, com ajustes para telas até **414px** de largura (referência iPhone XR em portrait) e suporte a **áreas seguras** (`safe-area-inset`) quando o viewport usa `viewport-fit=cover`

## Particularidades

- **Dados apenas em memória:** ao reiniciar o servidor Flask, a lista de tarefas é perdida. Não há banco de dados neste projeto.
- Cada tarefa é um dicionário com `id` (incremental), `texto` e `feito`.
- O SEO básico da página principal está configurado no template (`title`, `meta description`, estrutura de cabeçalhos).

## Requisitos

- **Python 3.10+** (recomendado 3.12)
- `pip` para instalar dependências

## Como baixar e rodar em outro computador

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

Substitua a URL pelo endereço real do seu repositório no GitHub.

### 2. Criar e ativar um ambiente virtual (recomendado)

**Linux e macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
python app.py
```

Ou, com o interpretador explícito:

```bash
python3 app.py
```

Abra no navegador: **http://127.0.0.1:5000**

Com `debug=True` (como está em `app.py`), o servidor recarrega automaticamente ao alterar o código; em produção use um servidor WSGI adequado e desative o modo debug.

## Estrutura principal do projeto

```
task_manager/
├── app.py                 # Aplicação Flask e rotas
├── requirements.txt       # Dependências Python
├── README.md
├── static/
│   ├── style.css
│   ├── favicon.svg
│   └── js/
│       └── lucide.min.js  # Ícones Lucide (UMD)
└── templates/
    └── index.html         # Template Jinja2 da página principal
```

## Rotas

| Método | Caminho | Descrição |
|--------|---------|-----------|
| GET | `/` | Lista ordenada + formulário de nova tarefa |
| POST | `/adicionar` | Adiciona tarefa (campo `texto`) e redireciona para `/` |
| GET | `/completar/<id>` | Marca tarefa como concluída e redireciona para `/` |
| POST | `/limpar` | Remove todas as tarefas e reinicia os IDs |

## Licença

Defina a licença do repositório no GitHub e, se desejar, adicione um arquivo `LICENSE` na raiz do projeto.
