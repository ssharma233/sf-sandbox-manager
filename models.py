import json

class ExportItem:
    def __init__(self, query, operation="Upsert", externalId="Name"):
        self.query = query
        self.operation = operation
        self.externalId = externalId
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class ExportObject:
    def __init__(self, objects):
        self.objects = objects

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)