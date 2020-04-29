import inspect
import requests


class AlaskaClient:

    def __init__(self, host):
        self.host = host

    def verify_response(self, res: requests.Response, ok_status=200) -> requests.Response:
        func = inspect.stack()[1][3]
        if isinstance(ok_status, int):
            ok_status = [ok_status]
        if res.status_code not in ok_status:
            raise ValueError(
                f"Verified response: function {func} failed: "
                f"server responded {res.status_code} "
                f"with data: {res.content}"
            )
        return res

    vr = verify_response

    def create_bear(self, data: dict):
        return requests.post(self.host + "/bear", json=data)

    def update_bear(self, uid: int,  data: dict):
        return requests.put(self.host + f"/bear/{uid}", json=data)

    def get_bear(self, uid: int):
        return requests.get(self.host + f"/bear/{uid}")

    def get_all_bears(self, uid: int):
        return requests.get(self.host + f"/bear")

    def delete_bear(self, uid: int):
        return requests.delete(self.host + f"/bear/{uid}")

    def delete_all_bears(self, uid: int):
        return requests.delete(self.host + f"/bear")
