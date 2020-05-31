# PublicTransportation
PROJECT BRIEF (WIA2005 - Algorithm Analysis and Design)
University/Programme/Course: 	University of Malaya/Bachelor of Computer Science/Algorithm Analysis and Design
Year: 2nd year / 4th semester
Pedagogical Approach: Project-based Learning
Learning Outcome:
Experience analysing and designing algorithms for problem solving with other team mates.
a.	Utilise all of the chosen tools
b.	Apply algorithms that have been learned in this course to solve the given problems
c.	Explore at least one new algorithm to solve the given problem.
d.	Integrate all of the algorithms within a computer program.
e.	Execute the computer program while explaining the relation between steps in algorithms with the behavior/output of the computer program.
f.	Analyse the complexity main algorithms that solve the given problem.
g.	Function effectively as a team member.
h.	Communicate effectively through reports and presentation.

Objective:
This project requires you and your team mates to analyse, design, and code a computer program using python and the chosen tools to solve the given problems.

Project Scope:
To meet the project requirement, you will need to:
	Form a work team of 6 members (must be within the same tutorial group).
	Elect a team leader, write contract item and sign using the group contract template in Appendix A.
	Identify clear roles and responsibilities, distributing and coordinating various tasks appropriately, and able to operate as a high performing team. You must clearly communicate how you have worked as a team. Refer FILA form at Appendix B.
	Analyse, design, and code a computer program using python and the chosen tools to solve the given problems as the following:-
 
One of the essences of computer science and information technology is to solve problem faced by human-kind. As the outcome of this project, you are required develop a computer program that is able to resolve the following problems:-
Problem 1: Malaysia has developed an integrated public transportation network which provides multiple options to passenger. Passenger may take the furthest route due to the lack of information on determining the combination of public transportation to get to their destination.
1.	Get and mark locations of stops (example origin location, airport, bus stop, taxi stand, grab pick up/drop-off spot, etc) to reach a destination in Malaysia. Enumerate 5-10 options to get from one origin location to one destination. Each option needs to have combination of at least 3 types of transportations.
Example to get from University of Malaya to the Penang National Part in the Penang Island.

Option 1:  Bus stop to Subang airport, Flight to Penang International Airport, Taxi to the Penang National Part.
Option 2:

Option 3:
...
Option n:
a.	Guide 1: you can use Python Geocoding Toolbox
Look up: https://pypi.python.org/pypi/geopy#downloads
b.	Guide 2: you can use gmplot
Lookup: https://github.com/vgm64/gmplot 
2.	Get the distances between these stops.
a.	Guide 1: you can use Python Geocoding Toolbox
b.	Suggestion 2: you should use Google Distance Matrix API
i.	Login to the google developer’s website and follow through the examples. It is important that you know how to use the API key given to you within the code that you are going to use. Refer to this link: https://developers.google.com/maps/documentation/distance-matrix/start
3.	Identify the option with the shortest path: Use one of the algorithms for shortest path, get the minimum distance to arrive to the destination using at least 3 types of transportation.

4.	Plot line to illustrate the origin location, stops and the destination based on the option chosen in step 3.
a.	Guide1:  you can use google.maps.Polyline. You can refer to this link:
https://www.sitepoint.com/create-a-polyline-using-the-geolocation-and-the-google-maps-api/
Problem 2: Even the shortest path able to be determine, passengers are still facing daily problem due to the long waiting time. The unusual and unexpected condition during the journey such as unexpected traffic congestion, unexpected delay, randomness in passengers’ demands OR weather changes need to be considered before making suggestion.

5.	Extract information about public transportation from the internet. (For example, traffic information website, new papers). Count the number of words in the webpages.
a.	Sometimes a webpage must be converted to the text version before it can be done
i.	Guide 1: You may refer to this website to extract word from a website
https://www.textise.net/ 
b.	Guide 2: You may refer to this website on how to count word frequency in a website
https://programminghistorian.org/lessons/counting-frequencies 
c.	You can also filter stops words from the text you found
i.	Guide 3: Stops words are such as conjunctions and prepositions. You may refer to this link: https://www.ranks.nl/stopwords 
ii.	Program using any String Matching algorithm to find and delete the stop words.
6.	Plot line/scatter/histogram graphs related to the word count using Plotly (Word count, stop words)
d.	Guide 3: You may refer this link on how to install Plotly and how to use the API keys
 http://www.instructables.com/id/Plotly-with-Python/ 
https://plot.ly/python/getting-started/ 
7.	Compare words in the webpages with the positive, negative and neutral English words using a String Matching algorithm
e.	Guide 4: Use the following word as positive and negative English words
http://positivewordsresearch.com/list-of-positive-words/
http://positivewordsresearch.com/list-of-negative-words/ 
f.	Put these words in a text file for you to access them in your algorithm
g.	Words that are not in the list can be considered as neutral
8.	Plot histogram graphs of positive and negative words found in the webpages.
h.	Guide 5: Use Plotly
9.	Give a conclusion regarding the sentiment of those articles
i.	Guide 6: If there are more positive words, conclude that the article is giving positive sentiment, if there are more negative words, conclude that the article is giving negative sentiment.
j.	You may try to conclude in different perspectives such as whether the list of positive and negative words above is accurate to be used in the context of the article you extracted the text.
k.	Based on the conclusion, you may say that each of the public transportation has positive or negative sentiment.

