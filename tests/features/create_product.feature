Feature: Product creation

    Scenario: Successfully creating a new Product
        Given the API is ready
        When I send a POST request to /products with valid data
        Then I receive a 201 response with an ID

    Scenario: Successfully update a product
        Given A product exists
        When I send a PUT request to /products/<id> with valid data
        Then i receive a 200 response with an ID
    
    Scenario: Successfully delte a product
        Given A product exists
        When I send a DELETE request to /products/<id> 
        Then i receive a 204 response with an ID