# 📘 Assignment: APIs REST com FastAPI

## 🎯 Objetivo

Nesta tarefa, você irá aprender a construir uma API REST funcional usando o framework FastAPI do Python. Você criará endpoints para gerenciar uma lista de tarefas (To-Do list), implementando operações CRUD (Create, Read, Update, Delete) e compreendendo os princípios fundamentais das APIs REST.

## 📝 Tarefas

### 🛠️	Criar API Básica com FastAPI

#### Description
Crie uma aplicação FastAPI básica com endpoints para gerenciar uma lista de tarefas. A API deve permitir criar, listar, atualizar e deletar tarefas.

#### Requirements
Completed program should:

- Instalar e configurar FastAPI com uvicorn
- Criar um modelo de dados para Task usando Pydantic
- Implementar endpoint GET /tasks para listar todas as tarefas
- Implementar endpoint POST /tasks para criar uma nova tarefa
- Implementar endpoint GET /tasks/{task_id} para buscar uma tarefa específica
- Implementar endpoint PUT /tasks/{task_id} para atualizar uma tarefa
- Implementar endpoint DELETE /tasks/{task_id} para deletar uma tarefa
- Incluir documentação automática do Swagger UI
- Tratar erros apropriadamente (404 para tarefa não encontrada)

### 🛠️	Adicionar Validação e Recursos Avançados

#### Description
Melhore sua API adicionando validações de dados, status codes apropriados e recursos extras como filtros e paginação.

#### Requirements
Completed program should:

- Validar dados de entrada usando Pydantic (título obrigatório, descrição opcional)
- Retornar status codes HTTP apropriados (200, 201, 404, 422)
- Adicionar campo de status para tarefas (pendente, em progresso, concluída)
- Implementar filtro por status usando query parameters
- Adicionar timestamps de criação e atualização automáticos
- Incluir middleware para CORS se necessário
- Adicionar pelo menos 3 tarefas de exemplo na inicialização
- Documentar todos os endpoints com descrições claras