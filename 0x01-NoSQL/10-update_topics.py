#!/usr/bin/env python3
'''Module in Task 10
'''


def update_topics(mongo_collection, name, topics):
    '''Changes all topics of a collection's document depending on the name
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
