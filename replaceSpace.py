def replaceSpace(self, s):
    # write code here
    import re
    s = re.sub(r" ", "%20",s)
    return s
