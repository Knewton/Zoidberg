
[('Jane', 'context', (u'singular', u'feminine')), ('has', 'operator', None), ('14', 'constant', None), ('balloons', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Jane', 'context', (u'singular', u'feminine')), ('buys', 'operator', None), ('another', u'noise', None), ('6', 'constant', None), ('balloons', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('balloons', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Jane', 'context', (u'singular', u'feminine')), ('have', 'q_stop', None), (('now', 'RB'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Jane has 14 balloons. She buys another 6 balloons. How many balloons does she have now?

## Digested problem
    Jane    	has     	14      	balloons	.       
    NNP     	VBZ     	CD      	NNS     	.       

    She     	buys    	another 	6       	balloons	.       
    PRP     	VBZ     	DT      	CD      	NNS     	.       

    How     	many    	balloons	does    	she     	have    	now     	?       
    WRB     	JJ      	NNS     	VBZ     	PRP     	VB      	RB      	.       

## Problem inference
I think this problem is about Jane getting balloons and asks a single question.

## Parsed problem
    Jane       	has        	14         	balloons   	.          
    context    	operator   	constant   	unit       	punctuation

    Jane       	buys       	another    	6          	balloons   	.          
    context    	operator   	noise      	constant   	unit       	punctuation

    How many   	balloons   	does       	Jane       	have       	now        	?          
    asking     	unit       	q_start    	context    	q_stop     	subordinate	punctuation


## Question 1

### Question text
How many balloons does she have now?

### Answer interpretation
The answer is the unknown value of balloons owned by Jane at the end of the problem.

## Data extraction

### Sentence 1
balloons owned by Jane = 14

### Sentence 2
balloons owned by Jane + 6

## Correct response
20 balloons

***

[('Mrs. Jones', 'context', (u'singular', u'feminine')), ('bought', 'operator', None), ('some', u'dynamic_variable', None), ('bananas', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[("Mrs. Jones' family", 'context', (u'plural', u'mixed')), ('ate', 'operator', None), ('5', 'constant', None), ('bananas', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Mrs. Jones', 'context', (u'singular', u'feminine')), ('gave', 'operator', None), ('the', u'noise', None), ('remaining', u'solution_zero', None), ('4', 'constant', None), ('bananas', 'unit', (u'plural', u'neutral')), ('to', 'conjunction', None), ("Mrs. Jones' friends", 'context', (u'plural', u'mixed')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('bananas', 'unit', (u'plural', u'neutral')), ('did', 'q_start', None), ('Mrs. Jones', 'context', (u'singular', u'feminine')), ('buy', 'q_stop', None), ('in', 'conjunction', None), ('the', u'noise', None), (('beginning', 'SUB'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Mrs. Jones bought some bananas. Her family ate 5 bananas. She gave the remaining 4 bananas to her friends. How many bananas did she buy in the beginning?

## Digested problem
    Mrs.     	Jones    	bought   	some     	bananas  	.        
    NNP      	NNP      	VBD      	DT       	NNS      	.        

    Her      	family   	ate      	5        	bananas  	.        
    PRP$     	NN       	NN       	CD       	NNS      	.        

    She      	gave     	the      	remaining	4        	bananas  	to       	her      	friends  	.        
    PRP      	VBD      	DT       	VBG      	CD       	NNS      	TO       	PRP$     	NNS      	.        

    How      	many     	bananas  	did      	she      	buy      	in       	the      	beginning	?        
    WRB      	JJ       	NNS      	VBD      	PRP      	VB       	IN       	DT       	NN       	.        

## Problem inference
I think this problem is about Mrs. Jones, Mrs. Jones' family, and Mrs. Jones' friends exchanging bananas and asks a single question.

## Parsed problem
    Mrs. Jones         	bought             	some               	bananas            	.                  
    context            	operator           	dynamic_variable   	unit               	punctuation        

    Mrs. Jones' family 	ate                	5                  	bananas            	.                  
    context            	operator           	constant           	unit               	punctuation        

    Mrs. Jones         	gave               	the                	remaining          	4                  	bananas            	to                 	Mrs. Jones' friends	.                  
    context            	operator           	noise              	solution_zero      	constant           	unit               	conjunction        	context            	punctuation        

    How many           	bananas            	did                	Mrs. Jones         	buy                	in                 	the                	beginning          	?                  
    asking             	unit               	q_start            	context            	q_stop             	conjunction        	noise              	subordinate        	punctuation        


## Question 1

### Question text
How many bananas did she buy in the beginning?

### Answer interpretation
The answer is the unknown value of bananas gained by Mrs. Jones at the beginning of the problem.

## Data extraction

### Sentence 1
bananas owned by Mrs. Jones + x

### Sentence 2
bananas owned by Mrs. Jones - 5

### Sentence 3
bananas owned by Mrs. Jones - 4
bananas owned by Mrs. Jones == 0
bananas owned by Mrs. Jones' friends + 4

## Correct response
9 bananas

***

[('Tony', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('19', 'constant', None), ('jars', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Tony', 'context', (u'singular', u'masculine')), ('gives', 'operator', None), ('16', 'constant', None), ('jars', 'unit', (u'plural', u'neutral')), ('to', 'conjunction', None), ("Tony's sister", 'context', (u'singular', u'feminine')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('jars', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Tony', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), (('now', 'RB'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Tony has 19 jars. He gives 16 jars to his sister. How many jars does he have now?

## Digested problem
    Tony  	has   	19    	jars  	.     
    NNP   	VBZ   	CD    	NNS   	.     

    He    	gives 	16    	jars  	to    	his   	sister	.     
    PRP   	VBZ   	CD    	NNS   	TO    	PRP$  	NN    	.     

    How   	many  	jars  	does  	he    	have  	now   	?     
    WRB   	JJ    	NNS   	VBZ   	PRP   	VB    	RB    	.     

## Problem inference
I think this problem is about Tony and Tony's sister jars and asks a single question.

## Parsed problem
    Tony           	has            	19             	jars           	.              
    context        	operator       	constant       	unit           	punctuation    

    Tony           	gives          	16             	jars           	to             	Tony's sister  	.              
    context        	operator       	constant       	unit           	conjunction    	context        	punctuation    

    How many       	jars           	does           	Tony           	have           	now            	?              
    asking         	unit           	q_start        	context        	q_stop         	subordinate    	punctuation    


## Question 1

### Question text
How many jars does he have now?

### Answer interpretation
The answer is the unknown value of jars owned by Tony at the end of the problem.

## Data extraction

### Sentence 1
jars owned by Tony = 19

### Sentence 2
jars owned by Tony - 16
jars owned by Tony's sister + 16

## Correct response
3 jars

***

[('Lucy', 'context', (u'singular', u'feminine')), ('has', 'operator', None), ('8', 'constant', None), ('dolls', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Ethelle', 'context', (u'singular', u'feminine')), ('has', 'operator', None), ('4', 'constant', None), ('more', u'rel_more', None), ('dolls', 'unit', (u'plural', u'neutral')), ('than', 'conjunction', None), (('Lucy', (u'singular', u'feminine')), 'comparator_context', (u'singular', u'feminine')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('dolls', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Ethelle', 'context', (u'singular', u'feminine')), ('have', 'q_stop', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Lucy has 8 dolls. Ethelle has 4 more dolls than her. How many dolls does Ethelle have?

## Digested problem
    Lucy   	has    	8      	dolls  	.      
    NNP    	VBZ    	CD     	NNS    	.      

    Ethelle	has    	4      	more   	dolls  	than   	her    	.      
    NNP    	VBZ    	CD     	JJR    	NNS    	IN     	PRP$   	.      

    How    	many   	dolls  	does   	Ethelle	have   	?      
    WRB    	JJ     	NNS    	VBZ    	NNP    	VB     	.      

## Problem inference
I think this problem is about Lucy and Ethelle grouping dolls and asks a single question.

## Parsed problem
    Lucy              	has               	8                 	dolls             	.                 
    context           	operator          	constant          	unit              	punctuation       

    Ethelle           	has               	4                 	more              	dolls             	than              	Lucy              	.                 
    context           	operator          	constant          	rel_more          	unit              	conjunction       	comparator_context	punctuation       

    How many          	dolls             	does              	Ethelle           	have              	?                 
    asking            	unit              	q_start           	context           	q_stop            	punctuation       


## Question 1

### Question text
How many dolls does Ethelle have?

### Answer interpretation
The answer is the unknown value of dolls owned by Ethelle.

## Data extraction

### Sentence 1
dolls owned by Lucy = 8

### Sentence 2
dolls owned by Ethelle = 8
dolls owned by Ethelle + 4

## Correct response
12 dolls

***

[('Joey', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('13', 'constant', None), ('toy cars', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Chandler', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('6', 'constant', None), ('toy cars', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('fewer', u'rel_less', None), ('toy cars', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Chandler', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), ('than', 'conjunction', None), (('Joey', (u'singular', u'masculine')), 'comparator_context', (u'singular', u'masculine')), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Joey has 13 toy cars. Chandler has 6 toy cars. How many fewer toy cars does Chandler have than Joey?

## Digested problem
    Joey    	has     	13      	toy     	cars    	.       
    NNP     	VBZ     	CD      	NN      	NNS     	.       

    Chandler	has     	6       	toy     	cars    	.       
    NNP     	VBZ     	CD      	NN      	NNS     	.       

    How     	many    	fewer   	toy     	cars    	does    	Chandler	have    	than    	Joey    	?       
    WRB     	JJ      	JJR     	NN      	NNS     	VBZ     	NNP     	VB      	IN      	NNP     	.       

## Problem inference
I think this problem is about Joey and Chandler grouping toy cars and asks a single question.

## Parsed problem
    Joey              	has               	13                	toy cars          	.                 
    context           	operator          	constant          	unit              	punctuation       

    Chandler          	has               	6                 	toy cars          	.                 
    context           	operator          	constant          	unit              	punctuation       

    How many          	fewer             	toy cars          	does              	Chandler          	have              	than              	Joey              	?                 
    asking            	rel_less          	unit              	q_start           	context           	q_stop            	conjunction       	comparator_context	punctuation       


## Question 1

### Question text
How many fewer toy cars does Chandler have than Joey?

### Answer interpretation
The answer is the difference in value of toy cars owned by Chandler with respect to Joey.

## Data extraction

### Sentence 1
toy cars owned by Joey = 13
toy cars owned by Joey + 13

### Sentence 2
toy cars owned by Chandler = 6
toy cars owned by Chandler + 6

## Correct response
14 toy cars

***

[('Marc', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('10', 'constant', None), ('apples', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Marc', 'context', (u'singular', u'masculine')), ('throws', 'operator', None), ('2', 'constant', None), ('apples', 'unit', (u'plural', u'neutral')), ('away', u'noise', None), ('.', 'punctuation', None)]
[('Marc', 'context', (u'singular', u'masculine')), ('gives', 'operator', None), ('2', 'constant', None), ('apples', 'unit', (u'plural', u'neutral')), ('to', 'conjunction', None), ('Jim', 'context', (u'singular', u'masculine')), ('.', 'punctuation', None)]
[('Marc', 'context', (u'singular', u'masculine')), ('gives', 'operator', None), ('3', 'constant', None), ('apples', 'unit', (u'plural', u'neutral')), ('to', 'conjunction', None), ('Julia', 'context', (u'singular', u'feminine')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('apples', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Marc', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), (('now', 'RB'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Marc has 10 apples.
He throws 2 apples away.
He gives 2 apples to Jim.
Marc gives 3 apples to Julia.
How many apples does Marc have now?

## Digested problem
    Marc  	has   	10    	apples	.     
    NNP   	VBZ   	CD    	NNS   	.     

    He    	throws	2     	apples	away  	.     
    PRP   	VBZ   	CD    	NNS   	RB    	.     

    He    	gives 	2     	apples	to    	Jim   	.     
    PRP   	VBZ   	CD    	NNS   	TO    	NNP   	.     

    Marc  	gives 	3     	apples	to    	Julia 	.     
    NNP   	VBZ   	CD    	NNS   	TO    	NNP   	.     

    How   	many  	apples	does  	Marc  	have  	now   	?     
    WRB   	JJ    	NNS   	VBZ   	NNP   	VB    	RB    	.     

## Problem inference
I think this problem is about Marc, Jim, and Julia exchanging apples and asks a single question.

## Parsed problem
    Marc       	has        	10         	apples     	.          
    context    	operator   	constant   	unit       	punctuation

    Marc       	throws     	2          	apples     	away       	.          
    context    	operator   	constant   	unit       	noise      	punctuation

    Marc       	gives      	2          	apples     	to         	Jim        	.          
    context    	operator   	constant   	unit       	conjunction	context    	punctuation

    Marc       	gives      	3          	apples     	to         	Julia      	.          
    context    	operator   	constant   	unit       	conjunction	context    	punctuation

    How many   	apples     	does       	Marc       	have       	now        	?          
    asking     	unit       	q_start    	context    	q_stop     	subordinate	punctuation


## Question 1

### Question text
How many apples does Marc have now?

### Answer interpretation
The answer is the unknown value of apples owned by Marc at the end of the problem.

## Data extraction

### Sentence 1
apples owned by Marc = 10

### Sentence 2
apples owned by Marc - 2

### Sentence 3
apples owned by Jim + 2
apples owned by Marc - 2

### Sentence 4
apples owned by Julia + 3
apples owned by Marc - 3

## Correct response
3 apples

***

[('8', 'constant', None), ('fish', 'context', None), ('are', 'pre_ind_plu', None), ('swimming', u'acting', None), ('in', 'conjunction', None), ('a', u'constant', None), (('pond', 'NN'), 'subordinate', (u'singular', u'neutral')), ('.', 'punctuation', None)]
[('4', 'constant', None), ('more', u'rel_more', None), ('fish', 'context', (u'regular', u'mixed')), ('join', 'operator', None), ('fish', 'context', (u'plural', u'mixed')), ('.', 'punctuation', None), (('pond', u'place_noun'), 'subordinate_inferred', (u'singular', u'neutral'))]
[('how many', 'asking', None), ('fish', 'context', (u'regular', u'mixed')), ('are', 'pre_ind_plu', None), ('swimming', u'acting', None), ('in', 'conjunction', None), ('the', u'noise', None), (('pond', 'NN'), 'subordinate', (u'singular', u'neutral')), (('now', 'RB'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
8 fish are swimming in a pond. 4 more fish join them.
How many fish are swimming in the pond now?

## Digested problem
    8       	fish    	are     	swimming	in      	a       	pond    	.       
    CD      	JJ      	NN      	VBG     	IN      	DT      	NN      	.       

    4       	more    	fish    	join    	them    	.       
    LS      	JJR     	JJ      	NN      	PRP     	.       

    How     	many    	fish    	are     	swimming	in      	the     	pond    	now     	?       
    WRB     	JJ      	JJ      	VBP     	VBG     	IN      	DT      	NN      	RB      	.       

## Problem inference
I think this problem is about an increasing number of swimming fish in a pond and asks a single question.

## Parsed problem
    8                   	fish                	are                 	swimming            	in                  	a                   	pond                	.                   
    constant            	context             	pre_ind_plu         	acting              	conjunction         	constant            	subordinate         	punctuation         

    4                   	more                	fish                	join                	fish                	.                   	pond                
    constant            	rel_more            	context             	operator            	context             	punctuation         	subordinate_inferred

    How many            	fish                	are                 	swimming            	in                  	the                 	pond                	now                 	?                   
    asking              	context             	pre_ind_plu         	acting              	conjunction         	noise               	subordinate         	subordinate         	punctuation         


## Question 1

### Question text
How many fish are swimming in the pond now?

### Answer interpretation
The answer is the unknown value of fish swimming in a pond at the end of the problem.

## Data extraction

### Sentence 1
swimming fish in a pond = 8

### Sentence 2
swimming fish in a pond + 4

## Correct response
12 fish

***

[('Michael', 'context', (u'singular', u'masculine')), ('had', 'operator', None), ('8', 'constant', None), ('pieces of pizza', 'unit', (u'singular', u'neutral')), ('.', 'punctuation', None)]
[('Michael', 'context', (u'singular', u'masculine')), ('ate', 'operator', None), ('2', 'constant', None), ('pieces of pizza', 'unit', (u'singular', u'neutral')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('pieces of pizza', 'unit', (u'singular', u'neutral')), ('did', 'q_start', None), ('Michael', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), (('left', 'SUB'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Michael had 8 pieces of pizza. He ate 2 pieces of pizza. How many pieces of pizza did Michael have left?

## Digested problem
    Michael	had    	8      	pieces 	of     	pizza  	.      
    NNP    	VBD    	CD     	NNS    	IN     	NN     	.      

    He     	ate    	2      	pieces 	of     	pizza  	.      
    PRP    	VBP    	CD     	NNS    	IN     	NN     	.      

    How    	many   	pieces 	of     	pizza  	did    	Michael	have   	left   	?      
    WRB    	JJ     	NNS    	IN     	NN     	VBD    	NNP    	VB     	VBN    	.      

## Problem inference
I think this problem is about Michael losing pieces of pizza and asks a single question.

## Parsed problem
    Michael        	had            	8              	pieces of pizza	.              
    context        	operator       	constant       	unit           	punctuation    

    Michael        	ate            	2              	pieces of pizza	.              
    context        	operator       	constant       	unit           	punctuation    

    How many       	pieces of pizza	did            	Michael        	have           	left           	?              
    asking         	unit           	q_start        	context        	q_stop         	subordinate    	punctuation    


## Question 1

### Question text
How many pieces of pizza did Michael have left?

### Answer interpretation
The answer is the unknown value of pieces of pizza owned by Michael at the end of the problem.

## Data extraction

### Sentence 1
pieces of pizza owned by Michael = 8

### Sentence 2
pieces of pizza owned by Michael - 2

## Correct response
6 pieces of pizza

***

[('Pigpen', 'context', (u'singular', u'masculine')), ('had', 'operator', None), ('some', u'dynamic_variable', None), ('rocks', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Pigpen', 'context', (u'singular', u'masculine')), ('kept', 'operator', None), ('3', 'constant', None), ('rocks', 'unit', (u'plural', u'neutral')), ('for', 'conjunction', None), ('Pigpen', 'context', (u'singular', u'masculine')), ('and', 'coordinating_conjunction', None), ('gave', 'operator', None), ('the', u'noise', None), ('remaining', u'solution_zero', None), ('8', 'constant', None), ('rocks', 'unit', (u'plural', u'neutral')), ('to', 'conjunction', None), ("Pigpen's friends", 'context', (u'plural', u'mixed')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('rocks', 'unit', (u'plural', u'neutral')), ('did', 'q_start', None), ('Pigpen', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), ('in', 'conjunction', None), ('the', u'noise', None), (('beginning', 'SUB'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Pigpen had some rocks.
He kept 3 rocks for himself and gave the remaining 8 rocks to his friends.
How many rocks did he have in the beginning?

## Digested problem
    Pigpen   	had      	some     	rocks    	.        
    NNP      	VBD      	DT       	NNS      	.        

    He       	kept     	3        	rocks    	for      	himself  	and      	gave     	the      	remaining	8        	rocks    	to       	his      	friends  	.        
    PRP      	VBD      	CD       	NNS      	IN       	PRP      	CC       	VBD      	DT       	VBG      	CD       	NNS      	TO       	PRP$     	NNS      	.        

    How      	many     	rocks    	did      	he       	have     	in       	the      	beginning	?        
    WRB      	JJ       	NNS      	VBD      	PRP      	VBP      	IN       	DT       	NN       	.        

## Problem inference
I think this problem is about Pigpen and Pigpen's friends exchanging rocks and asks a single question.

## Parsed problem
    Pigpen                  	had                     	some                    	rocks                   	.                       
    context                 	operator                	dynamic_variable        	unit                    	punctuation             

    Pigpen                  	kept                    	3                       	rocks                   	for                     	Pigpen                  	and                     	gave                    	the                     	remaining               	8                       	rocks                   	to                      	Pigpen's friends        	.                       
    context                 	operator                	constant                	unit                    	conjunction             	context                 	coordinating_conjunction	operator                	noise                   	solution_zero           	constant                	unit                    	conjunction             	context                 	punctuation             

    How many                	rocks                   	did                     	Pigpen                  	have                    	in                      	the                     	beginning               	?                       
    asking                  	unit                    	q_start                 	context                 	q_stop                  	conjunction             	noise                   	subordinate             	punctuation             


## Question 1

### Question text
How many rocks did he have in the beginning?

### Answer interpretation
The answer is the unknown value of rocks owned by Pigpen at the beginning of the problem.

## Data extraction

### Sentence 1
rocks owned by Pigpen = x

### Sentence 2
rocks owned by Pigpen - 3
rocks owned by Pigpen's friends - 8
rocks owned by Pigpen's friends == 0

## Correct response
3 rocks

***

[('Mr. Lupis', 'context', (u'singular', u'masculine')), ('needs', 'operator', None), ('4', 'constant', None), ('eggs', 'unit', (u'plural', u'neutral')), ('to', 'conjunction', None), ('bake', 'operator', None), ('13', 'constant', None), (('muffins', 'NNS'), 'subordinate', None), ('.', 'punctuation', None)]
[('Mr. Lupis', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('only', u'noise', None), ('2', 'constant', None), ('eggs', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None), (('muffins', None), 'subordinate_inferred', None)]
[('how many', 'asking', None), ('more', u'rel_more', None), ('eggs', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Mr. Lupis', 'context', (u'singular', u'masculine')), ('need', 'q_stop', None), ('to', 'conjunction', None), ('bake', 'operator', None), ('the', u'noise', None), (('muffins', 'NNS'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Mr. Lupis needs 4 eggs to bake 13 muffins. He has only 2 eggs. How many more eggs does he need to bake the muffins?

## Digested problem
    Mr.    	Lupis  	needs  	4      	eggs   	to     	bake   	13     	muffins	.      
    NNP    	NNP    	VBZ    	CD     	NNS    	TO     	VB     	CD     	NNS    	.      

    He     	has    	only   	2      	eggs   	.      
    PRP    	VBZ    	RB     	CD     	NNS    	.      

    How    	many   	more   	eggs   	does   	he     	need   	to     	bake   	the    	muffins	?      
    WRB    	JJ     	RBR    	NNS    	VBZ    	PRP    	VBP    	TO     	VB     	DT     	NNS    	.      

## Problem inference
I think this problem is about Mr. Lupis eggs and asks a single question.

## Parsed problem
    Mr. Lupis           	needs               	4                   	eggs                	to                  	bake                	13                  	muffins             	.                   
    context             	operator            	constant            	unit                	conjunction         	operator            	constant            	subordinate         	punctuation         

    Mr. Lupis           	has                 	only                	2                   	eggs                	.                   	muffins             
    context             	operator            	noise               	constant            	unit                	punctuation         	subordinate_inferred

    How many            	more                	eggs                	does                	Mr. Lupis           	need                	to                  	bake                	the                 	muffins             	?                   
    asking              	rel_more            	unit                	q_start             	context             	q_stop              	conjunction         	operator            	noise               	subordinate         	punctuation         


## Question 1

### Question text
How many more eggs does he need to bake the muffins?

### Answer interpretation
The answer is the increase in value of eggs needed by Mr. Lupis to bake muffins.

## Data extraction

### Sentence 1
eggs needed by Mr. Lupis to bake muffins == 4

### Sentence 2
eggs owned by Mr. Lupis = 2

## Correct response
2 eggs

***

[('Mitch', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('3', 'constant', None), ('cobs of corn', 'unit', (u'singular', u'neutral')), ('.', 'punctuation', None)]
[('Lisa', 'context', (u'singular', u'feminine')), ('has', 'operator', None), ('2', 'constant', None), ('cobs of corn', 'unit', (u'singular', u'neutral')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('cobs of corn', 'unit', (u'singular', u'neutral')), ('do', 'q_start', None), ('Mitch and Lisa', 'context', (u'plural', u'mixed')), ('have', 'q_stop', None), (('altogether', 'RB'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Mitch has 3 cobs of corn. 
Lisa has 2 cobs of corn. 
How many cobs of corn do they have altogether?

## Digested problem
    Mitch     	has       	3         	cobs      	of        	corn      	.         
    NN        	VBZ       	CD        	NNS       	IN        	NN        	.         

    Lisa      	has       	2         	cobs      	of        	corn      	.         
    NNP       	VBZ       	CD        	NNS       	IN        	NN        	.         

    How       	many      	cobs      	of        	corn      	do        	they      	have      	altogether	?         
    WRB       	JJ        	NNS       	IN        	NN        	VBP       	PRP       	VBP       	RB        	.         

## Problem inference
I think this problem is about Mitch and Lisa grouping cobs of corn and asks a single question.

## Parsed problem
    Mitch         	has           	3             	cobs of corn  	.             
    context       	operator      	constant      	unit          	punctuation   

    Lisa          	has           	2             	cobs of corn  	.             
    context       	operator      	constant      	unit          	punctuation   

    How many      	cobs of corn  	do            	Mitch and Lisa	have          	altogether    	?             
    asking        	unit          	q_start       	context       	q_stop        	subordinate   	punctuation   


## Question 1

### Question text
How many cobs of corn do they have altogether?

### Answer interpretation
The answer is the unknown value of cobs of corn owned by Mitch and Lisa added together.

## Data extraction

### Sentence 1
cobs of corn owned by Mitch = 3

### Sentence 2
cobs of corn owned by Lisa = 2

## Correct response
5 cobs of corn

***

[('Mickey', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('12', 'constant', None), ('apples', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Eric', 'context', (u'singular', u'masculine')), ('takes', 'operator', None), ('away', u'noise', None), (u'0.5', 'variable_relationship', None), ('of', 'conjunction', None), ('the', u'noise', None), (('apples owned by Mickey', 'apples', 'Mickey', 'Eric'), 'context_unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('apples', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Mickey', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), (('now', 'RB'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Mickey has a dozen apples.
Eric takes away half of the apples.
How many apples does Mickey have now?

## Digested problem
    Mickey	has   	a     	dozen 	apples	.     
    NNP   	VBZ   	DT    	NN    	NNS   	.     

    Eric  	takes 	away  	half  	of    	the   	apples	.     
    NNP   	VBZ   	RB    	DT    	IN    	DT    	NNS   	.     

    How   	many  	apples	does  	Mickey	have  	now   	?     
    WRB   	JJ    	NNS   	VBZ   	NNP   	VB    	RB    	.     

## Problem inference
I think this problem is about Mickey and Eric exchanging apples and asks a single question.

## Parsed problem
    Mickey               	has                  	12                   	apples               	.                    
    context              	operator             	constant             	unit                 	punctuation          

    Eric                 	takes                	away                 	0.5                  	of                   	the                  	apples owned by Mickey	.                    
    context              	operator             	noise                	variable_relationship	conjunction          	noise                	context_unit         	punctuation          

    How many             	apples               	does                 	Mickey               	have                 	now                  	?                    
    asking               	unit                 	q_start              	context              	q_stop               	subordinate          	punctuation          


## Question 1

### Question text
How many apples does Mickey have now?

### Answer interpretation
The answer is the unknown value of apples owned by Mickey at the end of the problem.

## Data extraction

### Sentence 1
apples owned by Mickey = 12

### Sentence 2
apples owned by Mickey - Eric apples
apples owned by Eric = Mickey apples * 0.5

## Correct response
6 apples

***

[('there', 'exestential', None), ('are', 'pre_ind_plu', None), ('6', 'constant', None), ('pink christmas ornaments', 'unit', (u'plural', u'neutral')), ('and', 'coordinating_conjunction', None), ('8', 'constant', None), ('blue christmas ornaments', 'unit', (u'plural', u'neutral')), ('on', 'conjunction', None), ('the', u'noise', None), (('christmas tree', 'NN'), 'subordinate', (u'singular', u'neutral')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('christmas ornaments', 'context', None), ('are', 'pre_ind_plu', None), ('on', 'conjunction', None), ('the', u'noise', None), (('christmas tree', 'NN'), 'subordinate', (u'singular', u'neutral')), (('altogether', 'RB'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
There are 6 pink christmas ornaments and 8 blue christmas ornaments on the christmas tree.
How many christmas ornaments are on the christmas tree altogether?

## Digested problem
    There     	are       	6         	pink      	christmas 	ornaments 	and       	8         	blue      	christmas 	ornaments 	on        	the       	christmas 	tree      	.         
    EX        	VBP       	CD        	NN        	NNS       	NNS       	CC        	CD        	JJ        	NNS       	NNS       	IN        	DT        	NNS       	VBP       	.         

    How       	many      	christmas 	ornaments 	are       	on        	the       	christmas 	tree      	altogether	?         
    WRB       	JJ        	NNS       	NNS       	VBP       	IN        	DT        	NNS       	VBP       	RB        	.         

## Problem inference
I think this problem is about christmas ornaments pink christmas ornaments, blue christmas ornaments, pink ornaments, christmas ornaments, and blue ornaments on the christmas tree and asks a single question.

## Parsed problem
    There                   	are                     	6                       	pink christmas ornaments	and                     	8                       	blue christmas ornaments	on                      	the                     	christmas tree          	.                       
    exestential             	pre_ind_plu             	constant                	unit                    	coordinating_conjunction	constant                	unit                    	conjunction             	noise                   	subordinate             	punctuation             

    How many                	christmas ornaments     	are                     	on                      	the                     	christmas tree          	altogether              	?                       
    asking                  	context                 	pre_ind_plu             	conjunction             	noise                   	subordinate             	subordinate             	punctuation             


## Question 1

### Question text
How many christmas ornaments are on the christmas tree altogether?

### Answer interpretation
The answer is the unknown value of christmas ornaments on the christmas tree added together.

## Data extraction

### Sentence 1
christmas ornaments on the christmas tree = 8
christmas ornaments on the christmas tree + 6
blue ornaments on the christmas tree = 8
blue christmas ornaments on the christmas tree = 8
pink ornaments on the christmas tree = 6
pink christmas ornaments on the christmas tree = 6

## Correct response
14 christmas ornaments

***

[('Sara', 'context', (u'singular', u'feminine')), ('has', 'operator', None), ('8', 'constant', None), ('pieces of chocolate', 'unit', None), ('.', 'punctuation', None)]
[("Sara's mother", 'context', (u'singular', u'feminine')), ('gives', 'operator', None), (('Sara', (u'singular', u'feminine')), 'comparator_context', (u'singular', u'feminine')), ('4', 'constant', None), ('more', u'rel_more', None), ('pieces of chocolate', 'unit', (u'singular', u'neutral')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('pieces of chocolate', 'unit', None), ('does', 'q_start', None), ('Sara', 'context', (u'singular', u'feminine')), ('have', 'q_stop', None), (('now', 'RB'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Sara has 8 pieces of chocolate.
Her mother gives her 4 more pieces.
How many pieces of chocolate does Sara have now?

## Digested problem
    Sara     	has      	8        	pieces   	of       	chocolate	.        
    NNP      	VBZ      	CD       	NNS      	IN       	JJ       	.        

    Her      	mother   	gives    	her      	4        	more     	pieces   	.        
    PRP$     	NN       	VBZ      	PRP$     	CD       	JJR      	NNS      	.        

    How      	many     	pieces   	of       	chocolate	does     	Sara     	have     	now      	?        
    WRB      	JJ       	NNS      	IN       	JJ       	VBZ      	NNP      	VB       	RB       	.        

## Problem inference
I think this problem is about Sara and Sara's mother pieces of chocolate and pieces and asks a single question.

## Parsed problem
    Sara               	has                	8                  	pieces of chocolate	.                  
    context            	operator           	constant           	unit               	punctuation        

    Sara's mother      	gives              	Sara               	4                  	more               	pieces of chocolate	.                  
    context            	operator           	comparator_context 	constant           	rel_more           	unit               	punctuation        

    How many           	pieces of chocolate	does               	Sara               	have               	now                	?                  
    asking             	unit               	q_start            	context            	q_stop             	subordinate        	punctuation        


## Question 1

### Question text
How many pieces of chocolate does Sara have now?

### Answer interpretation
The answer is the unknown value of pieces of chocolate owned by Sara at the end of the problem.

## Data extraction

### Sentence 1
pieces of chocolate owned by Sara = 8

### Sentence 2
pieces of chocolate owned by Sara's mother - 4
pieces of chocolate owned by Sara + 4

## Correct response
12 pieces of chocolate

***

[('Alex', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('7', 'constant', None), ('doughnuts', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Bennett', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('4', 'constant', None), ('doughnuts', 'unit', (u'plural', u'neutral')), ('more', u'rel_more', None), ('than', 'conjunction', None), (('Alex', (u'singular', u'masculine')), 'comparator_context', (u'singular', u'masculine')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('doughnuts', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Bennett', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Alex has 7 doughnuts.
Bennett has 4 doughnuts more than him.
How many doughnuts does Bennett have?

## Digested problem
    Alex     	has      	7        	doughnuts	.        
    NNP      	VBZ      	CD       	NNS      	.        

    Bennett  	has      	4        	doughnuts	more     	than     	him      	.        
    NNP      	VBZ      	CD       	NNS      	JJR      	IN       	PRP      	.        

    How      	many     	doughnuts	does     	Bennett  	have     	?        
    WRB      	JJ       	NNS      	VBZ      	NNP      	VB       	.        

## Problem inference
I think this problem is about Alex and Bennett grouping doughnuts and asks a single question.

## Parsed problem
    Alex              	has               	7                 	doughnuts         	.                 
    context           	operator          	constant          	unit              	punctuation       

    Bennett           	has               	4                 	doughnuts         	more              	than              	Alex              	.                 
    context           	operator          	constant          	unit              	rel_more          	conjunction       	comparator_context	punctuation       

    How many          	doughnuts         	does              	Bennett           	have              	?                 
    asking            	unit              	q_start           	context           	q_stop            	punctuation       


## Question 1

### Question text
How many doughnuts does Bennett have?

### Answer interpretation
The answer is the unknown value of doughnuts owned by Bennett.

## Data extraction

### Sentence 1
doughnuts owned by Alex = 7

### Sentence 2
doughnuts owned by Bennett = 7
doughnuts owned by Bennett + 4

## Correct response
11 doughnuts

***

[('Charlie', 'context', (u'singular', u'masculine')), ('gave', 'operator', None), ('4', 'constant', None), ('bottles', 'unit', (u'plural', u'neutral')), ('to', 'conjunction', None), ('Mac', 'context', (u'singular', u'masculine')), ('.', 'punctuation', None)]
[('Charlie', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('8', 'constant', None), ('bottles', 'unit', (u'plural', u'neutral')), (('left', 'SUB'), 'subordinate', None), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('bottles', 'unit', (u'plural', u'neutral')), ('did', 'q_start', None), ('Charlie', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), ('in', 'conjunction', None), ('the', u'noise', None), (('beginning', 'SUB'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Charlie gave 4 bottles to Mac.
He has 8 bottles left.
How many bottles did Charlie have in the beginning?

## Digested problem
    Charlie  	gave     	4        	bottles  	to       	Mac      	.        
    NNP      	VBD      	CD       	NNS      	TO       	NNP      	.        

    He       	has      	8        	bottles  	left     	.        
    PRP      	VBZ      	CD       	NNS      	VBN      	.        

    How      	many     	bottles  	did      	Charlie  	have     	in       	the      	beginning	?        
    WRB      	JJ       	NNS      	VBD      	NNP      	VB       	IN       	DT       	NN       	.        

## Problem inference
I think this problem is about Charlie and Mac bottles and asks a single question.

## Parsed problem
    Charlie    	gave       	4          	bottles    	to         	Mac        	.          
    context    	operator   	constant   	unit       	conjunction	context    	punctuation

    Charlie    	has        	8          	bottles    	left       	.          
    context    	operator   	constant   	unit       	subordinate	punctuation

    How many   	bottles    	did        	Charlie    	have       	in         	the        	beginning  	?          
    asking     	unit       	q_start    	context    	q_stop     	conjunction	noise      	subordinate	punctuation


## Question 1

### Question text
How many bottles did Charlie have in the beginning?

### Answer interpretation
The answer is the unknown value of bottles owned by Charlie at the beginning of the problem.

## Data extraction

### Sentence 1
bottles owned by Charlie - 4
bottles owned by Mac + 4

### Sentence 2
bottles owned by Charlie == 8

## Correct response
12 bottles

***

[('Meathead', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('6', 'constant', None), ('newspapers', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Archie', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('7', 'constant', None), ('newspapers', 'unit', (u'plural', u'neutral')), ('more', u'rel_more', None), ('than', 'conjunction', None), (('Meathead', (u'singular', u'masculine')), 'comparator_context', (u'singular', u'masculine')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('newspapers', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Archie', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Meathead has 6 newspapers.
Archie has 7 newspapers more than him.
How many newspapers does Archie have?

## Digested problem
    Meathead  	has       	6         	newspapers	.         
    NNP       	VBZ       	CD        	NNS       	.         

    Archie    	has       	7         	newspapers	more      	than      	him       	.         
    NNP       	VBZ       	CD        	NNS       	JJR       	IN        	PRP       	.         

    How       	many      	newspapers	does      	Archie    	have      	?         
    WRB       	JJ        	NNS       	VBZ       	NNP       	VB        	.         

## Problem inference
I think this problem is about Meathead and Archie grouping newspapers and asks a single question.

## Parsed problem
    Meathead          	has               	6                 	newspapers        	.                 
    context           	operator          	constant          	unit              	punctuation       

    Archie            	has               	7                 	newspapers        	more              	than              	Meathead          	.                 
    context           	operator          	constant          	unit              	rel_more          	conjunction       	comparator_context	punctuation       

    How many          	newspapers        	does              	Archie            	have              	?                 
    asking            	unit              	q_start           	context           	q_stop            	punctuation       


## Question 1

### Question text
How many newspapers does Archie have?

### Answer interpretation
The answer is the unknown value of newspapers owned by Archie.

## Data extraction

### Sentence 1
newspapers owned by Meathead = 6

### Sentence 2
newspapers owned by Archie = 6
newspapers owned by Archie + 7

## Correct response
13 newspapers

***

[('Hellen', 'context', (u'singular', u'feminine')), ('has', 'operator', None), ('2', 'constant', None), ('dolls', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Troy', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('3', 'constant', None), ('more', u'rel_more', None), ('dolls', 'unit', (u'plural', u'neutral')), ('than', 'conjunction', None), (('Hellen', (u'singular', u'feminine')), 'comparator_context', (u'singular', u'feminine')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('dolls', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Troy', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), ('?', 'punctuation', None)]
[('how many', 'asking', None), ('dolls', 'unit', (u'plural', u'neutral')), ('do', 'q_start', None), ('Troy and Hellen', 'context', (u'plural', u'mixed')), ('have', 'q_stop', None), (('altogether', 'RB'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Hellen has 2 dolls.
Troy has 3 more dolls than her.
How many dolls does Troy have?
How many dolls do they have altogether?

## Digested problem
    Hellen    	has       	2         	dolls     	.         
    NNP       	VBZ       	CD        	NNS       	.         

    Troy      	has       	3         	more      	dolls     	than      	her       	.         
    NNP       	VBZ       	CD        	JJR       	NNS       	IN        	PRP$      	.         

    How       	many      	dolls     	does      	Troy      	have      	?         
    WRB       	JJ        	NNS       	VBZ       	NNP       	VB        	.         

    How       	many      	dolls     	do        	they      	have      	altogether	?         
    WRB       	JJ        	NNS       	VBP       	PRP       	VBP       	RB        	.         

## Problem inference
I think this problem is about Hellen and Troy grouping dolls and asks multiple questions.

## Parsed problem
    Hellen            	has               	2                 	dolls             	.                 
    context           	operator          	constant          	unit              	punctuation       

    Troy              	has               	3                 	more              	dolls             	than              	Hellen            	.                 
    context           	operator          	constant          	rel_more          	unit              	conjunction       	comparator_context	punctuation       

    How many          	dolls             	does              	Troy              	have              	?                 
    asking            	unit              	q_start           	context           	q_stop            	punctuation       

    How many          	dolls             	do                	Troy and Hellen   	have              	altogether        	?                 
    asking            	unit              	q_start           	context           	q_stop            	subordinate       	punctuation       


## Question 1

### Question text
How many dolls does Troy have?

### Answer interpretation
The answer is the unknown value of dolls owned by Troy.

## Question 2

### Question text
How many dolls do they have altogether?

### Answer interpretation
The answer is the unknown value of dolls owned by Troy and Hellen added together.

## Data extraction

### Sentence 1
dolls owned by Hellen = 2

### Sentence 2
dolls owned by Troy = 2
dolls owned by Troy + 3

## Correct response

### Response 1
5 dolls

### Response 2
7 dolls

***

[('Dad', 'context', (u'singular', u'masculine')), ('gives', 'operator', None), ('Richard', 'context', (u'singular', u'masculine')), ('7', 'constant', None), ('feathers', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Dad', 'context', (u'singular', u'masculine')), ('gives', 'operator', None), ('William', 'context', (u'singular', u'masculine')), ('4', 'constant', None), ('feathers', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('feathers', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Dad', 'context', (u'singular', u'masculine')), ('give', 'q_stop', None), ('to', 'conjunction', None), ('the', u'noise', None), ('two', 'constant', None), (('boys', 'NNS'), 'subordinate', None), ('?', 'punctuation', None)]
[('how many', 'asking', None), ('more', u'rel_more', None), ('feathers', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Richard', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), ('than', 'conjunction', None), (('William', (u'singular', u'masculine')), 'comparator_context', (u'singular', u'masculine')), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Dad gives Richard 7 feathers.
Dad gives William 4 feathers.
How many feathers does Dad give to the two boys?
How many more feathers does Richard have than William?

## Digested problem
    Dad     	gives   	Richard 	7       	feathers	.       
    NNP     	VBZ     	NNP     	CD      	NNS     	.       

    Dad     	gives   	William 	4       	feathers	.       
    NNP     	VBZ     	NNP     	CD      	NNS     	.       

    How     	many    	feathers	does    	Dad     	give    	to      	the     	two     	boys    	?       
    WRB     	JJ      	NNS     	VBZ     	NNP     	VB      	TO      	DT      	CD      	NNS     	.       

    How     	many    	more    	feathers	does    	Richard 	have    	than    	William 	?       
    WRB     	JJ      	RBR     	NNS     	VBZ     	NNP     	VB      	IN      	NNP     	.       

## Problem inference
I think this problem is about Dad, Richard, and William feathers and asks multiple questions.

## Parsed problem
    Dad               	gives             	Richard           	7                 	feathers          	.                 
    context           	operator          	context           	constant          	unit              	punctuation       

    Dad               	gives             	William           	4                 	feathers          	.                 
    context           	operator          	context           	constant          	unit              	punctuation       

    How many          	feathers          	does              	Dad               	give              	to                	the               	two               	boys              	?                 
    asking            	unit              	q_start           	context           	q_stop            	conjunction       	noise             	constant          	subordinate       	punctuation       

    How many          	more              	feathers          	does              	Richard           	have              	than              	William           	?                 
    asking            	rel_more          	unit              	q_start           	context           	q_stop            	conjunction       	comparator_context	punctuation       


## Question 1

### Question text
How many feathers does Dad give to the two boys?

### Answer interpretation
The answer is the unknown value of feathers given to William and Richard added together.

## Question 2

### Question text
How many more feathers does Richard have than William?

### Answer interpretation
The answer is the increase in value of feathers owned by Richard with respect to William.

## Data extraction

### Sentence 1
feathers owned by Dad - 7
feathers owned by Richard + 7

### Sentence 2
feathers owned by William + 4
feathers owned by Dad - 4

## Correct response

### Response 1
11 feathers

### Response 2
3 feathers

***

[('Tom', 'context', (u'singular', u'masculine')), ('is', 'operator', None), ('6', 'constant', None), ('years', 'unit', (u'plural', u'neutral')), ('old', 'adjective', None), ('.', 'punctuation', None)]
[('Lee', 'context', (u'singular', u'masculine')), ('is', 'operator', None), ('3', 'constant', None), ('years', 'unit', (u'plural', u'neutral')), ('younger', u'rel_less', None), ('than', 'conjunction', None), (('Tom', (u'singular', u'masculine')), 'comparator_context', (u'singular', u'masculine')), ('.', 'punctuation', None)]
[('how old', 'asking', None), ('is', 'q_start', None), ('Lee', 'context', (u'singular', u'masculine')), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Tom is 6 years old. 
Lee is 3 years younger than Tom. 
How old is Lee?

## Digested problem
    Tom    	is     	6      	years  	old    	.      
    NNP    	VBZ    	CD     	NNS    	JJ     	.      

    Lee    	is     	3      	years  	younger	than   	Tom    	.      
    NNP    	VBZ    	CD     	NNS    	JJR    	IN     	NNP    	.      

    How    	old    	is     	Lee    	?      
    WRB    	JJ     	VBZ    	NNP    	.      

## Problem inference
I think this problem is about Tom and Lee grouping years and asks a single question.

## Parsed problem
    Tom               	is                	6                 	years             	old               	.                 
    context           	operator          	constant          	unit              	adjective         	punctuation       

    Lee               	is                	3                 	years             	younger           	than              	Tom               	.                 
    context           	operator          	constant          	unit              	rel_less          	conjunction       	comparator_context	punctuation       

    How old           	is                	Lee               	?                 
    asking            	q_start           	context           	punctuation       


## Question 1

### Question text
How old is Lee?

### Answer interpretation
The answer is the unknown value of years owned by Lee.

## Data extraction

### Sentence 1
years owned by Tom = 6

### Sentence 2
years owned by Lee = 6
years owned by Lee - 3

## Correct response
3 years

***

[('Sam', 'context', (u'singular', u'ambiguous')), ('has', 'operator', None), ('12', 'constant', None), ('bags', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Sam', 'context', (u'singular', u'masculine')), ('buys', 'operator', None), ('8', 'constant', None), ('more', u'rel_more', None), ('bags', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('bags', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Sam', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), ('in', 'conjunction', None), ('all', u'dynamic_variable', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Sam has 12 bags. 
He buys 8 more bags. 
How many bags does he have in all?

## Digested problem
    Sam 	has 	12  	bags	.   
    NNP 	VBZ 	CD  	NNS 	.   

    He  	buys	8   	more	bags	.   
    PRP 	VBZ 	CD  	JJR 	NNS 	.   

    How 	many	bags	does	he  	have	in  	all 	?   
    WRB 	JJ  	NNS 	VBZ 	PRP 	VB  	IN  	DT  	.   

## Problem inference
I think this problem is about Sam getting bags and asks a single question.

## Parsed problem
    Sam             	has             	12              	bags            	.               
    context         	operator        	constant        	unit            	punctuation     

    Sam             	buys            	8               	more            	bags            	.               
    context         	operator        	constant        	rel_more        	unit            	punctuation     

    How many        	bags            	does            	Sam             	have            	in              	all             	?               
    asking          	unit            	q_start         	context         	q_stop          	conjunction     	dynamic_variable	punctuation     


## Question 1

### Question text
How many bags does he have in all?

### Answer interpretation
The answer is the unknown value of bags owned by Sam.

## Data extraction

### Sentence 1
bags owned by Sam = 12

### Sentence 2
bags owned by Sam + 8

## Correct response
20 bags

***

[('Paul', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('10', 'constant', None), ('books', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Paul', 'context', (u'singular', u'masculine')), ('gives', 'operator', None), ("Paul's sister", 'context', (u'singular', u'feminine')), ('7', 'constant', None), ('books', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('books', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Paul', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), (('left', 'SUB'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Paul has 10 books. 
Paul gives his sister 7 books. 
How many books does Paul have left?

## Digested problem
    Paul  	has   	10    	books 	.     
    NNP   	VBZ   	CD    	NNS   	.     

    Paul  	gives 	his   	sister	7     	books 	.     
    NNP   	VBZ   	PRP$  	NN    	CD    	NNS   	.     

    How   	many  	books 	does  	Paul  	have  	left  	?     
    WRB   	JJ    	NNS   	VBZ   	NNP   	VB    	VBN   	.     

## Problem inference
I think this problem is about Paul and Paul's sister books and asks a single question.

## Parsed problem
    Paul           	has            	10             	books          	.              
    context        	operator       	constant       	unit           	punctuation    

    Paul           	gives          	Paul's sister  	7              	books          	.              
    context        	operator       	context        	constant       	unit           	punctuation    

    How many       	books          	does           	Paul           	have           	left           	?              
    asking         	unit           	q_start        	context        	q_stop         	subordinate    	punctuation    


## Question 1

### Question text
How many books does Paul have left?

### Answer interpretation
The answer is the unknown value of books owned by Paul at the end of the problem.

## Data extraction

### Sentence 1
books owned by Paul = 10

### Sentence 2
books owned by Paul - 7
books owned by Paul's sister + 7

## Correct response
3 books

***

[('Paul', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('6', 'constant', None), ('cups', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Paul', 'context', (u'singular', u'masculine')), ('buys', 'operator', None), ('11', 'constant', None), ('more', u'rel_more', None), ('cups', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('cups', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Paul', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), ('in', 'conjunction', None), ('all', u'dynamic_variable', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Paul has 6 cups. 
He buys 11 more cups. 
How many cups does he have in all?

## Digested problem
    Paul	has 	6   	cups	.   
    NNP 	VBZ 	CD  	NNS 	.   

    He  	buys	11  	more	cups	.   
    PRP 	VBZ 	CD  	JJR 	NNS 	.   

    How 	many	cups	does	he  	have	in  	all 	?   
    WRB 	JJ  	NNS 	VBZ 	PRP 	VB  	IN  	DT  	.   

## Problem inference
I think this problem is about Paul getting cups and asks a single question.

## Parsed problem
    Paul            	has             	6               	cups            	.               
    context         	operator        	constant        	unit            	punctuation     

    Paul            	buys            	11              	more            	cups            	.               
    context         	operator        	constant        	rel_more        	unit            	punctuation     

    How many        	cups            	does            	Paul            	have            	in              	all             	?               
    asking          	unit            	q_start         	context         	q_stop          	conjunction     	dynamic_variable	punctuation     


## Question 1

### Question text
How many cups does he have in all?

### Answer interpretation
The answer is the unknown value of cups owned by Paul.

## Data extraction

### Sentence 1
cups owned by Paul = 6

### Sentence 2
cups owned by Paul + 11

## Correct response
17 cups

***

[('Sidd', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('10', 'constant', None), ('books', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Sidd', 'context', (u'singular', u'masculine')), ('buys', 'operator', None), ('11', 'constant', None), ('more', u'rel_more', None), ('books', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('books', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Sidd', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), ('in', 'conjunction', None), ('all', u'dynamic_variable', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Sidd has 10 books. 
He buys 11 more books. 
How many books does he have in all?


## Digested problem
    Sidd 	has  	10   	books	.    
    NNP  	VBZ  	CD   	NNS  	.    

    He   	buys 	11   	more 	books	.    
    PRP  	VBZ  	CD   	JJR  	NNS  	.    

    How  	many 	books	does 	he   	have 	in   	all  	?    
    WRB  	JJ   	NNS  	VBZ  	PRP  	VB   	IN   	DT   	.    

## Problem inference
I think this problem is about Sidd getting books and asks a single question.

## Parsed problem
    Sidd            	has             	10              	books           	.               
    context         	operator        	constant        	unit            	punctuation     

    Sidd            	buys            	11              	more            	books           	.               
    context         	operator        	constant        	rel_more        	unit            	punctuation     

    How many        	books           	does            	Sidd            	have            	in              	all             	?               
    asking          	unit            	q_start         	context         	q_stop          	conjunction     	dynamic_variable	punctuation     


## Question 1

### Question text
How many books does he have in all?

### Answer interpretation
The answer is the unknown value of books owned by Sidd.

## Data extraction

### Sentence 1
books owned by Sidd = 10

### Sentence 2
books owned by Sidd + 11

## Correct response
21 books

***

[('Lee', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('10', 'constant', None), ('blocks', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Lee', 'context', (u'singular', u'masculine')), ('buys', 'operator', None), ('2', 'constant', None), ('more', u'rel_more', None), ('blocks', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('blocks', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Lee', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), ('in', 'conjunction', None), ('all', u'dynamic_variable', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Lee has 10 blocks. 
He buys 2 more blocks. 
How many blocks does he have in all?

## Digested problem
    Lee   	has   	10    	blocks	.     
    NNP   	VBZ   	CD    	NNS   	.     

    He    	buys  	2     	more  	blocks	.     
    PRP   	VBZ   	CD    	JJR   	NNS   	.     

    How   	many  	blocks	does  	he    	have  	in    	all   	?     
    WRB   	JJ    	NNS   	VBZ   	PRP   	VB    	IN    	DT    	.     

## Problem inference
I think this problem is about Lee getting blocks and asks a single question.

## Parsed problem
    Lee             	has             	10              	blocks          	.               
    context         	operator        	constant        	unit            	punctuation     

    Lee             	buys            	2               	more            	blocks          	.               
    context         	operator        	constant        	rel_more        	unit            	punctuation     

    How many        	blocks          	does            	Lee             	have            	in              	all             	?               
    asking          	unit            	q_start         	context         	q_stop          	conjunction     	dynamic_variable	punctuation     


## Question 1

### Question text
How many blocks does he have in all?

### Answer interpretation
The answer is the unknown value of blocks owned by Lee.

## Data extraction

### Sentence 1
blocks owned by Lee = 10

### Sentence 2
blocks owned by Lee + 2

## Correct response
12 blocks

***

[('Tom', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('5', 'constant', None), ('bags', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Tom', 'context', (u'singular', u'masculine')), ('gives', 'operator', None), ("Tom's sister", 'context', (u'singular', u'feminine')), ('4', 'constant', None), ('bags', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('bags', 'unit', (u'plural', u'neutral')), ('does', 'q_start', None), ('Tom', 'context', (u'singular', u'masculine')), ('have', 'q_stop', None), (('left', 'SUB'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Tom has 5 bags. 
Tom gives his sister 4 bags. 
How many bags does Tom have left?

## Digested problem
    Tom   	has   	5     	bags  	.     
    NNP   	VBZ   	CD    	NNS   	.     

    Tom   	gives 	his   	sister	4     	bags  	.     
    NNP   	VBZ   	PRP$  	NN    	CD    	NNS   	.     

    How   	many  	bags  	does  	Tom   	have  	left  	?     
    WRB   	JJ    	NNS   	VBZ   	NNP   	VB    	VBN   	.     

## Problem inference
I think this problem is about Tom and Tom's sister bags and asks a single question.

## Parsed problem
    Tom            	has            	5              	bags           	.              
    context        	operator       	constant       	unit           	punctuation    

    Tom            	gives          	Tom's sister   	4              	bags           	.              
    context        	operator       	context        	constant       	unit           	punctuation    

    How many       	bags           	does           	Tom            	have           	left           	?              
    asking         	unit           	q_start        	context        	q_stop         	subordinate    	punctuation    


## Question 1

### Question text
How many bags does Tom have left?

### Answer interpretation
The answer is the unknown value of bags owned by Tom at the end of the problem.

## Data extraction

### Sentence 1
bags owned by Tom = 5

### Sentence 2
bags owned by Tom's sister + 4
bags owned by Tom - 4

## Correct response
1 bags

***

[('Tom', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('5', 'constant', None), ('books', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('Sidd', 'context', (u'singular', u'masculine')), ('has', 'operator', None), ('8', 'constant', None), ('books', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('books', 'unit', (u'plural', u'neutral')), ('do', 'q_start', None), ('Sidd and Tom', 'context', (u'plural', u'mixed')), ('have', 'q_stop', None), (('altogether', 'RB'), 'subordinate', None), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
Tom has 5 books. 
Sidd has 8 books. 
How many books do they have altogether?

## Digested problem
    Tom       	has       	5         	books     	.         
    NNP       	VBZ       	CD        	NNS       	.         

    Sidd      	has       	8         	books     	.         
    NNP       	VBZ       	CD        	NNS       	.         

    How       	many      	books     	do        	they      	have      	altogether	?         
    WRB       	JJ        	NNS       	VBP       	PRP       	VBP       	RB        	.         

## Problem inference
I think this problem is about Tom and Sidd grouping books and asks a single question.

## Parsed problem
    Tom         	has         	5           	books       	.           
    context     	operator    	constant    	unit        	punctuation 

    Sidd        	has         	8           	books       	.           
    context     	operator    	constant    	unit        	punctuation 

    How many    	books       	do          	Sidd and Tom	have        	altogether  	?           
    asking      	unit        	q_start     	context     	q_stop      	subordinate 	punctuation 


## Question 1

### Question text
How many books do they have altogether?

### Answer interpretation
The answer is the unknown value of books owned by Sidd and Tom added together.

## Data extraction

### Sentence 1
books owned by Tom = 5

### Sentence 2
books owned by Sidd = 8

## Correct response
13 books

***

[('me', 'context', (u'self', u'self')), ('have', 'operator', None), ('7', 'constant', None), ('balloons', 'unit', (u'plural', u'neutral')), ('and', 'coordinating_conjunction', None), ('my friend', 'context', (u'singular', u'ambiguous')), ('has', 'operator', None), ('5', 'constant', None), ('balloons', 'unit', (u'plural', u'neutral')), ('.', 'punctuation', None)]
[('how many', 'asking', None), ('more', u'rel_more', None), ('balloons', 'unit', (u'plural', u'neutral')), ('do', 'q_start', None), ('me', 'context', (u'self', u'self')), ('have', 'q_stop', None), ('than', 'conjunction', None), (('my friend', (u'singular', u'ambiguous')), 'comparator_context', (u'singular', u'ambiguous')), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
You have 7 balloons and your friend has 5 balloons. 
How many more balloons do you have than your friend? 

## Digested problem
    You     	have    	7       	balloons	and     	your    	friend  	has     	5       	balloons	.       
    PRP     	VBP     	CD      	NNS     	CC      	PRP$    	NN      	VBZ     	CD      	NNS     	.       

    How     	many    	more    	balloons	do      	you     	have    	than    	your    	friend  	?       
    WRB     	JJ      	RBR     	NNS     	VBP     	PRP     	VB      	IN      	PRP$    	NN      	.       

## Problem inference
I think this problem is about me and my friend grouping balloons and asks a single question.

## Parsed problem
    I                       	have                    	7                       	balloons                	and                     	my friend               	has                     	5                       	balloons                	.                       
    context                 	operator                	constant                	unit                    	coordinating_conjunction	context                 	operator                	constant                	unit                    	punctuation             

    How many                	more                    	balloons                	do                      	I                       	have                    	than                    	my friend               	?                       
    asking                  	rel_more                	unit                    	q_start                 	context                 	q_stop                  	conjunction             	comparator_context      	punctuation             


## Question 1

### Question text
How many more balloons do you have than your friend?

### Answer interpretation
The answer is the increase in value of balloons owned by me with respect to my friend.

## Data extraction

### Sentence 1
balloons owned by me = 7
balloons owned by my friend = 5

## Correct response
2 balloons

***

[('2', 'constant', None), ('birds', 'context', None), ('were', 'pre_ind_plu', None), ('sitting', u'acting', None), ('on', 'conjunction', None), ('the', u'noise', None), (('fence', 'NN'), 'subordinate', (u'singular', u'neutral')), ('.', 'punctuation', None)]
[('4', 'constant', None), ('more', u'rel_more', None), ('birds', 'context', (u'plural', u'mixed')), ('came', 'operator', None), ('to', 'conjunction', None), ('join', 'operator', None), ('birds', 'context', (u'plural', u'mixed')), ('.', 'punctuation', None), (('fence', u'place_noun'), 'subordinate_inferred', (u'singular', u'neutral'))]
[('how many', 'asking', None), ('birds', 'context', (u'plural', u'mixed')), ('are', 'pre_ind_plu', None), ('sitting', u'acting', None), ('on', 'conjunction', None), ('the', u'noise', None), (('fence', 'NN'), 'subordinate', (u'singular', u'neutral')), ('?', 'punctuation', None)]
# Zoidberg Solution

## The problem
2 birds were sitting on the fence. 
4 more birds came to join them. 
How many birds are sitting on the fence?

## Digested problem
    2      	birds  	were   	sitting	on     	the    	fence  	.      
    LS     	NNS    	VBD    	VBG    	IN     	DT     	NN     	.      

    4      	more   	birds  	came   	to     	join   	them   	.      
    LS     	JJR    	NNS    	VBD    	TO     	VB     	PRP    	.      

    How    	many   	birds  	are    	sitting	on     	the    	fence  	?      
    WRB    	JJ     	NNS    	VBP    	VBG    	IN     	DT     	NN     	.      

## Problem inference
I think this problem is about an increasing number of sitting birds on the fence and asks a single question.

## Parsed problem
    2                   	birds               	were                	sitting             	on                  	the                 	fence               	.                   
    constant            	context             	pre_ind_plu         	acting              	conjunction         	noise               	subordinate         	punctuation         

    4                   	more                	birds               	came                	to                  	join                	birds               	.                   	fence               
    constant            	rel_more            	context             	operator            	conjunction         	operator            	context             	punctuation         	subordinate_inferred

    How many            	birds               	are                 	sitting             	on                  	the                 	fence               	?                   
    asking              	context             	pre_ind_plu         	acting              	conjunction         	noise               	subordinate         	punctuation         


## Question 1

### Question text
How many birds are sitting on the fence?

### Answer interpretation
The answer is the unknown value of birds sitting on the fence.

## Data extraction

### Sentence 1
sitting birds on the fence = 2

### Sentence 2
sitting birds on the fence + 4

## Correct response
6 birds
