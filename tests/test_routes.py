import pytest
# from app import create_app
from app.models import db, Product
from factories import ProductFactory
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.drop_all()
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
    print(data)
    assert data['name'] == "Keyboard"
    assert response.status_code == 201
    print(response.get_data(as_text=True))
    with client.application.app_context():
        product_in_db = Product.query.filter_by(name="Keyboard").first()
        assert product_in_db is not None, "Product not found in DB"
        assert product_in_db.description == "Mechanical keyboard"
        assert product_in_db.price == 49.99
        print("Product exists in DB:", product_in_db)
    
    
def test_get_product(client):
    """Create new product and get it via /products/<id>"""
    product = ProductFactory()
    db.session.add(product)
    db.session.commit()
    res = client.get(f"/products/{product.id}")
    data = res.get_json()
    print(data)
    assert data['id'] == product.id
    assert data['name'] == product.name
    
def test_update_a_product(client):
    """Update a new product and test it product status code & name"""
    product = ProductFactory()
    db.session.add(product)
    db.session.commit()
    response = client.put(f"/products/{product.id}", json={
        "price": 50.99
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == product.name
    assert data['price'] == 50.99
    
def test_delete_product(client):
    product = ProductFactory()
    db.session.add(product)
    db.session.commit()
    prod_count = Product.query.count()
    assert prod_count == 1
    res = client.delete(f"/products/{product.id}")
    assert res.status_code == 204
    prod_after_count = Product.query.count()
    assert prod_after_count == 0
    
def test_list_products(client):
    names = []
    for _ in range(5):
        product = ProductFactory()
        names.append(product.name)
        
    db.session.commit()
    
    res = client.get("/products")
    data = res.get_json()
    
    assert len(data) == 5

    response_names = [p["name"] for p in data]
    assert set(response_names) == set(names)
    
    
            
