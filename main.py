from fastapi import FastAPI,Query,HTTPException
from model import MenuItem, MenuResponse
from data import menu_items


app = FastAPI(
  title = "chai point menu API",
  description = "Read only API for chai point menu management. Handling the menu management system for chai point"
)

@app.get("/")
def root():
  """root endpoint for the menu api"""
  return{"message":"Welcome to the chai point menu API"}

# menu -> path
#  /menu?category=chai&available=true

@app.get("/menu", response_model =MenuResponse)
def get_menu(category:str | None = Query(None, description = "Filter by chai,stock or combo")):
  if category:
    filtered = [item for item in menu_items if item["category"] == category.lower()]
    if not filtered:
      raise HTTPException(status_code=404, detail=f"No menu items found for category:'{category}'")
    return MenuResponse(count=len(filtered), items=filtered)

  return MenuResponse(count=len(menu_items), items=menu_items)

@app.get("/menu/{item_id}", response_model=MenuItem)
def get_item(item_id: int):
  for item in menu_items:
    if item["id"] ==item_id:
      return item

  raise HTTPException(status_code=404, detail=f"Menu items with id {item_id} not found")