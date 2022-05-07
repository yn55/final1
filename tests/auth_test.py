from flask_login import test_client


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_auth_pages(client):
    """This makes the index page"""
    response = client.get("/dashboard")
    assert response.status_code == 302
    response = client.get("/register")
    assert response.status_code == 200
    response = client.get("/login")
    assert response.status_code == 200



def test_upload_csvfile(client):
    file = "transactions.csv"
    data = {
        'image': (open(file, 'rb'), file)
    }
    response = client.post('/uploads', data=data)
    assert response.status_code == 404