Problem 3: The hassle question faced by passengers to decide which options should be taken depending on the time and situation. For example, “Should I wait for the bus at this time, or should I walk a few miles to the train station, or should I just take a grab as the traffic at this time may not be congested”
10.	Develop an algorithm to automatically generate summary of the 5-10 options based on their respective distance and sentiment. Then, the algorithm should be able to recommend the best option based on the distance AND the sentiment for the passenger to travel from one destination to another destination. 

	Week 5: Only group leader has to submit the following in a .zip file through Spectrum:
	Group Contract
	1st FILA form (compulsory to all members to develop the program)
	Week 5-12: Analyse, design, and code a computer program using python and the chosen tools to solve the given problems.
	Week 12:Each student needs to individually submit the peer evaluation form through Spectrum. Your peer evaluation is confidential and will not be exposed to other team members.
	Week 13-14:Each group has to do 20-30 minutes presentation using the power point slide.
	Week 14: One final submission for each group. Only group leader has to submit following in a .zip file through Spectrum:
	Source code: raw python files (All programming codes must use python 2 or 3)
	2nd FILA form (compulsory to all members to develop the program)
	Report Content: 
1.	Introduction
2.	Description 
- Include the description of the project with Control flow graph (CFG)
- Elaborate how tools and algorithms resolve each of the given problems.
- Highlight at least one new algorithm that has NOT been taught in this course to solve the given problems
3.	Time complexity of each of the algorithm that resolve the given problem
4.	The program code: source code and snapshots of input/output
5.	Conclusion
6.	References

Assessment Criteria:
The assessment for this group project is divided into two categories:
o	Assessment criteria for soft skill as described  in Table 1
o	Assessment criteria for algorithms in solving the given problems as described in Table 2

Table 1:  Assessment criteria for soft skill (Individual Assessment)
 	 	Partially meets	Meets	Exceeds	Exemplary
Skill level	                Score Description	1	2	3-4	5
CS1 (KIM)

Presentation (2%)	The ability to present ideas clearly, effectively and confidently, in both oral, written forms 
Oral
Parameters:
•	delivery, 
•	projection (pace, volume,enunciation)
•	appearance (attire and demeanor) 	Either one parameter is acceptable.	All parameters are acceptable.	Some parameters  are exceptional.	All parameters  are exceptional.
TS4

FILA form (3%)	The ability to contribute towards:
•	planning, 
•	coordination
 of the team’s efforts	Student is able to  contribute towards any one task	Student is able to feasibly contribute towards both tasks.	Student is able to contribute towards both tasks well.	Student is  consistently able to contribute towards both tasks excellently.

 
Table 2:  Assessment criteria for algorithms in solving the given problems (Group Assessment)
Criteria	Scoring
Accuracy / Content Knowledge 	5	4	3	2-1
	All algorithms and the usage of tools are presented, execute without error and output appears to be accurate.	Almost all algorithms and the usage of tools are presented, execute without error and output appears to be accurate.	Most algorithms and the usage of tools are presented, without error but output appears to be less accurate.	Some algorithms and the usage of tools are presented, execute with minor/major error, resolve with hard-codes, output appears to be accurate.
-Algorithm to resolve Problem 1 (5%)				
-Algorithm to resolve Problem 2(5%)				
-Algorithm to resolve Problem 3 (5%)				
Integration between items (5%)	5	4	3-2	1-0
	The entire system appears to be integrated 	Most system appears to be integrated	Some system appears to be integrated with some hard-coding	Minor integration between items 1-10 with hard-coding
Include new algorithm that is not taught in the course (5%)	5-4	3-1	0
	At least one new algorithm that resolve the main problem (Example shortest distance, string matching) adopted/created	At least one new algorithm that resolve the sub- problem	None



 
Appendix A

Semester 2 2019/2020	WIA2005 : ALGORITHMS ANALYSIS AND DESIGN 
GROUP CONTRACT  

A team of at most 6 students to 
●	Declare and identify individual strength
●	Identify individual role in the team
●	Agreed on meeting time, venue, communication means and approaches to arrives at any decisions
●	Develop team / group social contact
Deliverable / To submit
Each member role and contract
Group Leader : 
Contract Item:  As a Team we agree to 

●	Participation 	






●	Communication 	






●	Meetings 	






●	Conduct 	






●	Deadlines 	






●	Conflict 	









Clause
In any violation of the above, we agree 	
























Please ensure that the items in the clause is effective and feasible.


No	Matric No	Name	Team Role	Signature
				
				
				
				
				
				

	

(Assessor:                                                                                                              Date Received:                             )


 
Appendix B
FILA FORM – University of Malaya 
 FACTS 	IDEAS 	LEARNING ISSUES 	ACTION 	DATELINE 
What we know about the task 	What do we need to find out? 	Who is going to do it? 

- The phases or process to develop or model the system 
- Integrate theory and practical 
	
- To analyze and translated the theory into practical or real scenario 
- To transfer the knowledge and suited with various of industries and provide the solution and improvement 
	
- Activities and group discussion 
- Find research information through internet or library 
	immediately 



 

