class Twitter(object):

    def __init__(self):

        """
        Initialize your data structure here.
        """
        self.userTweetlistDict = {};
        self.graphAdjDict = {};
        self.timeStamp = 0;

    def postTweet(self, userId, tweetId):

        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """

        # using userTweetlistDict, construct {userID:[(tweetID,timestamp) ..]}

        self.timeStamp = self.timeStamp + 1;
        if userId not in self.userTweetlistDict:
            temp = [];
            temp.append((tweetId, self.timeStamp));
            self.userTweetlistDict[userId] = temp;

        else:
            temp = self.userTweetlistDict[userId];
            temp.append((tweetId, self.timeStamp));
            self.userTweetlistDict[userId] = temp;


    def getNewsFeed(self, userId):

        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """

        userTweetlist = [];

        if userId in self.userTweetlistDict:
            userTweetlist = self.userTweetlistDict[userId];

        followTweetlist = [];

        if userId in self.graphAdjDict:
            followList = self.graphAdjDict[userId];
            followList = list(set(followList));

            for i in range(0, len(followList)):
                if followList[i] in self.userTweetlistDict:
                    followTweetlist = followTweetlist + self.userTweetlistDict[followList[i]];
        currTweetlist = userTweetlist + followTweetlist;

        if currTweetlist == []:
            return [];

        currTweetlist.sort(key = lambda x: x[1], reverse = True);

        resList = [];
        if len(currTweetlist) <= 10:
            for pos in range(0, len(currTweetlist)):
                resList.append(currTweetlist[pos][0]);
        else:
            for pos in range(0, 10):
                resList.append(currTweetlist[pos][0]);

        return resList;


    def follow(self, followerId, followeeId):

        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """

        # use graphAdjDict to construct adjlist of directed graph
        if followerId != followeeId:

            if followerId not in self.graphAdjDict:
                adjList = [];
                adjList.append(followeeId);
                self.graphAdjDict[followerId] = adjList;

            else:
                adjList = self.graphAdjDict[followerId];
                adjList.append(followeeId);
                self.graphAdjDict[followerId] = adjList;


    def unfollow(self, followerId, followeeId):

        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """

        if followerId != followeeId:

            if followerId in self.graphAdjDict:
                currAdj = self.graphAdjDict[followerId];
                if followeeId in currAdj:
                    currAdj.remove(followeeId);
                    if currAdj == []:
                        del self.graphAdjDict[followerId];
                    else:
                        self.graphAdjDict[followerId] = currAdj;


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
