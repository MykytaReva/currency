
def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200

# def test_function_fixture(function_fixture):
#   assert function_fixture == 1
