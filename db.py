from pymongo import MongoClient
from pymongo import uri_parser
import os

# The Singleton Set
_db_set = {}
def DB(uri):
    global _db_set
    if uri not in _db_set:
        _client = MongoClient(uri)
        _db_set[uri] = _client[uri_parser.parse_uri(uri)['database']]

    return _db_set[uri]
