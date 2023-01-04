#！coding=utf-8
import pytest,requests
from requests.structures import CaseInsensitiveDict, LookupDict

class TestRequests:

    @pytest.mark.parametrize(
        "url, expected",
        (
                (
                        "http://example.com/path#fragment",
                        "http://example.com/path?a=b#fragment",
                ),
                (
                        "http://example.com/path?key=value#fragment",
                        "http://example.com/path?key=value&a=b#fragment",
                ),
        ),
    )
    def test_params_are_added_before_fragment(self, url, expected):
        request = requests.Request("GET", url, params={"a": "b"}).prepare()
        assert request.url == expected

# assert 使用
# assert "Content-Length" not in req.headers
# assert "Content-Length" in r.headers
# assert req.headers["Content-Length"] == "0"
# assert next_resp.request.body is None
# assert request.url == expected
# assert isinstance(request.body, bytes)
# assert r.status_code == 200, f"failed for scheme {scheme}"  #附带自定义错误信息
# assert len(e.response.history) == 30
# assert r.json()["data"] == byte_str.decode("utf-8")
# assert (self.case_insensitive_dict == other) is result

# pytest手动
#  pytest.fail("Expected redirect to raise TooManyRedirects but it did not")

class TestCaseInsensitiveDict:
    @pytest.fixture(autouse=True)
    def setup(self):
        """CaseInsensitiveDict instance with "Accept" header."""
        self.case_insensitive_dict = CaseInsensitiveDict()
        self.case_insensitive_dict["Accept"] = "application/json"

    possible_keys = pytest.mark.parametrize(
        "key", ("accept", "ACCEPT", "aCcEpT", "Accept")
    )
    @possible_keys
    def test_getitem(self, key):
        assert self.case_insensitive_dict[key] == "application/json"


if __name__=='__main__':
    pytest.main(["test_requests.py"])