import requests
import streamlit as st
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return r.json()

hide_st_style = """
                <style>
                #MainMenu { visibility : hidden;}
                footer { visibility : hidden;}
                header { visibility : hidden;}
                </style>
                """
st.markdown(hide_st_style , unsafe_allow_html = True)

# use local css
def local_css(file_name):
    with open(file_name) as f :
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

img_codeauction = Image.open("images/code.png")
img_q1 = Image.open("images/q1.png")
img_q2 = Image.open("images/q2.png")
img_q3 = Image.open("images/q3.png")
img_q4 = Image.open("images/q4.png")
img_q5 = Image.open("images/q5.png")
img_q6 = Image.open("images/q6.png")
img_q7 = Image.open("images/q7.png")
img_q8 = Image.open("images/q8.png")
img_q9 = Image.open("images/q9.png")
img_q10 = Image.open("images/q10.png")
img_q11 = Image.open("images/q11.png")
img_q12 = Image.open("images/q12.png")
img_q38 = Image.open("images/q37.png")



#st.image(img_logo,width = 220, use_column_width = 70 )
                                  

#horizontal menu
selected = option_menu(
        menu_title ="",
        options =["home","Questions","Contact"],
        icons = ["house","book","person-fill"],
        menu_icon = "cast",
        default_index = 0,
        orientation = "horizontal")


if selected == "home":
      with st.container():
          st.title("CODE AUCTION")
          st.subheader("UDBHAV - 2023 ")
          st.subheader("Technical Event conducted by CSE department")
          st.image(img_codeauction,caption="Logo")
