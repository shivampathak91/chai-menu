from fastapi import FastAPI
import uvicorn
from fastapi import Request

# app = FastAPI(
#   title = "swiggy order API",
#   description = (
#     "This is a simple API for swiggy order management."
#     "Handling the order management system for swiggy"),
#     version = "1.0.0",
#     docs_url = "/docs",
#     redoc_url="/redoc",
#     openapi_url = "/openapi.json")

app = FastAPI(
    title="swiggy order API",
    description=(
        "This is a simple API for swiggy order management. "
        "Handling the order management system for swiggy"
    ),
    version="1.0.0",
    openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
  """Root endpoint for the API."""
  # FASTAPI converts this into a JSON response automatically
  return {"message": "This is the about page."," status": "healthy"}

@app.get("/about")
def about():
  """About endpoint for the API."""
  return {
    "service": "swiggy order API",
    "team": "backend team",
    "region":"ap-south-1",
    "version": "1.0.2"}

@app.get("/orders")
def orders():
  """Orders endpoint for the API."""
  return {
    "orders":[
      {"id":1,"item":"paneer masala","status":"delivered"},
      {"id":2,"item":"paneer tikka","status":"preparing"},
      {"id":3,"item":"paneer butter masala","status":"delivered"}
    ] }

@app.get("/orders/status")
def order_status():
  """Get order status"""
  return {
    "total_today": 2_340_32,
    "top_city": "bengaluru"
  }

@app.get("/debug/request_info")
async def request_inf(request: Request):
  """Inspect the raw request object"""
  return {
    "request" : request.method,
    "url": str(request.url),
    "headers": dict(request.headers),
    "path_params" : request.path_params,
    "query_params": dict(request.query_params),
  }

@app.get(
  "/orders/active",
  summary="Get active orders",
  description=(
    "Get active orders."
    "This endpoint returns a list of active orders for the user."
  ),
  tags=["orders"],
  response_description="A list of active order objects.",
  deprecated= False,
)
def get_active_orders():
  """this returns active orders api"""
  return{
    "orders":[
      {"id": 1,
      "item":"matar paneer",
      "status":"out for delivery"}
    ]
  }


@app.get("/restaurants",tags=["restaurants"])
def list_restaurants():
  """restaurants endpoint for the API."""
  return{
    "restaurants": [
      {"test": "test"}
    ]
  }

@app.get("/restaurants/delhi",tags=["restaurants"])
def list_restaurants_delhi():
  """restaurants endpoint for the API."""
  return{
    "restaurants": [
      {"test": "test"}
    ]
  }