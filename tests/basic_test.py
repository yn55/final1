"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/about"' in response.data

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/student"' in response.data


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/welcome"' in response.data

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/register"' in response.data
    assert b"Register" in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index" in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data

def test_request_welcome(client):
    """This makes the index page"""
    response = client.get("/welcome")
    assert response.status_code == 200

def test_request_welcome(client):
    """This makes the index page"""
    response = client.get("/welcome")
    assert b"welcome" in response.data

def test_request_student(client):
    """This makes the index page"""
    response = client.get("/student")
    assert response.status_code == 200
    assert b"student" in response.data

def test_request_class1(client):
    """This makes the index page"""
    response = client.get("/class1")
    assert response.status_code == 200
    assert b"class1" in response.data

def test_request_class2(client):
    """This makes the index page"""
    response = client.get("/class2")
    assert response.status_code == 200
    assert b"class2" in response.data

def test_request_class3(client):
    """This makes the index page"""
    response = client.get("/class3")
    assert response.status_code == 200
    assert b"class3" in response.data

def test_request_class4(client):
    """This makes the index page"""
    response = client.get("/class4")
    assert response.status_code == 200
    assert b"class4" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404

