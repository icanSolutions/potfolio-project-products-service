# test_integration_async.py
import asyncio
import aiohttp
import pytest
import os

PRODUCTS_SERVICE_URL = os.getenv('PRODUCTS_SERVICE_URL')
REVIEWS_SERVICE_URL = os.getenv('REVIEWS_SERVICE_URL')


async def wait_for_service(url, timeout=30):
    async with aiohttp.ClientSession() as session:
        for _ in range(timeout):
            try:
                async with session.get(url) as r:
                    if r.status < 500:
                        return True
            except:
                pass
            await asyncio.sleep(1)
    raise RuntimeError(f"Service {url} not available")

@pytest.mark.asyncio
async def test_products_and_reviews_connection():
    await asyncio.gather(
        wait_for_service(f"{PRODUCTS_SERVICE_URL}/health"),
        wait_for_service(f"{REVIEWS_SERVICE_URL}/health")
    )

    async with aiohttp.ClientSession() as session:
        # Create a Product
        product_data = {"name": "Keyboard", "description": "Mechanical keyboard", "price": 49.99}
        async with session.post(f"{PRODUCTS_SERVICE_URL}/products", json=product_data) as res:
            assert res.status == 201
            product = await res.json()
            product_id = product["id"]

        # Create a Review for that Product
        review_data = {"user_name": "TestUser", "product_id": product_id, "rating": 5, "comment": "Great!"}
        async with session.post(f"{REVIEWS_SERVICE_URL}/reviews", json=review_data) as res:
            assert res.status == 201
            review = await res.json()
            assert review["product_id"] == product_id

        # Delete the Product
        async with session.delete(f"{PRODUCTS_SERVICE_URL}/products/{product_id}") as res:
            assert res.status == 204

        # Check that the Review is deleted 
        async with session.get(f"{REVIEWS_SERVICE_URL}/reviews/{review['id']}") as res:
            assert res.status == 404  