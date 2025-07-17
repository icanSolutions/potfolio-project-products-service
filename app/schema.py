from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from app.models import Product

class ProductSchema(SQLAlchemySchema):
    class Meta:
        model = Product
        load_instance = True  # Deserialize into SQLAlchemy model
        include_fk = True     # If using foreign keys

    id = auto_field(dump_only=True)
    name = auto_field(required=True)
    description = auto_field()
    price = auto_field(required=True)