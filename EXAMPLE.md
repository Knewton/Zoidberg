
how many asking
balloons unit
does q_start
Jane context
have q_stop
('now', None) subordinate
? punctuation
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
how many asking
bananas unit
did q_start
Mrs. Jones context
buy q_stop
in conjunction
the noise
('beginning', 'in') subordinate
? punctuation
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
I think this problem is about Mrs. Jones, her family, and her friends exchanging bananas and asks a single question.

## Parsed problem
    Mrs. Jones     	bought         	some           	bananas        	.              
    context        	operator       	variable       	unit           	punctuation    

    her family     	ate            	5              	bananas        	.              
    context        	operator       	constant       	unit           	punctuation    

    Mrs. Jones     	gave           	the            	remaining      	4              	bananas        	to             	her friends    	.              
    context        	operator       	noise          	solution_zero  	constant       	unit           	noise          	context        	punctuation    

    How many       	bananas        	did            	Mrs. Jones     	buy            	in             	the            	beginning      	?              
    asking         	unit           	q_start        	context        	q_stop         	conjunction    	noise          	subordinate    	punctuation    


## Question 1

### Question text
How many bananas did she buy in the beginning?

### Answer interpretation
The answer is the unknown value of bananas owned by Mrs. Jones at the beginning of the problem.

## Data extraction

### Sentence 1
bananas owned by Mrs. Jones = 0
bananas owned by Mrs. Jones + x

### Sentence 2
bananas owned by Mrs. Jones - 5

### Sentence 3
bananas owned by Mrs. Jones - 4
bananas owned by Mrs. Jones == 0

## Correct response
9 bananas
how many asking
jars unit
does q_start
Tony context
have q_stop
('now', None) subordinate
? punctuation
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
I think this problem is about Tony and his sister exchanging jars and asks a single question.

## Parsed problem
    Tony           	has            	19             	jars           	.              
    context        	operator       	constant       	unit           	punctuation    

    Tony           	gives          	16             	jars           	to             	his sister     	.              
    context        	operator       	constant       	unit           	noise          	context        	punctuation    

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

## Correct response
3 jars
how many asking
dolls unit
does q_start
Ethelle context
have q_stop
? punctuation
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
I think this problem is about Lucy and Ethelle having dolls and asks a single question.

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
how many asking
fewer rel_less
toy cars unit
does q_start
Chandler context
have q_stop
than conjunction
('Joey', (u'singular', u'masculine')) comparator_context
? punctuation
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
I think this problem is about Joey and Chandler having toy cars and asks a single question.

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

### Sentence 2
toy cars owned by Chandler = 6

## Correct response
7 fewer toy cars
how many asking
apples unit
does q_start
Marc context
have q_stop
('now', None) subordinate
? punctuation
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
    context    	operator   	constant   	unit       	noise      	context    	punctuation

    Marc       	gives      	3          	apples     	to         	Julia      	.          
    context    	operator   	constant   	unit       	noise      	context    	punctuation

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
apples owned by Marc - 2

### Sentence 4
apples owned by Marc - 3

## Correct response
3 apples
how many asking
fish context
are pre_ind_plu
swimming acting
in conjunction
the noise
('pond', 'in') subordinate
('now', None) subordinate
? punctuation
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
    8          	fish       	are        	swimming   	in         	a          	pond       	.          
    constant   	context    	pre_ind_plu	acting     	conjunction	constant   	subordinate	punctuation

    4          	more       	fish       	join       	fish       	.          
    constant   	rel_more   	context    	operator   	context    	punctuation

    How many   	fish       	are        	swimming   	in         	the        	pond       	now        	?          
    asking     	context    	pre_ind_plu	acting     	conjunction	noise      	subordinate	subordinate	punctuation


## Question 1

### Question text
How many fish are swimming in the pond now?

### Answer interpretation
The answer is the unknown value of fish swimming fish in a pond at the end of the problem.

## Data extraction

### Sentence 1
swimming fish in a pond = 8

### Sentence 2
swimming fish in a pond + 4

## Correct response
12 fish
