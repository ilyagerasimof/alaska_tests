from api import bearGenerator


def test_create_new_bear(client):
        data = bearGenerator.random_valid_bear()
        res = client.vr(client.create_bear(data), [200, 201])
        bear_id = res.json()
        data['bear_id'] = bear_id
        res = client.vr(client.get_bear(bear_id), [200, 201])
        exists = res.json()
        assert data == exists

def test_update_bear(client):
        data = bearGenerator.random_valid_bear()
        res = client.vr(client.create_bear(data), [200, 201])
        bear_id = res.json()
        data_new = bearGenerator.random_valid_bear()
        client.vr(client.update_bear(bear_id, data_new), [200, 201])
        data_new['bear_id'] = bear_id
        res = client.vr(client.get_bear(bear_id), [200, 201])
        exists = res.json()
        assert data_new == exists
