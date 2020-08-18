def josephus():
    n, k = map(int, input("n m을 입력하세요 : ").split())
    people = []
    answer = []
    temp = 0
    length = n
    
    for i in range(1, int(n) + 1):
        people.append(i)
    
    
    for i in range(n): 
        temp += (k-1) 
        
        if length <= temp: 
               temp = temp % length ### 어려운 핵심부
        
        answer.append(str(people[temp])) 
        del people[temp]   
        length = length - 1   
    
    return print("<",",".join(answer),">", sep = '') # join 각 str형 원소들을 합치는 역할



josephus()