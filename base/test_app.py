from app import application

def test_home_page():

    # Create a test client using the Flask application configured for testing
    with application.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"This is a very basic example" in response.data

