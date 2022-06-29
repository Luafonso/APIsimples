# Criando uma Api usando FastApi

from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"Item": "Camisa", "Preço unitário": 35.00, "Quantidades": 5},
    2: {"Item": "Calça", "Preço unitário": 120.00, "Quantidades": 8},
    3: {"Item": "Tênis", "Preço unitário": 200.00, "Quantidades": 6},
    4: {"Item": "Boné", "Preço unitário": 25.00, "Quantidades": 10},
}

@app.get("/")
def home():
    return {"Vendas": len(vendas)}


@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return "Id Venda não disponivel"
