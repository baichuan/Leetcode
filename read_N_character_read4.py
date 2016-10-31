# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

# 读到buf里，可能file里的字符数大于n，所以只能读n。如果file里的字符数小于等于n，那读所有的就好
# Check several cases: 1) file = 14, n = 14. 2) file = 10, n = 16. 3) file = 16, n = 10

class Solution(object):

    def read(self, buf, n):

        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """

        # we have to write character results into the buffer

        buffer = [""]*4;
        readBytes = 0;

        for i in range(0, n/4 + 1):

            size = read4(buffer);
            if size:
                buf[readBytes:readBytes + size] = buffer;
                readBytes = readBytes + size;

            else:
                break;

        return min(readBytes, n);



# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer

# def read4(buf):

class Solution(object):

    def read(self, buf, n):

        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        
        for i in range(0, n, 4):
            
            temp = [""]*4;

            # 将数据读入临时数组
            readBytes = read4(temp);

            #  将临时数组拷贝至buf数组，这里拷贝的长度是本次读到的个数和剩余所需个数中较小的
            buf[i: i + min(readBytes, n - i)] =temp;

            # 如果读不满4个，说明已经读完了，返回总所需长度和目前已经读到的长度的较小的
            if readBytes < 4:
                
                return min(i + readBytes, n);

        # 如果循环内没有返回，说明读取的字符是4的倍数       
        return n;
