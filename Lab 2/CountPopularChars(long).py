r'''
Task Description:
In this task, you are going to design one program to check the popular characters
in a given string. You need to write one program to calculate the top 5 most 
frequent characters. The following are some hints that may help you design this program. 
	. String has a cool function that you can use to return a copy of the string 
     in which all case-based characters have been lowercased. 
	. To get the top 5 most frequent characters after sorting them, you need to 
     extract all the characters first and figure out one way to calculate the frequency 
     of each character. Then select the top 5 characters. 
	. The output must in the descending order of character frequency. If there are 
     characters with the same frequency, they must be printed in ascending ASCII order.
	. Print out the top 5 characters and their counts in the screen. (Your output should be in one line)

Running Examples:
C:\INF1002\Lab2\CountPopularChars>python CountPopularChars.py sdsERwweYxcxeewHJesddsdskjjkjrFGe21DS2145o9003gDDS
d:7,s:7,e:6,j:4,w:3
'''
import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def CountPopularChars():
     try:
          # Initialize an empty dictionary to store the frequency of each character in the string.
          stringDict = {}
          top5repeated = {}

          # Convert the string to lowercase and count the frequency of each character.
          if len(sys.argv) == 2:
               for i in sys.argv[1].lower():
                    if i in stringDict:
                         stringDict[i] += 1
                    else:
                         stringDict[i] = 1
               
               # Sort the dictionary in descending order of character frequency and ascending ASCII order.
               top5 = dict(sorted(stringDict.items(), key=lambda item:item[1],reverse=True)[:5])
               for i in top5:
                    value = i
                    key = top5[i]
                    if key in top5repeated:
                         top5repeated[key].append(value)
                    else:
                         top5repeated[key] = [value]

               # Sort the dictionary in ascending ASCII order.
               finalList = []
               for item in top5repeated:
                    repeatSort = sorted(top5repeated[item])
                    finalList += repeatSort

               # Create a new dictionary with the sorted ASCII order.
               finalDict = {}
               for key in finalList:
                    value = top5[key]
                    finalDict[key] = value
               
               outputString = ','.join(f"{key}:{value}" for key,value in finalDict.items())
               print(outputString)
      
     except:
          print('Your input is invalid!')

if __name__=='__main__':
      CountPopularChars()
      
