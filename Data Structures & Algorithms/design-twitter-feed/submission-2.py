class Twitter:

    def __init__(self):
        self.tweets = []
        heapq.heapify(self.tweets)
        self.followers = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time-=1
        tweet = (self.time, userId, tweetId)
        heapq.heappush(self.tweets, tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        q = deque()
        while self.tweets:
            time, user, tweetId = heapq.heappop(self.tweets)
            if user == userId or (userId in self.followers and user in self.followers[userId]):
                res.append(tweetId)
            tweet = (time, user, tweetId)
            q.append(tweet)
            if len(res) == 10:
                break

        while q:
            tweet = q.popleft()
            heapq.heappush(self.tweets, tweet)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)
