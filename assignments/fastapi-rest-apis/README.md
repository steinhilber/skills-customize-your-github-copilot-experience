# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI to practice route creation, request validation, and basic CRUD operations using an in-memory data store.

## 📝 Tasks

### 🛠️	Create the FastAPI App and Health Endpoint

#### Description
Set up a FastAPI application and create your first endpoint to confirm the server is running.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`.
- Add a `GET /health` endpoint that returns JSON like `{ "status": "ok" }`.
- Run the app locally with Uvicorn and confirm the endpoint responds successfully.


### 🛠️	Build Product Endpoints

#### Description
Create endpoints to manage a small product catalog in memory.

#### Requirements
Completed program should:

- Define a Pydantic model named `Product` with fields: `id`, `name`, `price`, and `in_stock`.
- Add `GET /products` to return all products.
- Add `POST /products` to create a new product and return it.


### 🛠️	Implement Update and Delete Behavior

#### Description
Finish your API by supporting update and delete operations and handling missing records clearly.

#### Requirements
Completed program should:

- Add `PUT /products/{product_id}` to update an existing product.
- Add `DELETE /products/{product_id}` to remove a product.
- Return `404` with a clear message when a product does not exist.
- Test all endpoints in `/docs` and verify expected status codes.
