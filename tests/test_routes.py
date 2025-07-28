import pytest
# from app import create_app
from app.models import db, Product
from factories import ProductFactory
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()
    
def test_create_a_product(client):
    """Create a new product and test the ststuse code & name"""
    response = client.post("/products", json={
        "name": "Keyboard",
        "description": "Mechanical keyboard",
        "price": 49.99
    })
    data = response.get_json()
    assert data['name'] == "Keyboard"
    assert response.status_code == 201
    print(response.get_data(as_text=True))
    
    
def test_get_product(client):
    """Create new product and get it via /products/<id>"""
    product = ProductFactory()
    res = client.get(f"/products/{product.id}")
    data = res.get_json()
    assert data['id'] == product.id
    assert data['name'] == product.name
    
def test_update_a_product(client):
    """Update a new product and test it product status code & name"""
    product = ProductFactory()
    response = client.put(f"/products/{product.id}", json={
        "price": 50.99
    })
    assert response.status_code == 200
    data = response.get_json()
    assert product.price != data['price']
    assert data['name'] == "Keyboard"
    assert data['price'] == 50.99
    
def test_delete_product(client):
    product = Product(name="Keyboard", description="Mechanical", price=49.99)
    prod_count = len(Product.all())
    assert prod_count == 1
    res = client.delete(f"/products/{product.id}")
    assert res.status_code == 204
    prod_after_count = len(Product.all())
    assert prod_after_count == 0
    
def test_list_products(client):
    names = []
    for i in range(5):
        product = ProductFactory()
        names.append(product.name)
    res = client.get(f"/products")
    data = res.get_json()
    products_count_after = len(data)
    assert products_count_after == 5
    assert data[0].name == names[0]
    assert data[4].name == names[4]
        
    
    
            
