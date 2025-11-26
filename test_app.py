from app import app

def test_home():
    responce=app.test_client().get("/home")
    assert responce.status_code==200
    assert responce.data=="hello prajwal"