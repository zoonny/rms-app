from fastapi import FastAPI, HTTPException

app = FastAPI()

# 임시 데이터 저장소
items = {
    1: {"name": "Item 1", "description": "This is item 1"},
    2: {"name": "Item 2", "description": "This is item 2"},
}

# Read: 모든 아이템 조회
@app.get("/items/")
def read_items():
    return items

# Read: 특정 아이템 조회
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

# Create: 새로운 아이템 추가
@app.post("/items/")
def create_item(item_id: int, name: str, description: str):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = {"name": name, "description": description}
    return {"message": "Item created successfully", "item": items[item_id]}

# Update: 기존 아이템 수정
@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, description: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id]["name"] = name
    items[item_id]["description"] = description
    return {"message": "Item updated successfully", "item": items[item_id]}

# Delete: 특정 아이템 삭제
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted successfully"}
