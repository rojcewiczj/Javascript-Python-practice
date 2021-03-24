scores = [[1,91]]

def average(scores):
    dicti = {}
    output = []
    
    for score in scores:
        if score[0] not in dicti:
            dicti[score[0]] = [score[1]]
        else:
            dicti[score[0]].append(score[1])
    
    for key in dicti:
        dicti[key].sort(reverse=True)
        inner_output = []
        inner_output.append(key)
        total = 0
        for i in range(0, len(dicti[key])):
            if i <= 4:
                total += dicti[key][i]
            if i == 4:
                total = total // 5
               
                break
            if i == len(dicti[key])-1:
                total // len(dicti[key])
        inner_output.append(total)
        output.append(inner_output)
    print(dicti)
    print(output)

            
                



    

average(scores)