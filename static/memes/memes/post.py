import facebook as fb

def main():
    cfg = {
        "name": "Civilton",
        "page_id": "",
        "access_token": "EAADZBzkfZAjfABAJEDowtP2r35XhLQbUZCNAVdCG11H4JrzRjU5gGs8gAHGhwPVcuqimRx9wbFJSTeNFFUUdAxR7kqQqBTPb67xNYrfyHukkbcZAq0Ae3jne6jjBtjTiE231J0tP6azE58uumAp3W7fXNZCyLI2NZBSkz9ZBzgY65qgZAHhMeNDAUdJUPPc0VpDWId1x35udkKt7f5DzqcDKHTGg2f3jLLudLvx8JdcMUQZDZD"
    }

    api = get_api(cfg)
    msg = "Hello world!"
    status = api.put_wall_post(msg)

def get_api(cfg):
    graph = fb.GraphAPI(cfg['access_token'], version='2.2')

    # Get page token to post as the page. You can skip
    # the following if you want to post as yourself.
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
    graph = fb.GraphAPI(page_access_token)
    return graph
