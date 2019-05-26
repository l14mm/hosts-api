DOMAIN = { 
  'hosts': {
    'schema': {
      '_id': {'type': 'integer'},
      'name': {'type': 'integer'},
      'timestamp': {'type': 'integer'},
      'friendly_name': {'type': 'integer'},
      'host': {'type': 'integer'},
      'person': {'type': 'integer'},
      'mac': {'type': 'integer'}
    }
  }
}                                               
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'monitor'
RESOURCE_METHODS = ['GET']
X_DOMAINS = '*'
X_HEADERS = ['Authorization','Content-type']