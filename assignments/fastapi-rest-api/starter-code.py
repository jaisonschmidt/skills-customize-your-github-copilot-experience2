# FastAPI To-Do List API - Starter Code
# Instale as dependências: pip install fastapi uvicorn

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum

# Criar instância da aplicação FastAPI
app = FastAPI(
    title="To-Do List API",
    description="Uma API REST simples para gerenciar tarefas",
    version="1.0.0"
)

# Enum para status das tarefas
class TaskStatus(str, Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"

# Modelo Pydantic para Task
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.PENDENTE
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# Modelo para atualização de tarefas (sem id)
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None

# Armazenamento em memória (lista simples)
tasks_db: List[Task] = []
next_id = 1

# Dados iniciais de exemplo
def initialize_sample_data():
    global next_id
    sample_tasks = [
        Task(
            id=1,
            title="Aprender FastAPI",
            description="Estudar os conceitos básicos do framework FastAPI",
            status=TaskStatus.EM_PROGRESSO,
            created_at=datetime.now(),
            updated_at=datetime.now()
        ),
        Task(
            id=2,
            title="Criar API REST",
            description="Implementar endpoints CRUD para gerenciar tarefas",
            status=TaskStatus.PENDENTE,
            created_at=datetime.now(),
            updated_at=datetime.now()
        ),
        Task(
            id=3,
            title="Testar endpoints",
            description="Usar Swagger UI para testar todos os endpoints",
            status=TaskStatus.PENDENTE,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
    ]
    tasks_db.extend(sample_tasks)
    next_id = 4

# Inicializar dados de exemplo na inicialização
initialize_sample_data()

# TODO: Implementar os endpoints abaixo

@app.get("/")
def read_root():
    """Endpoint raiz da API"""
    return {"message": "Bem-vindo à To-Do List API!"}

# TODO: Implementar GET /tasks - Listar todas as tarefas (com filtro opcional por status)
# Dica: Use Query parameter para filtro opcional

# TODO: Implementar POST /tasks - Criar nova tarefa
# Dica: Use datetime.now() para timestamps e incremente next_id

# TODO: Implementar GET /tasks/{task_id} - Buscar tarefa por ID
# Dica: Raise HTTPException(404) se não encontrar

# TODO: Implementar PUT /tasks/{task_id} - Atualizar tarefa
# Dica: Atualize apenas campos fornecidos e updated_at

# TODO: Implementar DELETE /tasks/{task_id} - Deletar tarefa
# Dica: Remova da lista e retorne confirmação

# Para executar: uvicorn main:app --reload
# Swagger UI: http://localhost:8000/docs