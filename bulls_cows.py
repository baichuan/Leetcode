class Solution(object):

    def getHint(self, secret, guess):

        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        s_dict = {};
        g_dict = {};

        for i in range(0, len(secret)):

            if secret[i] not in s_dict:
                temp_s = [];
                temp_s.append(i);
                s_dict[secret[i]] = temp_s;

            else:

                temp_s = s_dict[secret[i]];
                temp_s.append(i);
                s_dict[secret[i]] = temp_s;

                

            if guess[i] not in g_dict:
                temp_g = [];
                temp_g.append(i);
                g_dict[guess[i]] = temp_g;

            else:
                temp_g = g_dict[guess[i]];
                temp_g.append(i);
                g_dict[guess[i]] = temp_g;

                
        # bull = secret与guess下标与数值均相同的数字个数
        # cow = secret与guess中出现数字的公共部分 - bull
        
        b_count = 0;
        c_count = 0;

        for k, v in s_dict.items():

            if k in g_dict.keys():

                bull = len(set(v).intersection(g_dict[k]));
                cow = min(len(v), len(g_dict[k])) - bull;
                b_count = b_count + bull;
                c_count = c_count + cow;

        return str(b_count) + "A" + str(c_count) + "B";
