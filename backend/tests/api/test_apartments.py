import json

from fastapi.testclient import TestClient

from backend import crud


def test_create_apartment(client: TestClient, monkeypatch):
    test_data = {
        'floor': 1,
        'number': 34,
        'area': 30.5,
        'rooms': 1,
        'classes': ['C балконом', 'С отделкой'],
        'start_price': 3000000
    }

    return_data = {
        'floor': 1,
        'number': 34,
        'area': 30.5,
        'rooms': 1,
        'balcony': True,
        'finishing': True,
        'start_price': 3000000
    }

    def mock_create_apartment(db, apartment_in):
        return return_data

    monkeypatch.setattr(crud, 'create_apartment', mock_create_apartment)

    response = client.post('/apartments/', data=json.dumps(test_data), )
    assert response.status_code == 201
    assert response.json() == return_data


def test_create_apartment_invalid_json(client: TestClient):
    wrong_test_data = {
        'floor': 1,
        'number': 1,
        'area': 30.5,
        'rooms': 1,
        'classes': ['C балконом', 'С отделкой'],
    }
    response = client.post("/apartments/", data=json.dumps(wrong_test_data))
    assert response.status_code == 422

    wrong_test_data = {
        'floor': 'one',
        'number': 1,
        'area': 30.5,
        'rooms': 1,
        'classes': ['C балконом', 'С отделкой'],
        'start_price': 3000000
    }

    response = client.post(
        '/apartments/', data=json.dumps(wrong_test_data)
    )
    assert response.status_code == 422


def test_read_apartment(client: TestClient, monkeypatch):
    test_data = {
        'floor': 1,
        'number': 34,
        'area': 30.5,
        'rooms': 1,
        'balcony': True,
        'finishing': True,
        'start_price': 3000000
    }

    def mock_read_apartment(db, number):
        return test_data

    monkeypatch.setattr(crud, 'read_apartment', mock_read_apartment)

    response = client.get("/apartments/34")
    assert response.status_code == 200
    assert response.json() == test_data


def test_read_apartment_incorrect_number(client: TestClient, monkeypatch):
    def mock_read_apartment(db, number):
        return None

    monkeypatch.setattr(crud, 'read_apartment', mock_read_apartment)

    response = client.get('/apartments/999')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Apartment not found'

    response = client.get('/apartments/0')
    assert response.status_code == 422