if selected == "Questions":
       with st.container():
           st.subheader("LEVEL 1 CODING QUESTIONS")
           st.title("Question no 1")
           st.write(
               """
Rahul is given an assignment consisting of an array of positive number and an integer k. The task is to obtain an array consisting of only one element by performing the following operations:

=> choose any two numbers from the array (OR) indices from the array such that A[i]+A[j]<=K, and remove either A[i] or A[j] from the array

If it is possible to obtain such array using the above operations only the print YES or print NO

Input Format:

The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and K.
The second line contains N space-separated integers A1, A2, …, AN.

Output Format:

For each test case, print "YES" if it is possible to obtain an array consisting of only one element using the given operation, otherwise print "NO"




              """ )
           st.image(img_q1)
           st.subheader("Base price : 15,000")
           st.subheader("points : 100 ")
           st.write("----------")
           st.title("Question 2")
           st.write("""
Problem – 2:
Pavan is participating in a quiz show: “Who wants to be a zillionaire?”, but Pavan is not confident in his mathematical skills as he is tired by writing the quiz and has asked for help evaluating his performance.
 Each questions has 26 candidate answers but only one is the optimal solution and is depicted by the characters A to Z. 
All the question in the quiz are shuffled randomly and the contestants are asked these questions randomly. If the contestant answers any question incorrectly he is out of the game. In order to win the game the contestant needs to answer N questions correctly consistently I.e.(successively) out of
M questions asked. 
Help pavan in evaluating his performance.


INPUT:

	The first line contains the integer T denoting the number of test cases.
	The first line of each test cases contains a single integer M denoting the number of questions and N denoting the questions required to answer correctly.
	next line contains N letters denoting the correct answers to the questions asked.
	Next line contains N letters denoting the answers given by Pavan to the questions.


	
OUTPUT:


	Print “QUALIFIED” if pavan passed the quiz else print “NOT QUALIFIED”.



                   """)

           st.image(img_q2)
           st.subheader("Base price : 8,000")
           st.subheader('pints : 50')
           st.write("----")
           st.title("Question 3")
           st.write("""
Arjun is learning how to play with arrays and is growing very found of arrays. 
Arjun is stuck in a problem which contains an array of numbers of size N. 
Given an array Arr[] of size N. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.
Help Arjun to solve the question.

INPUT FORMAT:
	
The first line contains N – denoting the number of integers
The second line contains N integers denoting the elements of the arrays.

OUTPUT FORMAT:

Your task is to print the sum of the contiguous subarray within a one-dimensional array of numbers that has the largest sum.

""")
           st.image(img_q3)
           st.subheader("Base price : 6,000")
           st.subheader("points : 30")
           st.write("---")
           st.title("Question 4")
           st.write("""
Given a non-negative integer N. The task is to check if N is a power of 2. More formally, check if N can be expressed as 2^x for some x.
CONSTRAINTS:
0<=N<=10^6

INPUT FORMAT:

The first and only line contains an integer N

OUTPUT FORMAT:

Print YES if it’s a power of 2

Else print NO .

""")
           st.image(img_q4)
           st.subheader("Base price : 6,000")
           st.subheader("points : 30")
           st.write("---")
           st.title("Question 5")
           st.write("""
Naveen is a software engineer, and is a specialist in working with the binary bits of the code.
One of the computer is giving problem to the user and Naveen is trying to repair the chip which contains the bits of the code or program.
The chip is reading the bits of the number, strings wrong, as Naveen is busy with repairing the chip he has asked you to help the error in the chips code.
Your are given two numbers A and B. The task is to count the number of bits needed to be flipped to convert the number A to number B.

CONSTRAINTS:

I<=A,B,<=10^6

INPUT FORMAT:

The first line contains the integer A.
The second line contains the integer B.

OUTPUT FORMAT:

Your task is to print a single integer i.e., the count of the bits needed to flip in order to convert the integer A to integer B.


""")
           st.image(img_q5)
           st.subheader("Base price : 8,000")
           st.subheader("points : 50")
           st.write("---")
           st.title("question 6 ")
           st.write("""


ITPCRC is a very reputed company and has a reputation for their level of questions asked in their recruitment process. In one of the interviews a question on string is asked on string, a string S is said to a Super string if and only if the count of each character in the string is equals to its ASCII value. In the string the ASCII value of the characters are ‘a’ is 1, ‘b’ is 2, ….., ‘z’ is 26. 
Your task is to find out whether the given string is a super string or not. 

CONSTRAINTS:

I<= T<= 10
1<= len(S) <= 50

INPUT FORMAT:

The first line contains the integer T – denoting the number of the test cases.
The next lines contains the string depending upon the value of T.

OUTPUT FORMAT:

	If the string is a super string print “Yes”
	Else print “NO”
""")
           st.image(img_q6)
           st.subheader("base price : 6,000")
           st.subheader("points : 50")
           st.write("---")
           st.title("question 7")
           st.write("""
Shruthi is new to coding and is trying to learn how to play with strings.
Shruthi is learning how to use ASCII values to learn strings. She is struck in a problem and is confused how to use ASCII values to convert the string of upper.
As a friend of Shruthi help her to write the code which converts the string of uppercase letters to lowercase letters.

INPUT FORMAT:

The first line contains an integer T – denoting the number of test cases.
Next there are N line containing a string of uppercase letters.

OUTPUT FORMAT:
	
Your task is to print a string of lowercase letters.

""")
           st.image(img_q7)
           st.subheader("base price : 6,000")
           st.subheader("points : 30")
           st.write("---")
           st.title("question 8")
           st.write("""
A lecturer is trying to form batches of two students in a class for assigning projects to them.
The group is formed on the basis on the grade of the previous test score.
Lecturer wants to form a group based on the following criteria:
	Two students who’s grades sum must be equal to the targeted value set by the lecturer.
	He wants to select as many as students as possible.
As the lecturer is busy correcting papers and assigning grades he as asked you for forming the teams for the project. Your task is to print the number of pairs of students eligible to form the group for the project.

INPUT FORMAT:

The first line contains the integers N- denoting the size of the array and K – denoting the targeted valued set by the professor.
The second line contains N integers denoting the grades of the students.

OUTPUT FORMAT:

Your task is to print a single integer which shows the maximum number of groups formed according to the given criteria.

""")
           st.image(img_q8)
           st.subheader('Base price : 6,000')
           st.subheader("points : 30")
           st.write("---")
           st.title("question 9")
           st.write("""
A number is said to be a prime number if it’s divisible by itself and 1. Given an integer N, the task is to count the number of the prime digits in N and print the sum of the prime numbers present in N.

INPUT FORMAT:

The first line contains the integer T- denoting the number of test cases.
The second line contains the integer N.

OUTPUT FORMAT:

PRINT THE COUT OF THE PRIME NUMBERS THEN THE SUM OF THE PRIME NUMBERS

""")
           st.image(img_q9)
           st.subheader("Base price : 6,000")
           st.subheader("points : 30")
           st.write("---")
           st.title("question 10")
           st.write("""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Explanation:

nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.

nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.

nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

The distinct triplets are [-1,0,1] and [-1,-1,2].

Notice that the order of the output and the order of the triplets does not matter.

Input: nums = [0,1,1]

Output: []

Explanation: The only possible triplet does not sum up to 0.









""")
           #st.image(img_q10)
           st.subheader("Base price 15,000")
           st.subheader("points : 100")
           st.write("---")
           st.title("question 11")
           st.write("""
Ramu has two sons, and he wants to distribute his property among his sons equally such there will be no dispute between his children. Ramu is weak in mathematics and as a friend of Ramu, he has asked your help in dividing the property among his sons equally.
Ramu has N assets. These assets are given in the form of an array.

INPUT FORMAT:

First line of input contains the integer N – denoting the size of the input array.
The second line contains an array of integers denoting the assets of Ramu.

OUTPUT FORMAT:

Print “YES” if the given array can be partitioned into two subarrays such that the sum of the elements in both arrays is equal.
Else print “NO”.

""")
           st.image(img_q11)
           st.subheader("Base price : 8,000")
           st.subheader("points : 50")
           st.write("---")
           st.title("Question 12")
           st.write("""
There was an electronic store heist last night.
All keyboards which were in the store yesterday were numbered in ascending order from some integer number x. For example, if x = 4 and there were 3 keyboards in the store, then the devices had indices 4, 5 and 6, and if x= 10 and there were 7 of them then the keyboards had indices 10,11,13,14,15 and 16.
After the heist, only n keyboards remain, and they have indices a1, a2, …., an.
Calculate the minimum possible number of keyboards that have been stolen. The staff remember neither x nor the number of keyboards in the store before the heist.

INPUT FORMAT:

The fist line contains single integer n- the number of keyboards in the store that remained after the heist.
The second line contains n distinct integers a1, a2, ….., an – the indices of the remaining keyboards. The integers ai are given in arbitrary order and are pairwise distinct.

OUTPUT FORMAT:

Print the minimum possible number of keyboards that have been stolen if the staff remember neither x nor the number of keyboards in the store before the heist.

""")
           st.image(img_q12)
           st.subheader("base price : 10,000")
           st.subheader("points : 75")
           st.write("---")
           st.title("question 13")
           st.write("""
A spy wants to send some secret information to the government. As the data is very
important, he encrypts the message by encoding by adding some extra characters.
the original message has only upper case letters and numbers, while the extra
characters are madeup of lowercase letters and special characters. Can you help the
receiver in designing a program that accepts the message and returns the secret
information.
Input Format:

a string from the user
Constraints
no

Output Format:

original message

Sample Input 0 :

Wel1c%OmE

Sample Output 0 :

W1OE

Sample Input 1:

pRak123aSh

Sample Output 1:

R123

""")
           st.subheader("Base price : 8,000")
           st.subheader("Base price : 50")
           st.write("---")
           st.title("Question 14")
           st.write("""
amir is travelling to mumbai, but this time he is taking flight. His brother has already
told him about luggage weight limits but forgot it. Now he is taking with him 3 trolly
bags.
As per the current airlines which amir will fly. has below weight limits.
There can be at max 2 check-in and 1 cabin luggage. Check-in has total limit of L1
and Cabin has limit of L2.
Now, amir has 3 luggage has weights as W1 and W2 and W3 respectively. Now he
should be smart enough to make sure that he can travel with all the 3 luggage
without paying extra charge.
Find out whether amir can take all of his luggage without any extra charges or not. If
all good and no extra changes were paid, output "Yes" otherwise "No".

Input Format

integers W1,W2,W3 and L1,L2

Constraints

no

Output Format

Yes or No

Sample Input 0

1 2 3 1 2

Sample Output 0

No

Sample Input 1

6 9 7 16 7

Sample Output 1

Yes
""")
           st.subheader("Base price 10,000")
           st.subheader("points : 75")
           st.write("---")
           st.title("Question 15")
           st.write("""
Michael wants to check the parity of the given number. To find tha parity, follow
below steps.
1. convert decimal number into binary number.
2. count the number of 1's and 0's in the binary representation.
if it contains odd number of 1-bits, then it is "odd parity" and if contains even number
of 1-bits then "even parity" Write a program to validate the given number belongs to
odd parity or even parity.
Input Format

a number from the user.

Constraints:

no

Output Format:

odd parity or even parity.

Sample Input 0:

5

Sample Output 0:

even

Sample Input 1:

8

Sample Output 1:

odd
""")
           st.subheader("Base price : 6,000")
           st.subheader("points : 30")
           st.write("---")
           st.title("Question 16")
           st.write("""
sofia loved to play with the programs unfortunately. she got stuck in one of the
questions. she tought to take help of james. james asked her the problem statement.
The problem statement was.
"for the given string S of length N consist of stream of character not in predefined
order. Write a program to find second non-repeating character in a string S. Write a
program to help sofia and james for the given problem statements.

Input Format:

string from the user

Constraints:

no

Output Format:

single character

Sample Input 0:

gaahaajapsps

Sample Output 0:

h

Sample Input 1:

welcome

Sample Output 1:

l

Sample Input 2:

demo
""")
           st.subheader("Base price : 10,000")
           st.subheader("points : 75")
           st.write("---")
           st.title("Question 17")
           st.write("""
You are given an array of integers, a of size n, Your task is to find the number of
elements whose positions will remain unchanged after sorted in ascending order.
Input Format :

array size and elements

Constraints :

no

Output Format:

unchanged count

Sample Input 0:

5

1 2 5 3 4

Sample Output 0:

2

Sample Input 1:

10

1 10 2 9 3 8 4 7 5 6

Sample Output 1:

1

""")
           st.subheader("Base price : 8,000")
           st.subheader("points : 50")
           st.write("---")
           st.title("Question 18")
           st.write("""
A person went to an exhibition. A lucky draw is going on, where one should buy a
ticket. And if they ticket number appear on the screen, that ticket will be considered
as jackpot winner.
he knows the secret of picking up the ticket number, which will be considered for the
jackpot.
1. sort the ticket number in the increasing order.
2. Now, the difference between the adjacent digits should not be more than 2.
If his ticket follows the above condition, then there are more chances to win the
jackpot.
Given a ticket number, find whether the ticket is eligible to be part of jackpot or not.
Print "Yes/No" based on the result.

Input Format

ticket number

Constraints

no

Output Format

Yes or No

Sample Input 0

171

Sample Output 0

No

Sample Input 1

123

Sample Output 1

Yes
""")
           st.subheader("Base price : 8,000")
           st.subheader("points : 50")
           st.write("---")
           st.title("Question 19")
           st.write("""
In an online exam, the test paper set is categorized by the letters A-Z. The students
enrolled in the exam have been assigned a numeric value called application ID. To
assign the test set to the student, firstly the sum of all digits in the application ID is
calculated. If the sum is within the numeric range 1-26 the corresponding alphanetic
set code is assigned to the student, else the sum of the digits are calcualted again
and so on unitil the sum falls within the 1-26 range.

Input Format

application id as int

Constraints

no

Output Format

set number

Sample Input 0

123

Sample Output 0

F

Sample Input 1

786

Sample Output 1

U
""")
           st.subheader("Base price 6,000")
           st.subheader("points : 30")
           st.write("---")
           st.title("Question 20")
           st.write("""
Cristina appeared for a corporate Hackathon. She cleated first round of this and
would like to take next challenge which is coding round. The problem statement
comes to her is
"Write a program to find numbers which are in between integer 2 and integer N and
such that the sum of its digits raised to the third power is equal to the number with
the input given.

Input Format

integer N

Constraints

no

Output Format

an integer value

Sample Input 0

200

Sample Output 0

153

Sample Input 1

300

Sample Output 1

153

""")
           st.subheader("Base price 15,000")
           st.subheader("points : 100")     
           st.write("---")
           st.title("Question 21")
           st.write("""
There was a grocery shop. Shopkeeper would like to keep trasactions as simple as
he can. Hence, he used to take money as whole number. To optimize trasactions, he
decided if someone buys groceries from his shop, he will round money to the nearest
whole number having zeros as last digit. Write a program to help shopkeeper to
make trasactions much simple.
Input Format

a number

Constraints

no

Output Format

nearest int value which ending with 0

Sample Input 0

17

Sample Output 0

20

Sample Input 1

153

Sample Output 1

160

Sample Input 2

174

Sample Output 2

180
""")
           st.subheader("Base price 8,000")
           st.subheader("points : 50")
           st.write("---")
           st.title("Question 22")
           st.write("""
Two strings are said to the same if they are of the same length and have the same
character at each index. Backspacing in a string removes the previous character in
the string.
Given two strings containing lowercase english letters and the character '#' which
represents a backspace key. determine if the two final strings are equal or not.
Return 1 if they are equal else 0.
Input Format

two strings s1 and s2

Constraints

no

Output Format

1 or 0

Sample Input 0

axx#bb#c
axbd#c#c

Sample Output 0

1

Sample Input 1

ayx#cb#c
axbd#c#c

Sample Output 1

0
""")
           st.subheader("Base price 15,000")
           st.subheader("points : 100")
           st.write("---")
           st.title("Question 23")
           st.write("""
a game developing company has developed a math game for kids called "Brain
Fun". The game is for smartphone users and the player is given list of N positive
numbers and a random number K. the player need to divide all the numbers in the
list with random number k and then need to add all the quotients received in each
division. the sum of all the quotients is the score of the player.
Write an algorithm to generate the score of the player.

Input Format

array size, elements and random number k

Constraints

no

Output Format

an int value

Sample Input 0

5

1 2 3 4 5

3

Sample Output 0

3
""")
           st.subheader("Base price 8,000")
           st.subheader("points : 50")
           st.write("---")
           st.title("Question 24")
           st.write("""
Tom has joined a new company and he is assigned a program to code. But before
starting to code, he needs to know the coding standards. He need to make sure that
the variable name should meet the below standards,
=> contains only english letter
=> and/or digits
=> and/or underscore (_)
=> should not start with digits
The program should return True/False based on the above conditions

Input Format

a string from the user

Constraints

no

Output Format

true or false

Sample Input 0

abc7

Sample Output 0

true

Sample Input 1

abc#

Sample Output 1

false
""")
           st.subheader("Base price 8,000")
           st.subheader("points : 50")
           st.write("---")
           st.title("Question 25")
           st.write("""
The function accepts two characters ch1 and ch2 as arguments, ch1 and ch2 are
alphabetical letters. Implement the function to find and return the next letter so that
distance between ch2 and the next letter is the same as the distance between ch1
and ch2. While counting distance if you exceed thhe letter 'z' then, count the
remaining distance starting from the letter 'a'.
Distance between two letters is the number of letters between them.

Input Format

char ch1 and char ch2

Constraints

no

Output Format

char ch

Sample Input 0

c g

Sample Output 0

k

Sample Input 1

a c

Sample Output 1

e
""")
           st.subheader("Base price 8,000")
           st.subheader("points : 50")
           st.write("---")
           st.title("Question 26")
           st.write("""
The country visa center generates the token number for its applicants from their
application ID. the application ID is numberic value. The token number is generated
in a specific form. the even digits in the applicant's ID are replaced by the digit one
greater than the even digitand the odd digits in the applicant's ID are replaced by the
digit one lesser than the odd digit. The numeric calue thus generated represents the
token number of applicant.
Write an algorithm togenerate the token number from the applicant ID.

Input Format

application ID

Constraints

no

Output Format

token id

Sample Input 0

235

Sample Output 0

324

Sample Input 1

417

Sample Output 1

506
""")
           st.subheader("Base price 8,000")
           st.subheader("points : 50")
           st.write("---")
           st.title("Question 27")
           st.write("""
Rahul's teacher gave an assignment to all the student that when they show up
tomorrow they should find a special type of number and report her. He thought very
carefully and came up with an idea to have neon numbers. A neon number is a
number where the square of the sum of each digit of the number results in the given
number.Given an integer N, Write aprogramto find whether the number N is a Neon
number. If it's not a Neon number, print the sqaure of the sum of digits of the number.

Input Format

a number

Constraints

no

Output Format

true or false

Sample Input 0

81

Sample Output 0

true

Sample Input 1

91

Sample Output 1

false


""")
           st.subheader("Base price 6,000")
           st.subheader("points : 30")
           st.write("---")
           st.title("Question 28")
           st.write("""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.


TEST CASE 1:

Input: n = 3, k = 3

Output: "213"

TEST CASE 2:

Input: n = 4, k = 9

Output: "2314"


""")
           st.subheader("Base price 15,000")
           st.subheader("points : 100")
           st.write("---")
           st.title("Question 29")
           st.write("""
A data company wishes to store its data files on the server. They N files. Each file
has a particular size. the server stires the files in bucket list. The bucket ID is
calculated as the sum of the digits of its file size. The server.. the bucket ID for every
file request where the file is stored.
Write an algorithm to find the bucketIDs where the files are stored.

Input Format

an array size and elements

Constraints

no

Output Format

bucketIds

Sample Input 0

4

43 345 20 987

Sample Output 0

7 12 2 2
""")
           st.subheader("Base price 6,000")
           st.subheader("points : 30")
           st.write("---")
           st.title("Question 30")
           st.write("""
Given an array a[] of size N which contains elements from 0 to N-1,
you need to find all the elements occurring more than once in the given
array.

Input:

N = 4
a[] = {0,3,1,2}

Output: -1

Explanation:
N=4 and all elements from 0 to (N-1 = 3) are present in the given array.

Therefore output is -1.

Input:

N = 5
a[] = {2,3,1,2,3}

Output: 2 3

Explanation: 2 and 3 occur more than once
in the given array.

""")
           st.subheader("Base price 8,000")
           st.subheader("points : 50")
           st.write("---")
           st.title("Question 31")
           st.write("""
Given an unsorted array arr[] of size N having both negative and
positive integers.
The task is place all negative element at the end of array without
changing the order of positive element and negative element.

Input :
N = 8
arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }

Output :
1 3 2 11 6 -1 -7 -5

Input :
N=8

arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}

Output :
7 9 10 11 -5 -3 -4 -1
""")
           st.subheader("Base price 15,000")
           st.subheader("points : 100")
           st.write("---")
           st.title("Question 32")
           st.write("""
Given an array A[ ] of positive integers of size N, where each value
represents the number of chocolates in a packet.
Each packet can have a variable number of chocolates. There are M
students, the task is to distribute chocolate packets among M students
such that :
1. Each student gets exactly one packet.
2. The difference between maximum number of chocolates given to a
student and minimum number of chocolates given to a student is minimum.

Example 1:
Input:
N = 8, M = 5
A = {3, 4, 1, 9, 56, 7, 9, 12}

Output: 6
Explanation: The minimum difference between
maximum chocolates and minimum chocolates
is 9 - 3 = 6 by choosing following M packets :
{3, 4, 9, 7, 9}.

Example 2:

Input:
N = 7, M = 3
A = {7, 3, 2, 4, 9, 12, 56}

Output:2

Explanation: The minimum difference between
maximum chocolates and minimum chocolates
is 4 - 2 = 2 by choosing following M packets :
{3, 2, 4}

""")
           st.subheader("Base price 15,000")
           st.subheader("points : 100")
           st.write("---")
           st.title("Question 33")
           st.write("""
Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.

INPUT FORMAT:
Array named ‘num’.

OUTPUT FORMAT:
Return the array answer.

TEST CASE 1:

Input: nums = [10,4,8,3]

Output: [15,1,11,22]

TEST CASE 2:

Input: nums = [1]

Output: [0]
""")
           st.subheader("Base price 15,000")
           st.subheader("points : 100")
           st.write("---")
           st.title("Question 34")
           st.write("""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

INPUT FORMAT:
 Number n


OUTPUT FORMAT:
 True or False

TEST CASE 1:

Input: n = 19

Output: true

TEST CASE 2:

Input: n = 2

Output: false
""")
           st.subheader("Base price 8,000")
           st.subheader("points : 50")
           st.write("---")
           st.title("Question 35")
           st.write("""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
INPUT FORMAT:
 Array

OUTPUT FORMAT:
Int number

TEST CASE 1:

Input: nums = [2,3,1,1,4]

Output: 2

TEST CASE 2:

Input: nums = [2,3,0,1,4]

Output: 2

""")
           st.subheader("Base price 15,000")
           st.subheader("points : 100")
           st.write("---")
           st.title("Question 36")
           st.write("""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

INPUT FORMAT:
 Two strings

OUTPUT FORMAT:
Int number

TEST CASE 1:

Input: word1 = "horse", word2 = "ros"

Output: 3

TEST CASE 2:

Input: word1 = "intention", word2 = "execution"

Output: 5

""")
           st.subheader("Base price 15,000")
           st.subheader("points : 100")
           st.write("---")
           st.title("Question 37")
           st.write("""
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

INPUT FORMAT:
 String 

OUTPUT FORMAT:
 Array of strings.


TEST CASE 1:

Input: s = "25525511135"

Output: ["255.255.11.135","255.255.111.35"]

TEST CASE 2:

Input: s = "0000"

Output: ["0.0.0.0"]
""")
           st.subheader("Base price 15,000")
           st.subheader("points : 100")
           st.write("---")
           st.title("Question 38")
           st.write("""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

INPUT FORMAT: 
String

OUTPUT FORMAT:
String

TEST CASE 1:

Input: s = "tree"

Output: "eert"

TEST CASE 2:

Input: s = "cccaaa"

Output: "aaaccc"


""")
           st.subheader("Base price 10,000")
           st.subheader("points : 75")
           st.write("---")
           st.title("Question 39")
           st.write("""
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

TEST CASE 1:

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
 
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

TEST CASE 2:

Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]

Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]


""")        
           st.image(img_q38)
           st.subheader("Base price 15,000")
           st.subheader("points : 100")
           st.write("---")
           st.title("Question 40")
           st.write("""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

TEST CASE 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]

Output: 6

TEST CASE 2:

Input: nums = [1]

Output: 1

""")
           st.subheader("Base price 15,000")
           st.subheader("points : 100")
           st.write("---")
           st.title("Question 41")
           st.write("""
You are given a $sorted$ list $A$ of size $N$.You have to make a new list $B$ such that $B[i]$ is equal to the number of elements $strictly$ $greater$ than $A[i]$ in the list $A$.

Print the $new$ $list$.

Input
The first line consists of $T$, denoting the number of test cases.

First line of each test case consists of one integer denoting $N$, where $N$ is the size of the list given to you.

Second line of each test case contains the list given to you containing $N$ elements.

Output
For each test case print the list in a single line and the elements of the list should be separated by $space$.

Print the answer to $each$ test case in a $new$ $line$.

Constraints
$1 \le T \le 100$ , where $T$ is the number of test cases.
$1 \le N \le 100$, where $N$ is the number of elements in the list.
$1 \le A[i] \le 1000000$ ,where $A[i]$ is the $ith$ element in the list given to you.
Subtasks
$15$ $points$: All the elements in the list given to you are distinct.
$35$ $points$: Original constraints: Elements can be repeated in the list.

Sample 1:

Input

2

4

1 2 4 4

5

1 2 2 2 2

Output

3 2 0 0

4 0 0 0 0



""")
           st.subheader("Base price : 8,000")
           st.subheader("points : 50")
           st.write("---")
           st.title("Question 42")
           st.write("""
Sergey has made N measurements. Now, he wants to know the average value of the measurements made.

In order to make the average value a better representative of the measurements, before calculating the average, he wants first to remove the highest K and the lowest K measurements. After that, he will calculate the average value among the remaining N - 2K measurements.

Could you help Sergey to find the average value he will get after these manipulations?

Input
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.

The first line of each test case contains two space-separated integers N and K denoting the number of measurements and the number of the greatest and the lowest values that will be removed.

The second line contains N space-separated integers A1, A2, ..., AN denoting the measurements.

Output
For each test case, output a single line containing the average value after removing K lowest and K greatest measurements.

Your answer will be considered correct, in case it has absolute or relative error, not exceeding 10-6.

Constraints
1 ≤ T ≤ 100
1 ≤ N ≤ 104
0 ≤ 2K < N
-106 ≤ Ai ≤ 106
Subtasks
Subtask #1 (50 points): K = 0
Subtask #2 (50 points): no additional constraints
Sample 1:

Input

3

5 1

2 9 -10 25 1

5 0

2 9 -10 25 1

3 1

1 1 1

Output

4.000000

5.400000

1.000000
""")
           st.subheader("Base price : 10,000")
           st.subheader("points : 75")
           st.write("---")
           st.title("Question 43")
           st.write("""
Chef is very fond of horses. He enjoys watching them race. As expected, he has a stable full of horses. He, along with his friends, goes to his stable during the weekends to watch a few of these horses race. Chef wants his friends to enjoy the race and so he wants the race to be close. This can happen only if the horses are comparable on their skill i.e. the difference in their skills is less.

There are N horses in the stable. The skill of the horse i is represented by an integer S[i]. The Chef needs to pick 2 horses for the race such that the difference in their skills is minimum. This way, he would be able to host a very interesting race. Your task is to help him do this and report the minimum difference that is possible between 2 horses in the race.

Input:
First line of the input file contains a single integer T, the number of test cases.
Every test case starts with a line containing the integer N.
The next line contains N space separated integers where the i-th integer is S[i].

Output:
For each test case, output a single line containing the minimum difference that is possible.

Constraints:
1 ≤ T ≤ 10
2 ≤ N ≤ 5000
1 ≤ S[i] ≤ 1000000000

Sample 1:

Input

1

5

4 9 1 32 13

Output

3
""")
           st.subheader("Base price : 12,000")
           st.subheader("points 75")
           st.write("---")
           st.title('Question 44')
           st.write("""
[Chopsticks (singular: chopstick) are short, frequently tapered sticks used in pairs of equal length, which are used as the traditional eating utensils of China, Japan, Korea and Vietnam. Originated in ancient China, they can also be found in some areas of Tibet and Nepal that are close to Han Chinese populations, as well as areas of Thailand, Laos and Burma which have significant Chinese populations. Chopsticks are most commonly made of wood, bamboo or plastic, but in China, most are made out of bamboo. Chopsticks are held in the dominant hand, between the thumb and fingers, and used to pick up pieces of food.]

Retrieved from wikipedia

Actually, the two sticks in a pair of chopsticks need not be of the same length. A pair of sticks can be used to eat as long as the difference in their length is at most D. The Chef has N sticks in which the ith stick is L[i] units long. A stick can't be part of more than one pair of chopsticks. Help the Chef in pairing up the sticks to form the maximum number of usable pairs of chopsticks.

Input
The first line contains two space-separated integers N and D. The next N lines contain one integer each, the ith line giving the value of L[i].

Output
Output a single line containing the maximum number of pairs of chopsticks the Chef can form.

Constraints
1 ≤ N ≤ 100,000 (10 5 )
0 ≤ D ≤ 1,000,000,000 (10 9 )
1 ≤ L[i] ≤ 1,000,000,000 (10 9 ) for all integers i from 1 to N
Sample 1:

Input

5 2

1

3

3

9

4

Output

2
""")
           st.subheader("Base price 12,000")
           st.subheader("points 75")
           st.write("---")
           st.title("Question 45")
           st.write("""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6

Output: [1,2]

""")
           st.subheader("Base price : 12,000")
           st.subheader("points 75")
           st.write("---")
           st.title("Question 46")
           st.write("""
Choose any two colors. Let's denote their values by x and y.
Mix the color with value x into the color with value y. After the mixing, the value of the first color remains x, but the value of the second color changes to x + y.
Find the minimum number of mixing operations Chef needs to perform to make her colors beautiful.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the number of colors.
The second line contains N space-separated integers A1, A2, ..., AN denoting Chef's initial colors.
Output
For each test case, print a single line containing one integer — the minimum number of required mixing operations.

Constraints
1 ≤ T ≤ 10
1 ≤ N ≤ 105
1 ≤ Ai ≤ 109 for each valid i
Subtasks
Subtask #1 (30 points): 1 ≤ N ≤ 100

Subtask #2 (70 points): original constraints

Sample 1:

Input

2

3

1 2 3

3

2 1 2

Output

0

1
""")
           st.subheader("Base price : 12,000")
           st.subheader(" ponts 75")
           st.write("---")
           st.title("Question 47")
           st.write("""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]

Output: 2, nums = [1,2,_]

Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]

Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


""")
           st.subheader("Base price : 12,000")
           st.subheader("points : 75")
           st.write("---")
           st.title("Question 48")
           st.write("""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;

sort(nums, 0, k); // Sort the first k elements of nums

for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [3,2,2,3], val = 3

Output: 2, nums = [2,2,_,_]

Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2

Output: 5, nums = [0,1,4,0,3,_,_,_]

Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
""")
           st.subheader("Base price : 12,000")
           st.subheader("points 75")
           st.write("---")
           st.title('Question 49')
           st.write("""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5

Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2

Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7

Output: 4
""")
           st.subheader("Base price 12,000")
           st.subheader("points 75")
           st.write("---")
           st.title("Question 50")
           st.write("""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]

Output: [1,2,4]

Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]

Output: [4,3,2,2]

Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
""")
           st.subheader("base price 8,000")
           st.subheader("points : 50")
           st.write("---")
           st.title("Question 51")
           st.write("""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]

Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]

Output: [0,1,2]

""")
           st.subheader("Base price 8,000")
           st.subheader("points : 50")
           st.write("---")
           st.title("Question 52")
           st.write("""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

Output: [1,2,2,3,5,6]

Explanation: The arrays we are merging are [1,2,3] and [2,5,6].

The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0

Output: [1]

Explanation: The arrays we are merging are [1] and [].

The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1

Output: [1]

Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
""")
           st.subheader("Base price 8,000")
           st.subheader("points 50")
           st.title("Question 53")
           st.write("""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4
""")
           st.subheader("Base price 8,000")
           st.subheader("points 50")
           st.title("Question 54")
           st.write("""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]

Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]

Output: 0

Explanation: In this case, no transactions are done and the max profit = 0.

""")
           st.subheader("base price 8,000")
           st.subheader("points 50")
           st.write("---")
           st.title("Question 55")
           st.write("""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Example 2:

Input: nums = [1,2,3,4]

Output: false

""")
           st.subheader("base price 8,000")
           st.subheader("points 50")
           st.write("---")
           st.title("Question 56")
           st.write("""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1

Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2

Output: false

""")
           st.subheader("Base price 8,000")
           st.subheader("points 50")
           st.write("---")
           st.title("Question 57")
           st.write("""
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

 

Example 1:

Input: g = [1,2,3], s = [1,1]

Output: 1

Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
Example 2:

Input: g = [1,2], s = [1,2,3]

Output: 2

Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
""")
           st.subheader("Base price 8,000")
           st.subheader("points 50")
           st.write("---")
           st.title("Question 58")
           st.write("""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]

Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]

Output: [0]
""")
           st.subheader("base price : 8,000")
           st.subheader("points 50")
           st.write("---")
           st.title("Question 59")
           st.write("""

Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]

Output: 1

Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]

Output: 2

Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

""")
           st.subheader("Base price : 8,000")
           st.subheader("points 50")
           st.write("---")
           st.title("Question 60")
           st.write("""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]

Output: [5,6]

Example 2:

Input: nums = [1,1]

Output: [2]
""")
           st.subheader("base price 8,000")
           st.subheader("points 50")
           st.write("---")
           st.title("Question 61")
           st.write("""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]

Output: 3

Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]

Output: 2
""")
           st.subheader("base price 8,000")
           st.subheader("points 50")
           st.write("---")
           st.title("Question 62")
           st.write("""
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:

Input: matrix = [[1,2,3],[4,5,6]]

Output: [[1,4],[2,5],[3,6]]
""")
           st.subheader("Question 63")
           st.subheader("points 50")
           st.write("---")
           st.title("Question 63")
           st.write("""

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]

Output: [0,1,9,16,100]

Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]

Output: [4,9,9,49,121]
""")
           st.subheader("base price 8,0000")
           st.subheader("points : 50")
           st.title("Question 64")
           st.write("""
Team RCB has earned X points in the games it has played so far in this year's IPL. To qualify for the playoffs they must earn at least a total of Y points. They currently have Z games left, in each game they earn 2 points for a win, 1 point for a draw, and no points for a loss.
Is it possible for RCB to qualify for the playoffs this year?
Input Format
First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of a single line of input, three integers X,Y,Z.
Output Format
For each test case, output in one line YES if it is possible for RCB to qualify for the playoffs, or NO if it is not possible to do so.
Output is case insensitive, which means that "yes", "Yes", "YEs", "no", "nO" - all such strings will be acceptable
Input

3

4   10   8

3    6    1

4    8    2

Output

YES

NO

YES
""")
           st.subheader("base price 6,000")
           st.subheader("Points 30")
           st.write("---")
           st.title("Question 65")
           st.write("""
Chef's phone shows a Battery Low notification if the battery level is 15% or less . Given that the battery level of Chef's phone is  X%, determine whether it would show a Battery low notification.
Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains a single line of input, an integer  X, denoting the battery level of the phone. 
Output Format
For each test case, output in a single line  Yes, if the battery level is  15% or below.
Otherwise, print No.
You may print each character of  Yes and No in uppercase or lowercase (for example, YES,  yes, YeS will be considered identical).

Input

3

15

3

65

Output

Yes

Yes

No

""")
           st.subheader("base price 6,000")
           st.subheader("Points 30")
           st.write("---")
           st.title("Question 66")
           st.write("""
Chef categorises an instagram account as spam, if, the following count of the account is more than 10 times the count of followers.
Given the following and follower count of an account as X and Y respectively, find whether it is a spam account.
Input Format
The first line of input will contain a single integer T,denoting the number of test cases.
Each test case consists of two space-separated integers X and Y - the following and follower count of an account, respectively.
Output Format
For each test case, output on a new line, YES, if the account is spam and NO otherwise.
You may print each character of the string in uppercase or lowercase. For example, the strings YES, yes, Yes and yES are identical.

Input

4

1     10

10    1

11    1

97    7

Output

NO

NO

YES
""")
           st.subheader("base price 6,0000")
           st.subheader("points 30")
           st.write("---")
           st.title("Question 67")
           st.write("""
Alice, Bob, and Charlie are contributing to buy a Netflix subscription. However, Netflix allows only two users to share a subscription.
Given that Alice, Bob, and Charlie have A,B,and C rupees respectively and a Netflix subscription costs X rupees, find whether any two of them can contribute to buy a subscription.
Input Format
The first line of input will contain a single integer T ,denoting the number of test cases.
Each test case contains four space-separated integers A,B,C , and X the amount that Alice, Bob, and Charlie have, and the cost of a Netflix subscription respectively.
Output Format
For each test case, output YES, if any two of Alice, Bob, and Charlie can contribute to buy a Netflix subscription or NO otherwise.
You may print each character in uppercase or lowercase. For example, NO, no, No, and nO are all considered identical.
Input

4

1 1 1 3

2 3 1 5

4 2 3 4

2 1 4 7

Output

NO

YES

YES

NO

 """)
           st.subheader("base price 8,000")
           st.subheader("points 50")
           st.write("---")
           st.title("Question 68")
           st.write("""
Apple considers any iPhone with a battery health of 80% or above, to be in optimal condition.
Given that your iPhone has X%  battery health, find whether it is in optimal condition.
Input Format
The first line of input will contain a single integer T,denoting the number of test cases.
The first and only line of each test case contains an integer  X — the battery health.
Output Format
For each test case, output on a new line, YES, if the battery is in optimal condition, and NO otherwise.
You may print each character in uppercase or lowercase. For example, NO, no, No and nO, are all considered identical.

Input

4

97

42

80

10

Output

YES

NO

YES

NO

""")
           st.subheader("Base price 6,000")
           st.subheader("points 50")
           st.write("---")
           st.title("Question 69")
           st.write("""
Bob and Alice are having a lockout match between them. There are three problems in the contest worth A,B and C points respectively. Only the first player to solve a problem gets points for that problem. It is impossible for Bob and Alice to solve a problem at the same time. Chef wants to know if there is any chance of a draw if Bob and Alice manage to solve 3 problems. A draw occurs when both players end with equal number of points.
Input Format
First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of a single line of input, three space separated integers A,B and C.
Output Format
For each testcase, output YES if the match can end in a draw, and NO otherwise.
You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).
Input

3

2   5   2

4   2   2

3   5   5

Output

NO

YES

NO

""")
           st.subheader("Base price 6,000")
           st.subheader("points 50")
           st.write("---")
           st.title("Question 70")
           st.write("""
Given the list of numbers, you are to sort them in non decreasing order.
Input
t – the number of numbers in list, then t lines follow [t <= 10^6].
Each line contains one integer: N [0 <= N <= 10^6]
Output
Output given numbers in non decreasing order.
Sample 1:

Input

5

5

3

6

7

1

Output

1

3

5

6

7
""")
           st.subheader("Base price 6,000")
           st.subheader("points 50")
           st.write("---")
           st.title("Question 71")
           st.write(""""
School holidays come in Berland. The holidays are going to continue for n days. The students of school are having the time of their lives and the IT teacher Marina Sergeyevna, who has spent all the summer busy checking the BSE (Berland State Examination) results, has finally taken a vacation break! Some people are in charge of the daily watering of flowers in shifts according to the schedule. However when Marina Sergeyevna was making the schedule, she was so tired from work and so lost in dreams of the oncoming vacation that she perhaps made several mistakes. In fact, it is possible that according to the schedule, on some days during the holidays the flowers will not be watered or will be watered multiple times. Help Marina Sergeyevna to find a mistake.
Input
The first input line contains two numbers n and m (1 ≤ n, m ≤ 100) — the number of days in Berland holidays and the number of people in charge of the watering respectively. The next m lines contain the description of the duty schedule. Each line contains two integers ai and bi (1 ≤ ai ≤ bi ≤ n), meaning that the i-th person in charge should water the flowers from the ai-th to the bi-th day inclusively, once a day. The duty shifts are described sequentially, i.e. bi ≤ ai + 1 for all i from 1 to n - 1 inclusively.
Output
Print "OK" (without quotes), if the schedule does not contain mistakes. Otherwise you have to find the minimal number of a day when the flowers will not be watered or will be watered multiple times, and output two integers — the day number and the number of times the flowers will be watered that day.
Example 1

Input

6 2

1 5

6 6

Output

OK

Example 2

Input

10 1

2 3

Output

1 0
""")
           st.subheader("Question 72")
           st.subheader("points 50")
           st.write("---")
           st.title("Question 73")
           st.write(""""
Q50
Chef is very fond of horses. He enjoys watching them race. As expected, he has a stable full of horses. He, along with his friends, goes to his stable during the weekends to watch a few of these horses race. Chef wants his friends to enjoy the race and so he wants the race to be close. This can happen only if the horses are comparable on their skill i.e. the difference in their skills is less.
There are N horses in the stable. The skill of the horse i is represented by an integer S[i]. The Chef needs to pick 2 horses for the race such that the difference in their skills is minimum. This way, he would be able to host a very interesting race. Your task is to help him do this and report the minimum difference that is possible between 2 horses in the race.
Input:

First line of the input file contains a single integer T, the number of test cases.
Every test case starts with a line containing the integer N.
The next line contains N space separated integers where the i-th integer is S[i].
Output:

For each test case, output a single line containing the minimum difference that is possible.
Constraints:

1 ≤ T ≤ 10
2 ≤ N ≤ 5000
1 ≤ S[i] ≤ 1000000000

Sample 1:

Input

1
5
4 9 1 32 13

Output

3

""")
           st.subheader("Base price 6,000")
           st.subheader("points 50")
           st.write("---")





           

           















           














           st.subheader("All the Best")
if selected == "Contact":
    st.subheader(" for coding related Contact : RISHI(8106864393),KARTHIK(8790514616)")
    st.subheader("HARIKA(77497795),SHAFI(7997465110)")
    st.subheader("For bidding details contact : NITHIN(7386158247),KAVYA(7386991562)")
    st.subheader("FOR MORE DETAILS : RISHI@HOST(8106864393)")





    
