string = "aaabbccccddeefffffggghhltmmmllll"

def CrushIt(string):
    vision = []
    i = 0
    while i < len(string) :
        if len(vision) < 1:
            vision.append(i)
            i += 1
        else:
            if string[i] == string[vision[-1]] and i < len(string):
                vision.append(i)
                i += 1
            else:
                if len(vision) >= 3:
                    if vision[0] == 0:
                        string = string[vision[-1] + 1: len(string)]
                    else:
                        string = string[0:vision[0]] + string[vision[-1] + 1: len(string)]
                    i = 0
                    vision =[0]
                    i += 1
                else:
                    vision=[]
                    vision=[i]
                    i += 1

            if vision[-1] == (len(string)-2): 
                string = string[0: vision[0]]

    print(string)
   


CrushIt(string)