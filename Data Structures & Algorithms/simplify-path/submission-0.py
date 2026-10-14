class Solution:
    def simplifyPath(self, path: str) -> str:
        result = "/"
        stack = []
        path_list = path.split("/")
        for each in path_list:
            if each == "/" or each =="." or not each:
                continue
            
            elif each == ".." :
                if stack :
                    stack.pop()
            else :
                stack.append(each)
      
        result = result+"/".join(stack) 
        return result
            
        