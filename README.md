# DevElas

O **DevElas** é um projeto em desenvolvimento para divulgar oportunidades de tecnologia voltadas para mulheres.

## Funcionalidades

- Página inicial com apresentação do projeto e quantidade de vagas abertas.
- Mural com oportunidades de tecnologia em diferentes áreas e níveis.
- Filtro de vagas por modalidade.
- Página de detalhes para cada oportunidade.
- Páginas sobre o projeto e contato.
- Cálculo da compatibilidade entre as skills da vaga e as skills cadastradas no projeto.
- Identificação das skills necessárias que ainda não foram adquiridas.
- Indicação de vagas abertas ou encerradas conforme o prazo.

## Atualizações recentes

- Os dados das vagas passaram a ser armazenados no arquivo `vagas/vagas.csv`.
- Foram adicionadas novas vagas e mais informações sobre cada oportunidade.
- O mural permite filtrar oportunidades por modalidade.
- Foi criada uma página com detalhes de cada vaga.
- Foram adicionadas as páginas **Sobre** e **Contato**.
- Foram introduzidas regras reutilizáveis para compatibilidade de skills, skills faltantes e prazo das vagas.
- O layout foi atualizado com Bootstrap, um template base e componentes compartilhados.

## Tecnologias

- Python 3
- Django 4.2.7
- HTML
- CSS
- Bootstrap
- SQLite
- Arquivo CSV para os dados das vagas

## Rotas disponíveis

- `/` — página inicial
- `/vagas/` — mural de vagas
- `/vagas/<id>/` — detalhes da vaga
- `/sobre/` — informações sobre o projeto
- `/contato/` — página de contato
- `/admin/` — administração do Django

## Como executar localmente

1. Clone o repositório e entre na pasta:

   ```bash
   git clone https://github.com/karlaaasp/develas.git
   cd develas
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   ```

   Linux/macOS:

   ```bash
   source .venv/bin/activate
   ```

   Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Instale o Django:

   ```bash
   python -m pip install Django==4.2.7
   ```

4. Aplique as migrações e inicie o servidor:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Acesse:

   - [http://127.0.0.1:8000/](http://127.0.0.1:8000/) — página inicial
   - [http://127.0.0.1:8000/vagas/](http://127.0.0.1:8000/vagas/) — mural de vagas

## Estrutura do projeto

- `manage.py` — utilitário de administração do Django.
- `develas/` — configurações do projeto e definição das URLs.
- `vagas/` — aplicação principal.
- `vagas/views.py` — views e preparação dos dados exibidos pelas páginas.
- `vagas/regras.py` — regras de compatibilidade, skills faltantes e validade das vagas.
- `vagas/dados.py` — leitura das informações e skills configuradas no projeto.
- `vagas/vagas.csv` — base de dados das vagas em formato CSV.
- `vagas/templates/` — templates HTML das páginas.
- `vagas/static/` — arquivos estáticos, como CSS.
- `vagas/tests.py` — testes básicos das views e funcionalidades.

## Próximos passos

- Evoluir o cadastro e gerenciamento das vagas.
- Migrar os dados para o banco de dados Django.
- Ampliar os filtros e a busca por vagas.
- Adicionar novas funcionalidades de interação e contato.
