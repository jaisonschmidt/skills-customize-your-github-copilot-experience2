# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes

## Padrão de Mensagens de Commit

Todas as mensagens de commit devem seguir o formato **Conventional Commits** para garantir histórico consistente e legível. Estrutura:

```
<tipo>(<escopo opcional>): <resumo curto no imperativo>

[corpo opcional explicando o porquê da mudança]

[rodapé opcional para issues ou BREAKING CHANGES]
```

Tipos principais aceitos:
- `feat`: nova funcionalidade
- `fix`: correção de bug
- `docs`: alteração de documentação (inclui README, comentários explicativos)
- `style`: mudanças que não afetam lógica (espaço, formatação, ponto e vírgula, CSS puramente estético)
- `refactor`: alteração interna sem adicionar feature nem corrigir bug
- `perf`: melhoria de performance
- `test`: adição ou ajuste de testes
- `build`: mudanças em build, dependências ou ferramentas (npm, pip, etc.)
- `ci`: ajustes de pipelines ou configs de integração contínua
- `chore`: tarefas diversas que não se encaixam nos demais (ex: ajustes menores)
- `revert`: reversão de commit anterior

Regras:
- Resumo com no máximo 72 caracteres, em português, modo imperativo (ex: "adiciona", "corrige", "atualiza").
- Usar escopo quando fizer sentido (ex: `feat(assignments): ...`). Escopo em `kebab-case`.
- Commits que introduzem quebra de compatibilidade devem incluir `!` após o tipo ou escopo e uma linha `BREAKING CHANGE:` no corpo explicando.
- Referências a issues no rodapé usando `Closes #123` ou `Refs #123`.

Exemplos:
```
feat(assignments): adiciona seção de próxima tarefa na página inicial

fix(script): corrige cálculo de próxima data de entrega quando não há tarefas futuras

docs: adiciona instruções de Conventional Commits ao guia do projeto

refactor(css): simplifica classes utilitárias de espaçamento

feat(config)!: reestrutura formato de assignments no config.json

BREAKING CHANGE: o campo "dueDate" agora é obrigatório e em formato ISO (YYYY-MM-DD)
```

Ao gerar múltiplos commits, agrupar mudanças coerentes e evitar commits gigantescos que misturem tipos diferentes.

Se a alteração for trivial (ex: trocar uma palavra em documentação) ainda assim usar o formato (`docs: corrige termo em README`).

Commits automáticos ou gerados pelo assistente devem seguir estritamente estas regras.

