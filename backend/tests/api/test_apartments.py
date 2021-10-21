import json

import pytest
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
        'start_price': 3000000,
        'status': 'for sale'
    }

    def mock_create_apartment(db, apartment_in):
        return return_data

    monkeypatch.setattr(crud, 'create_apartment', mock_create_apartment)

    response = client.post('/apartments/', data=json.dumps(test_data), )
    assert response.status_code == 201
    assert response.json() == return_data


@pytest.mark.parametrize(
    'payload, status_code',
    [
        [{
            'floor': 1,
            'number': 1,
            'area': 30.5,
            'rooms': 1,
            'classes': ['C балконом', 'С отделкой'],
        }, 422],
        [{
            'floor': 'one',
            'number': 1,
            'area': 30.5,
            'rooms': 1,
            'classes': ['C балконом', 'С отделкой'],
            'start_price': 3000000
        }, 422],
    ]
)
def test_create_apartment_invalid_json(client: TestClient, payload, status_code):
    response = client.post('/apartments/', data=json.dumps(payload))
    assert response.status_code == status_code


def test_read_apartment(client: TestClient, monkeypatch):
    test_data = {
        'floor': 1,
        'number': 34,
        'area': 30.5,
        'rooms': 1,
        'balcony': True,
        'finishing': True,
        'start_price': 3000000,
        'status': 'for sale'
    }

    def mock_read_apartment(db, number):
        return test_data

    monkeypatch.setattr(crud, 'read_apartment', mock_read_apartment)

    response = client.get('/apartments/34')
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


def test_read_all_apartments(client: TestClient, monkeypatch):
    test_data = [{
        'floor': 1,
        'number': 34,
        'area': 30.5,
        'rooms': 1,
        'balcony': True,
        'finishing': True,
        'start_price': 3000000,
        'status': 'for sale'
    }, {
        'floor': 1,
        'number': 35,
        'area': 40.5,
        'rooms': 2,
        'balcony': True,
        'finishing': False,
        'start_price': 5000000,
        'status': 'for sale'
    }, {
        'floor': 2,
        'number': 46,
        'area': 25,
        'rooms': 1,
        'balcony': False,
        'finishing': True,
        'start_price': 2500000,
        'status': 'for sale'
    }, {
        'floor': 2,
        'number': 49,
        'area': 30.5,
        'rooms': 1,
        'balcony': True,
        'finishing': True,
        'start_price': 3000000,
        'status': 'for sale'
    }
]

    def mock_read_all_apartments(db):
        return test_data

    monkeypatch.setattr(crud, 'read_all_apartments', mock_read_all_apartments)

    response = client.get('/apartments/')
    assert response.status_code == 200
    assert response.json() == test_data


def test_update_apartment(client: TestClient, monkeypatch):
    test_data = {
        'floor': 1,
        'number': 34,
        'area': 30.5,
        'rooms': 1,
        'balcony': True,
        'finishing': True,
        'start_price': 3000000,
        'status': 'for sale'
    }
    test_update_data = {
        'floor': 1,
        'number': 34,
        'area': 30.5,
        'rooms': 1,
        'balcony': True,
        'finishing': True,
        'start_price': 5000000,
        'status': 'for sale'
    }

    def mock_read_apartment(db, number):
        return test_data

    monkeypatch.setattr(crud, 'read_apartment', mock_read_apartment)

    def mock_update_apartment(db, apartment, floor, area, rooms, start_price, balcony, finishing):
        return test_update_data

    monkeypatch.setattr(crud, 'update_apartment', mock_update_apartment)

    response = client.put('/apartments/34/', data=json.dumps(test_update_data), )
    assert response.status_code == 200
    assert response.json() == test_update_data


@pytest.mark.parametrize(
    'number, payload, status_code',
    [
        [34, {}, 422],
        [34, {'floor': 1}, 422],
        [999, {
            'floor': 1,
            'number': 34,
            'area': 30.5,
            'rooms': 1,
            'balcony': True,
            'finishing': True,
            'start_price': 3000000,
            'status': 'for sale'
        }, 404],
        [34, {
            'floor': 'one',
            'number': 34,
            'area': 30.5,
            'rooms': 1,
            'balcony': True,
            'finishing': True,
            'start_price': 3000000,
            'status': 'for sale'
        }, 422],
        [34, {
            'floor': 1,
            'number': 34,
            'area': '',
            'rooms': 1,
            'balcony': True,
            'finishing': True,
            'start_price': 3000000,
            'status': 'for sale'
        }, 422],
        [0, {
            'floor': 1,
            'number': 34,
            'area': 30.5,
            'rooms': 1,
            'balcony': True,
            'finishing': True,
            'start_price': 3000000,
            'status': 'for sale'
        }, 422],
        [0, {
            'floor': 1,
            'number': 34,
            'area': 30.5,
            'rooms': 1,
            'balcony': True,
            'finishing': True,
            'start_price': 3000000,
            'status': 'wrong status'
        }, 422],
    ],
)
def test_update_apartment_invalid(client: TestClient, monkeypatch, number, payload, status_code):
    def mock_read_apartment(db, number):
        return None

    monkeypatch.setattr(crud, 'read_apartment', mock_read_apartment)

    response = client.put(f'/apartments/{number}/', data=json.dumps(payload), )
    assert response.status_code == status_code


def test_remove_apartment(client: TestClient, monkeypatch):
    test_data = {
        'floor': 1,
        'number': 34,
        'area': 30.5,
        'rooms': 1,
        'balcony': True,
        'finishing': True,
        'start_price': 3000000,
        'status': 'for sale'
    }

    def mock_read_apartment(db, number):
        return test_data

    monkeypatch.setattr(crud, 'read_apartment', mock_read_apartment)

    def mock_delete_apartment(db, number):
        return test_data

    monkeypatch.setattr(crud, 'delete_apartment', mock_delete_apartment)

    response = client.delete('/apartments/34/')
    assert response.status_code == 200
    assert response.json() == test_data


def test_remove_note_incorrect_id(client: TestClient, monkeypatch):
    def mock_read_apartment(db, number):
        return None

    monkeypatch.setattr(crud, 'read_apartment', mock_read_apartment)

    response = client.delete('/apartments/999/')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Apartment not found'

    response = client.delete('/apartments/0/')
    assert response.status_code == 422
