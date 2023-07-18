#!/usr/bin/env puthon3
'''Module in TAsk 11
'''


def schools_by_topic(mongo_collection, topic):
    '''Returns the list of schools that have a specific topic
    '''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
