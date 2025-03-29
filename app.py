from flask import Flask, request, jsonify

app = Flask(__name__)


class Task:
    def __init__(self, id, title, description=""):
        self.id = id
        self.title = title
        self.description = description

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description}


tasks = []
task_id_control = 1

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/about")
def about():
    return "Página sobre"

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()

 
    if "title" not in data:
        return jsonify({"error": "Título é obrigatório!"}), 400

    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)


    return jsonify({"message": "Nova tarefa criada com sucesso", "task": new_task.to_dict()}), 201

if __name__ == "__main__":
    app.run(debug=True)
