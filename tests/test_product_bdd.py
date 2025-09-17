# import pytest
# from pytest_bdd import scenarios, given, when, then
# from app import create_app
# from app.models import db, Product

# scenarios('features/create_product.feature')


# @pytest.fixture
# def client():
#     app = create_app()
#     app.config['TESTING'] = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

#     with app.app_context():
#         db.create_all()
#         yield app.test_client()
            

# @given("the API is ready")
# def api_ready(client):
#     return client

# @when("I send a POST request to /products with valid data")
# def send_post_request(client):
#     response = client.post("/products", json={
#         "name": "Keyboard",
#         "description": "Mechanical keyboard",
#         "price": 49.99
#     })
#     client.last_response = response

# @then("I receive a 201 response with an ID")
# def check_response(client):
#     res = client.last_response
#     assert res.status_code == 201
#     data = res.get_json()
#     assert "id" in data
    
    
# @when("I send a PUT request to /products/<id> with valid data")
# def send_put_request(client):
#     """Send a PUT request to update a product"""
#     prod_id = client.product_id
#     response = client.put(f"/products/{prod_id}", json={
#         "price": 50.09
#     })
#     client.last_response = response
    
# @then("i receive a 200 response with an ID")
# def check_response(client):
#     res = client.last_response
#     assert res.status_code == 200
#     data = res.get_json()
#     assert "id" in data
    
# @given("A product exists")
# def an_exist_product(client):
#     """Create a product in the DB before the test."""
#     product = Product(name="Keyboard", description="Mechanical", price=49.99)
#     with client.application.app_context():
#         db.session.add(product)
#         db.session.commit()
#     client.product_id = product.id  # Save for use in other steps
    
# @when("I send a DELETE request to /products/<id>")
# def send_put_request(client):
#     """Send a DELETE request to delete a product"""
#     prod_id = client.product_id
#     response = client.delete(f"/products/{prod_id}")
#     client.last_response = response
    
# @then("i receive a 204 response with an ID")
# def check_delete_response(client):
#     res = client.last_response
#     assert res.status_code == 204
#     assert res.data == b''  # Response body should be empty