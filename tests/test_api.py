
def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_event_not_found(client):
    response = client.get("/events/bingo-da-joana")
    assert response.status_code == 404


def test_post_question(client):
    response = client.post("/events/bingo-da-joana/questions", json={"content": "zoing ?"})
    assert response.status_code == 201
    assert response.json() == {"content": "zoing ?", "id": 1}


def test_get_items(client):
    for c in ["zoing ?", "boing ?"]:
        response = client.post("/events/bingo-da-joana/questions", json={"content": c})
        assert response.status_code == 201

    response = client.get("/events/bingo-da-joana")
    assert response.status_code == 200
    assert response.json() == {
        "name": "bingo-da-joana",
        "questions": [
            {"content": "zoing ?", "id": 1},
            {"content": "boing ?", "id": 2},
        ]
    }
