from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

# Custom exception
class ProductNotFoundError(Exception):
    """Raised when a product is not found."""
    pass    

    ...

def register_error_handlers(app):
    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        """
        Handle schema validation errors from Marshmallow.
        """
        return jsonify({"errors": err.messages}), 400

    @app.errorhandler(404)
    def handle_not_found(err):
        """
        Handle 404 Not Found errors.
        """
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(500)
    def handle_internal_error(err):
        """
        Handle generic 500 Internal Server Errors.
        """
        return jsonify({"error": "An unexpected error occurred"}), 500

    @app.errorhandler(SQLAlchemyError)
    def handle_sqlalchemy_error(err):
        """
        Handle database errors.
        """
        return jsonify({"error": "A database error occurred"}), 500

    # Optional: catch all unhandled exceptions
    @app.errorhandler(Exception)
    def handle_unexpected_error(err):
        """
        Catch-all for unhandled exceptions.
        """
        return jsonify({"error": str(err)}), 500
    
    @app.errorhandler(ProductNotFoundError)
    def handle_product_not_found(err):
        return jsonify({"error": str(err)}), 404