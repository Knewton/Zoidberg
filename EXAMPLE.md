
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
14 toy cars fewer

***

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
The answer is the unknown value of fish swimming in a pond at the end of the problem.

## Data extraction

### Sentence 1
swimming fish in a pond = 8

### Sentence 2
swimming fish + 4

## Correct response
8 fish

***

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
rocks owned by Pigpen - 8
rocks owned by Pigpen == 0
rocks owned by Pigpen's friends + 8

## Correct response
11 rocks

***

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
    Mr. Lupis  	needs      	4          	eggs       	to         	bake       	13         	muffins    	.          
    context    	operator   	constant   	unit       	conjunction	operator   	constant   	subordinate	punctuation

    Mr. Lupis  	has        	only       	2          	eggs       	.          
    context    	operator   	noise      	constant   	unit       	punctuation

    How many   	more       	eggs       	does       	Mr. Lupis  	need       	to         	bake       	the        	muffins    	?          
    asking     	rel_more   	unit       	q_start    	context    	q_stop     	conjunction	operator   	noise      	subordinate	punctuation


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
2 eggs more

***

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
