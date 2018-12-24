import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds139523.mlab.com:39523/superbike

host = "ds139523.mlab.com"
port = 39523
db_name = "superbike"
user_name = "kira"
password = "VetKira.96"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())