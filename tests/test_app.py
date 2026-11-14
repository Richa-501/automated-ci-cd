from app import app

def test_homepage():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Welcome to My Flask Application!" in response.data

def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_version():
    response = app.test_client().get("/version")
    assert response.status_code == 200
    assert response.get_json() == {"version": "1.0.0"}
