class Solution(object):

    def canFinish(self, numCourses, prerequisites):

        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # build a planed course boolean list

        planedList = [];
        for i in range(0, numCourses):
            planedList.append(False);

        # build a hash table to store the course id with its corresponding prerequisites

        dict = {};

        for pos in range(0, len(prerequisites)):
            courseID = prerequisites[pos][0];
            prerequisiteID = prerequisites[pos][1];

            if courseID not in dict:
                temp = [];
                temp.append(prerequisiteID);
                dict[courseID] = temp;

            else:
                temp = dict[courseID];
                temp.append(prerequisiteID);
                dict[courseID] = temp;

        # helper function will determine whether the given course can be taken or not

        courseTakenset = set();
        for i in range(0, numCourses):
            if self.helper(courseTakenset, dict, planedList, i) == False:
                return False;
        return True;

        
    def helper(self, courseTakenset, dict, planedList, i):

        if i in courseTakenset:
            return True;

        planedList[i] = True;
        if i not in dict:
            courseTakenset.add(i);
            return True;

        preList = dict[i];

        for p in range(0, len(preList)):
            if preList[p] not in courseTakenset and (planedList[preList[p]] == True or self.helper(courseTakenset, dict, planedList, preList[p]) == False):
                return False;

        courseTakenset.add(i);
        return True;
