python_react_app (Python/Django Framework/React)

A. API (Python/Django Framework)

List of products 
GET http://localhost:8000/api/v1/products/

Full text search 
GET http://localhost:8000/api/v1/products/?search=prod%201

Product CRUD
GET http://localhost:8000/api/v1/products/{id}/
<br />
POST http://localhost:8000/api/v1/products/new
<br />
PUT http://localhost:8000/api/v1/products/{id}/
<br />
DELETE http://localhost:8000/api/v1/products/{id}/

Swagger 
http://localhost:8000/api/docs/

DB 
db.sqlite3

Run
python manage.py runserver