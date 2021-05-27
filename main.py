def MatchingCharacters(strParam):
 
 count1=0
 for i in range(0,len(strParam)):
    w=strParam[i]
    temp=0
    for j in range(i+1,len(strParam)):
     if w==strParam[j]:
            break
     temp=temp+1  
    if temp>=((len(strParam)-1)-i):
      temp=0
    if temp>count1:
      count1=temp

     
     
 return count1        

  # code goes here
  

# keep this function call here 
print(MatchingCharacters(input()))
