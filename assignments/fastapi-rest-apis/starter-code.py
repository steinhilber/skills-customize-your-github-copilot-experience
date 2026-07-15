# Starter Code for Building REST APIs with FastAPI

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Product API")


class Product(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    in_stock: bool


# In-memory product storage for this assignment.
products: list[Product] = []


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/products", response_model=list[Product])
def list_products() -> list[Product]:
    return products


@app.post("/products", response_model=Product, status_code=201)
def create_product(product: Product) -> Product:
    products.append(product)
    return product


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product) -> Product:
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}")
def delete_product(product_id: int) -> dict[str, str]:
    for index, product in enumerate(products):
        if product.id == product_id:
            products.pop(index)
            return {"message": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")


# Run locally with:
# uvicorn starter-code:app --reload
