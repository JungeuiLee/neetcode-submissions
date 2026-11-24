import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweet:
            self.tweet[userId] = []
        self.tweet[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        user = {userId} | self.following.get(userId,set())

        feed = []
        for u in user:
            feed.extend(self.tweet.get(u, []))
            feed.sort(reverse=True)
        return [tid for t, tid in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        # if followeeId not in self.following:
        #     self.following[followeeId] = []
        # self.following[followeeId].append(followerId)

        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)

