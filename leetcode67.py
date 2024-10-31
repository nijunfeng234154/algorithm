class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        jinwei = 0
        x = 0
        res = []
        l = max(len(a),len(b))
        if len(a)>len(b):
            for i in range(len(a)-len(b)):
                b = '0'+b
        else:
            for i in range(len(b)-len(a)):
                a = '0'+a

        for i in range(l-1,-1,-1):
            x = int(a[i])^int(b[i])
            x = x^jinwei
            if a[i] == b[i] == '1':
                jinwei = 1
            else:
                jinwei = 0
            res.append(x)
        
        for i in range(len(res)):
            if i != 0:
                res = res[i:]
                break

        return res