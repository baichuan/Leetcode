class Solution(object):

    def hIndex(self, citations):

        """
        :type citations: List[int]
        :rtype: int
        """

        h_index = 0;

        # reverse sort the citation list first
        citations = sorted(citations, reverse= True);

        for i in range(0,len(citations)):

            if i+1 <= citations[i]:
                h_index = h_index + 1;
            else:
                break;

        return h_index;
