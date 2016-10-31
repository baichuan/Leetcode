# The read4 API is already defined for you.

# @param buf, a list of characters
# @return an integer
# def read4(buf):


class Solution(object):
    
    # use a queue to store the remaining character of last call (FIFO) and queue should be global variable
    def __init__(self):

	self.queue = [];
    
    def read(self, buf, n):

        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """

        # 第一次调用时，如果read4读出的多余字符我们要先将其暂存起来，这样第二次调用时先读取这些暂存的字符
        # 第二次调用时，如果连暂存字符都没读完，那么这些暂存字符还得留给第三次调用时使用
        
        i = 0;
        
        while i < n and self.queue:
            
            buf[i] =  self.queue.pop(0);
            i += 1;
            
        # when the queue is empty, we can read the character from current call
        
        for pos in range(0, n, 4):
            
            temp = [""] * 4;
            readBytes = read4(temp);
            
            # 如果读到字符多于我们需要的字符，需要暂存这些多余字符
            
            if readBytes > n - pos:
                
                buf[pos: pos + n - pos] = temp;
                
                # 把多余的字符存入队列中
                
                for inpos in range(n - pos, readBytes):
                    self.queue.append(temp[inpos]);
            
            # 如果读到的字符少于我们需要的字符，直接拷贝  
             
            else:
                
                buf[pos: pos + readBytes] = temp;

            # 同样的，如果读不满4个，说明数据已经读完，返回总所需长度和目前已经读到的长度的较小的   

            if readBytes < 4:
                
                return min(pos + readBytes, n);
        
        # 如果循环内没有返回，说明读取的字符是4的倍数   
        
        return n;
