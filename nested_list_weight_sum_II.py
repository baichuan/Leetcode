# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation

# """

#class NestedInteger(object):

#    def isInteger(self):

#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """

#

#    def getInteger(self):

#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """

#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution(object):

    def depthSumInverse(self, nestedList):

        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """

        maxDepth = self.dfsDeep(nestedList)

        return self.depthSumHelper(nestedList, maxDepth)


    def dfsDeep(self, nestedList):

        if len(nestedList) == 1 and nestedList[0].isInteger():

            return 1

        deep = 0    

        for nInt in nestedList:

            if nInt.isInteger():

                deep = max(deep, 1)

            else:

                deep = max(self.dfsDeep(nInt.getList()) + 1, deep)

        return deep

        
    def depthSumHelper(self, nestedList, maxDepth): 

        sum = 0;

        for item in nestedList:

            if item.isInteger():

                sum = sum + item.getInteger() * maxDepth;

            else:

                sum = sum + self.depthSumHelper(item.getList(), maxDepth - 1);
                
        return sum;

