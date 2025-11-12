# UC3 — Django Static Blog/Empresa

Projeto didático de Blog no DJANGO: Admin, ORM, Models, Partials.

## Requisitos
- Python 3.11+
- venv
- pip

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
# acesse http://127.0.0.1:8000/admin/
```

## Conteúdo do projeto
- `blog/models.py` com nomes descritivos: `titulo`, `Descricao`, `esta_ativo`.
- Admin otimizado: filtros, busca, edição em lista, ações de publicar/despublicar.
- Templates com **partials**: `_navbar`, `_footer`, `_alert`, `_posts`.
- View de lista com filtro por termo e categoria e paginação.
- Configuração de `TIME_ZONE='America/Sao_Paulo'` e `LANGUAGE_CODE='pt-br'`.

## Fluxo recomendado
1. Crie categorias no admin.
2. Cadastre POST com `esta_ativo=False` para revisão.
3. Publique via ação do admin.



