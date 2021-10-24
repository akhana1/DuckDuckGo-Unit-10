import pytest
import requests

presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson", "Buren", "Harrison", "Tylee",
              "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Jonson", "Grant", "Hayes", "Garfield",
              "Arthur", "Cleveland", "Harrison", "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding",
              "Coolidge", "Hoover", "Roosevelt", "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "August",
              "Carter",
              "Reagan", "Bush", "Clinton", "W", "Obama", "Trump", "Biden"]

url_pl = "https://api.duckduckgo.com"

resp = requests.get(url_pl + "/?q=President of the united states&format=json")
rsp_data = resp.json()


@pytest.mark.parametrize("president_name", presidents)
def test_pl_president(president_name):
    for president_name in ['Text']:
        if president_name in rsp_data['RelatedTopics']:
            assert True
