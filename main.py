#!/usr/bin/env python

import twitter

so_far = int()
api = twitter.Api(consumer_key='uWTo0x3JMpSwsW0JzeOdbGBQV',
                  consumer_secret='pmaaBV5RiKwJHAub6t7TjREWLXJDgCJg88bcpgeIYJ0rrX3DkY',
                  access_token_key='776129399783428096-P6q5kQA0EZWSicMz2hYRIWAdjuD9ETX',
                  access_token_secret='PPkuQ55uUMYXiVP90Woyc152gqFvCaFzvRVAhl0fRTTpb')


def follow(uid, how_many=50):
    global so_far
    following = list()
    for fid in api.GetFriendIDs(uid):
        try:
            uid = api.CreateFriendship(fid).id
            so_far += 1
            if so_far >= how_many:
                exit(0)
            print(f"now following {uid}")
            following.append(uid)
        except twitter.error.TwitterError:
            pass
    return following


def get_n_followers(start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(follow(vertex))
    return visited


if __name__ == '__main__':
    for fid in api.GetFriendIDs(api.VerifyCredentials().id):
        get_n_followers(fid)
