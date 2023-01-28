

def validate(self, value):
    return json.loads(value) or True  # OK
