class Solution(object):

    def simplifyPath(self, path):

        """
        :type path: str
        :rtype: str
        """
        
	# test cases:
	# "/home/" => "/home"
	# "/a/./b/../../c/d/" => "/c/d"
	# "/../" => "/"
	# "/home//baichuan/" => "/home/baichuan"

        parsed_path = path.strip().split("/");
        res = [];
        
        for i in range(0, len(parsed_path)):
            
            # ignore these cases

            if parsed_path[i] == "" or parsed_path[i] == ".":
                continue;
                
            elif parsed_path[i] == "..":
                if len(res) > 0:
                    res.pop();
                    
            else:
                res.append(parsed_path[i]);
                
        return "/" + "/".join(res);
