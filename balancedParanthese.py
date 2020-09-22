    def minAddToMakeValid(self, S: str) -> int:
        vision = []
        back_vision = []
        
        for i in range(0, len(S)):
            if S[i] == "(":
                vision.append(i)
            if S[i] == ")":
                if len(vision) > 0:
                    vision.pop(-1)
                else:
                    back_vision.append(i)
        print(vision, back_vision)
                
        return(len(vision) + len(back_vision))