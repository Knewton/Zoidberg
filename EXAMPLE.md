
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

    Jane       	buys       	6          	balloons   	.          
    context    	operator   	constant   	unit       	punctuation

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
    14 toy cars

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
    context    	operator   	constant   	unit       	operator   	punctuation

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
    I think this problem is about an increasing number of fish swimming in a pond and asks a single question.

## Parsed problem
    8                   	fish                	are                 	swimming            	in                  	1                   	pond                	.                   
    constant            	context             	pre_ind_plu         	acting              	conjunction         	constant            	subordinate         	punctuation         

    4                   	more                	fish                	join                	fish                	.                   	pond                	swimming            
    constant            	rel_more            	context             	operator            	context             	punctuation         	subordinate_inferred	acting_inferred     

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
    rocks owned by Pigpen's friends - 8
    rocks owned by Pigpen's friends == 0

## Correct response
    3 rocks

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
    context              	operator             	operator             	variable_relationship	conjunction          	noise                	context_unit         	punctuation          

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
    I think this problem is about pink christmas ornaments, blue christmas ornaments, pink ornaments, christmas ornaments, and blue ornaments on the christmas tree and asks a single question.

## Parsed problem
    There                   	are                     	6                       	pink christmas ornaments	and                     	8                       	blue christmas ornaments	on                      	the                     	christmas tree          	.                       
    exestential             	pre_ind_plu             	constant                	unit                    	coordinating_conjunction	constant                	unit                    	conjunction             	noise                   	subordinate             	punctuation             

    How many                	christmas ornaments     	are                     	on                      	the                     	christmas tree          	altogether              	?                       
    asking                  	unit                    	pre_ind_plu             	conjunction             	noise                   	subordinate             	subordinate             	punctuation             


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

***

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

    How many          	feathers          	does              	Dad               	give              	to                	the               	2                 	boys              	?                 
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

    How old           	is                	Lee               	?                 	years             
    asking            	q_start           	context           	punctuation       	unit_inferred     


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
    I think this problem is about an increasing number of birds sitting on the fence and asks a single question.

## Parsed problem
    2                   	birds               	were                	sitting             	on                  	the                 	fence               	.                   
    constant            	context             	pre_ind_plu         	acting              	conjunction         	noise               	subordinate         	punctuation         

    4                   	more                	birds               	came                	to                  	join                	birds               	.                   	fence               	sitting             
    constant            	rel_more            	context             	operator            	conjunction         	operator            	context             	punctuation         	subordinate_inferred	acting_inferred     

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

***

# Zoidberg Solution

## The problem
    You have 7 cookies and you ate 2 of them. 
    How many cookies do you have left? 
    
    
## Digested problem
    You    	have   	7      	cookies	and    	you    	ate    	2      	of     	them   	.      
    PRP    	VBP    	CD     	NNS    	CC     	PRP    	VBP    	CD     	IN     	PRP    	.      

    How    	many   	cookies	do     	you    	have   	left   	?      
    WRB    	JJ     	NNS    	VBP    	PRP    	VB     	VBN    	.      

## Problem inference
    I think this problem is about me losing cookies and asks a single question.

## Parsed problem
    I                       	have                    	7                       	cookies                 	and                     	I                       	ate                     	2                       	cookies                 	.                       
    context                 	operator                	constant                	unit                    	coordinating_conjunction	context                 	operator                	constant                	unit                    	punctuation             

    How many                	cookies                 	do                      	I                       	have                    	left                    	?                       
    asking                  	unit                    	q_start                 	context                 	q_stop                  	subordinate             	punctuation             


## Question 1

### Question text
    How many cookies do you have left?

### Answer interpretation
    The answer is the unknown value of cookies owned by me at the end of the problem.

## Data extraction

### Sentence 1
    cookies owned by me = 7
    cookies owned by me - 2

## Correct response
    5 cookies

***

# Zoidberg Solution

## The problem
    You have collected 7 crickets. 
    How many more crickets do you need to collect to have 11 crickets? 
    
## Digested problem
    You      	have     	collected	7        	crickets 	.        
    PRP      	VBP      	VBN      	CD       	NNS      	.        

    How      	many     	more     	crickets 	do       	you      	need     	to       	collect  	to       	have     	11       	crickets 	?        
    WRB      	JJ       	RBR      	NNS      	VBP      	PRP      	VBP      	TO       	VB       	TO       	VB       	CD       	NNS      	.        

## Problem inference
    I think this problem is about me getting crickets to collect to to have crickets and asks a single question.

## Parsed problem
    I          	have       	collected  	7          	crickets   	.          
    context    	operator   	operator   	constant   	unit       	punctuation

    How many   	more       	crickets   	do         	I          	need       	to         	collect    	to         	have       	11         	crickets   	?          
    asking     	rel_more   	unit       	q_start    	context    	q_stop     	conjunction	q_start    	conjunction	q_stop     	constant   	subordinate	punctuation


## Question 1

### Question text
    How many more crickets do you need to collect to have 11 crickets?

### Answer interpretation
    The answer is the increase in value of crickets owned by me needed to equal the specified value.

## Data extraction

### Sentence 1
    crickets owned by me = 7

### Sentence 2
    crickets owned by me == 11

## Correct response
    4 crickets

***

# Zoidberg Solution

## The problem
    A bee has 6 legs. 
    How many legs do 5 bees have?
    
## Digested problem
    A   	bee 	has 	6   	legs	.   
    DT  	NN  	VBZ 	CD  	NNS 	.   

    How 	many	legs	do  	5   	bees	have	?   
    WRB 	JJ  	NNS 	VBP 	CD  	NNS 	VBP 	.   

## Problem inference
    I think this problem is about bees having legs and asks a single question.

## Parsed problem
    1          	bee        	has        	6          	legs       	.          
    constant   	context    	operator   	constant   	unit       	punctuation

    How many   	legs       	do         	5          	bees       	have       	?          
    asking     	unit       	q_start    	constant   	context    	q_stop     	punctuation


## Question 1

### Question text
    How many legs do 5 bees have?

### Answer interpretation
    The answer is the unknown value of legs owned by 5 bees.

## Data extraction

### Sentence 1
    legs owned by 1 bee = 6

## Correct response
    30 legs

***

# Zoidberg Solution

## The problem
    4 birds are sitting on a branch. 
    1 flies away. 
    How many birds are left on the branch? 
    
## Digested problem
    4      	birds  	are    	sitting	on     	a      	branch 	.      
    LS     	NNS    	VBP    	VBG    	IN     	DT     	NN     	.      

    1      	flies  	away   	.      
    LS     	NNS    	RB     	.      

    How    	many   	birds  	are    	left   	on     	the    	branch 	?      
    WRB    	JJ     	NNS    	VBP    	VBN    	IN     	DT     	NN     	.      

## Problem inference
    I think this problem is about a decreasing number of birds sitting and flies on a branch and asks a single question.

## Parsed problem
    4                   	birds               	are                 	sitting             	on                  	1                   	branch              	.                   
    constant            	context             	pre_ind_plu         	acting              	conjunction         	constant            	subordinate         	punctuation         

    1                   	flies               	away                	.                   	birds               	branch              
    constant            	acting              	operator            	punctuation         	context_inferred    	subordinate_inferred

    How many            	birds               	are                 	left                	on                  	the                 	branch              	?                   	sitting             
    asking              	context             	pre_ind_plu         	subordinate         	conjunction         	noise               	subordinate         	punctuation         	acting_inferred     


## Question 1

### Question text
    How many birds are left on the branch?

### Answer interpretation
    The answer is the unknown value of birds sitting at the end of the problem on a branch.

## Data extraction

### Sentence 1
    sitting birds on a branch = 4

### Sentence 2
    sitting birds on a branch - 1

## Correct response
    3 birds

***

# Zoidberg Solution

## The problem
    There are 6 birds and 3 nests. 
    How many more birds are there than nests? 
    
## Digested problem
    There	are  	6    	birds	and  	3    	nests	.    
    EX   	VBP  	CD   	NNS  	CC   	CD   	NNS  	.    

    How  	many 	more 	birds	are  	there	than 	nests	?    
    WRB  	JJ   	RBR  	NNS  	VBP  	RB   	IN   	NNS  	.    

## Problem inference
    I think this problem is about birds and nests than nests and asks a single question.

## Parsed problem
    There                   	are                     	6                       	birds                   	and                     	3                       	nests                   	.                       
    exestential             	pre_ind_plu             	constant                	unit                    	coordinating_conjunction	constant                	unit                    	punctuation             

    How many                	more                    	birds                   	are                     	there                   	than                    	nests                   	?                       
    asking                  	rel_more                	unit                    	pre_ind_plu             	exestential             	conjunction             	subordinate             	punctuation             


## Question 1

### Question text
    How many more birds are there than nests?

### Answer interpretation
    The answer is the increase in value of birds with respect to nests.

## Data extraction

### Sentence 1
    nests = 3
    birds = 6

## Correct response
    3 birds

***

# Zoidberg Solution

## The problem
    3 raccoons are playing in the woods. 
    2 go home to eat dinner. How many raccoons are left in the woods? 
    
## Digested problem
    3       	raccoons	are     	playing 	in      	the     	woods   	.       
    LS      	NNS     	VBP     	VBG     	IN      	DT      	NNS     	.       

    2       	go      	home    	to      	eat     	dinner  	.       
    LS      	VBP     	RB      	TO      	VB      	NN      	.       

    How     	many    	raccoons	are     	left    	in      	the     	woods   	?       
    WRB     	JJ      	NNS     	VBP     	VBN     	IN      	DT      	NNS     	.       

## Problem inference
    I think this problem is about a decreasing number of raccoons playing in the woods and home and asks a single question.

## Parsed problem
    3                   	raccoons            	are                 	playing             	in                  	the                 	woods               	.                   
    constant            	context             	pre_ind_plu         	acting              	conjunction         	noise               	subordinate         	punctuation         

    2                   	go                  	home                	to                  	eat                 	dinner              	.                   	raccoons            	woods               	playing             
    constant            	operator            	subordinate         	conjunction         	operator            	subordinate         	punctuation         	context_inferred    	subordinate_inferred	acting_inferred     

    How many            	raccoons            	are                 	left                	in                  	the                 	woods               	?                   	playing             
    asking              	context             	pre_ind_plu         	subordinate         	conjunction         	noise               	subordinate         	punctuation         	acting_inferred     


## Question 1

### Question text
    How many raccoons are left in the woods?

### Answer interpretation
    The answer is the unknown value of raccoons playing at the end of the problem in the woods.

## Data extraction

### Sentence 1
    playing raccoons in the woods = 3

### Sentence 2
    playing raccoons in the woods - 2

## Correct response
    1 raccoons

***

# Zoidberg Solution

## The problem
    There are 5 flowers and 3 bees. 
    How many less bees than flowers?
    
## Digested problem
    There  	are    	5      	flowers	and    	3      	bees   	.      
    EX     	VBP    	CD     	NNS    	CC     	CD     	NNS    	.      

    How    	many   	less   	bees   	than   	flowers	?      
    WRB    	JJ     	JJR    	NNS    	IN     	NNS    	.      

## Problem inference
    I think this problem is about flowers and bees than flowers and asks a single question.

## Parsed problem
    There                   	are                     	5                       	flowers                 	and                     	3                       	bees                    	.                       
    exestential             	pre_ind_plu             	constant                	unit                    	coordinating_conjunction	constant                	unit                    	punctuation             

    How many                	less                    	bees                    	than                    	flowers                 	?                       
    asking                  	rel_less                	unit                    	conjunction             	subordinate             	punctuation             


## Question 1

### Question text
    How many less bees than flowers?

### Answer interpretation
    The answer is the difference in value of bees with respect to flowers.

## Data extraction

### Sentence 1
    flowers = 5
    bees = 3

## Correct response
    2 bees

***

# Zoidberg Solution

## The problem
    1 lonely pigeons was eating breadcrumbs. 
    Another pigeon came to eat breadcrumbs, too. 
    How many pigeons are eating breadcrumbs now? 
    
## Digested problem
    1          	lonely     	pigeons    	was        	eating     	breadcrumbs	.          
    LS         	RB         	NNS        	VBD        	VBG        	NNS        	.          

    Another    	pigeon     	came       	to         	eat        	breadcrumbs	,          	too        	.          
    DT         	NN         	VBD        	TO         	VB         	NNS        	,          	RB         	.          

    How        	many       	pigeons    	are        	eating     	breadcrumbs	now        	?          
    WRB        	JJ         	NNS        	VBP        	VBG        	NNS        	RB         	.          

## Problem inference
    I think this problem is about pigeons getting and losing eating breadcrumbs and pigeon lonely and asks a single question.

## Parsed problem
    1                   	lonely              	pigeons             	was                 	eating              	breadcrumbs         	.                   
    constant            	subordinate         	context             	pre_ind_plu         	acting              	unit                	punctuation         

    1                   	pigeon              	came                	to                  	eat                 	breadcrumbs         	,                   	too                 	.                   	pigeons             	lonely              	eating              
    constant            	unit                	operator            	conjunction         	operator            	subordinate         	punctuation         	noise               	punctuation         	context_inferred    	subordinate_inferred	acting_inferred     

    How many            	pigeons             	are                 	eating              	breadcrumbs         	now                 	?                   	lonely              
    asking              	context             	pre_ind_plu         	acting              	unit                	subordinate         	punctuation         	subordinate_inferred


## Question 1

### Question text
    How many pigeons are eating breadcrumbs now?

### Answer interpretation
    The answer is the unknown value of pigeons eating lonely at the end of the problem.

## Data extraction

### Sentence 1
    eating pigeons lonely = 1

### Sentence 2
    eating pigeons lonely + 1

## Correct response
    2 pigeons

***

# Zoidberg Solution

## The problem
    3 owls were sitting on the fence. 
    2 more owls joined them. 
    How many owls are on the fence now? 
    
    
## Digested problem
    3      	owls   	were   	sitting	on     	the    	fence  	.      
    LS     	NNS    	VBD    	VBG    	IN     	DT     	NN     	.      

    2      	more   	owls   	joined 	them   	.      
    LS     	JJR    	NNS    	VBD    	PRP    	.      

    How    	many   	owls   	are    	on     	the    	fence  	now    	?      
    WRB    	JJ     	NNS    	VBP    	IN     	DT     	NN     	RB     	.      

## Problem inference
    I think this problem is about an increasing number of owls sitting on the fence and asks a single question.

## Parsed problem
    3                   	owls                	were                	sitting             	on                  	the                 	fence               	.                   
    constant            	context             	pre_ind_plu         	acting              	conjunction         	noise               	subordinate         	punctuation         

    2                   	more                	owls                	joined              	owls                	.                   	fence               	sitting             
    constant            	rel_more            	context             	operator            	context             	punctuation         	subordinate_inferred	acting_inferred     

    How many            	owls                	are                 	on                  	the                 	fence               	now                 	?                   	sitting             
    asking              	context             	pre_ind_plu         	conjunction         	noise               	subordinate         	subordinate         	punctuation         	acting_inferred     


## Question 1

### Question text
    How many owls are on the fence now?

### Answer interpretation
    The answer is the unknown value of owls sitting on the fence at the end of the problem.

## Data extraction

### Sentence 1
    sitting owls on the fence = 3

### Sentence 2
    sitting owls on the fence + 2

## Correct response
    5 owls

***

# Zoidberg Solution

## The problem
    2 beavers were working on their home. 
    1 went for a swim. 
    How many beavers are still working on their home? 
    
    
## Digested problem
    2      	beavers	were   	working	on     	their  	home   	.      
    LS     	NNS    	VBD    	VBG    	IN     	PRP$   	NN     	.      

    1      	went   	for    	a      	swim   	.      
    LS     	VBD    	IN     	DT     	NN     	.      

    How    	many   	beavers	are    	still  	working	on     	their  	home   	?      
    WRB    	JJ     	NNS    	VBP    	RB     	VBG    	IN     	PRP$   	NN     	.      

## Problem inference
    I think this problem is about a decreasing number of beavers, their home, and beavers' home working on their home and asks a single question.

## Parsed problem
    2                   	beavers             	were                	working             	on                  	home                	.                   
    constant            	context             	pre_ind_plu         	acting              	conjunction         	subordinate         	punctuation         

    1                   	went                	for                 	1                   	swim                	.                   	beavers             	home                	working             
    constant            	operator            	conjunction         	constant            	noise               	punctuation         	context_inferred    	subordinate_inferred	acting_inferred     

    How many            	beavers             	are                 	still               	working             	on                  	home                	?                   
    asking              	context             	pre_ind_plu         	subordinate         	acting              	conjunction         	subordinate         	punctuation         


## Question 1

### Question text
    How many beavers are still working on their home?

### Answer interpretation
    The answer is the unknown value of beavers working at the end of the problem on their home.

## Data extraction

### Sentence 1
    working beavers on their home = 2

### Sentence 2
    working beavers on their home - 1

## Correct response
    1 beavers

***

# Zoidberg Solution

## The problem
    2 toucans are sitting on a tree limb. 
    1 more toucan joins them. 
    How many toucans in all? 
    
## Digested problem
    2      	toucans	are    	sitting	on     	a      	tree   	limb   	.      
    LS     	NNS    	VBP    	VBG    	IN     	DT     	NN     	NN     	.      

    1      	more   	toucan 	joins  	them   	.      
    LS     	JJR    	JJ     	NNS    	PRP    	.      

    How    	many   	toucans	in     	all    	?      
    WRB    	JJ     	NNS    	IN     	DT     	.      

## Problem inference
    I think this problem is about an increasing number of toucans sitting on a tree limb and asks a single question.

## Parsed problem
    2                   	toucans             	are                 	sitting             	on                  	1                   	tree limb           	.                   
    constant            	context             	pre_ind_plu         	acting              	conjunction         	constant            	subordinate         	punctuation         

    1                   	more                	toucan              	joins               	.                   	toucans             	tree limb           	sitting             
    constant            	rel_more            	adjective           	operator            	punctuation         	context_inferred    	subordinate_inferred	acting_inferred     

    How many            	toucans             	in                  	all                 	?                   	tree limb           	sitting             
    asking              	context             	conjunction         	dynamic_variable    	punctuation         	subordinate_inferred	acting_inferred     


## Question 1

### Question text
    How many toucans in all?

### Answer interpretation
    The answer is the unknown value of toucans sitting on a tree limb.

## Data extraction

### Sentence 1
    sitting toucans on a tree limb = 2

### Sentence 2
    sitting toucans on a tree limb + 1

## Correct response
    3 toucans

***

# Zoidberg Solution

## The problem
    There are 4 squirrels in a tree with 2 nuts. 
    How many more squirrels are there than nuts?
    
## Digested problem
    There    	are      	4        	squirrels	in       	a        	tree     	with     	2        	nuts     	.        
    EX       	VBP      	CD       	NNS      	IN       	DT       	NN       	IN       	CD       	NNS      	.        

    How      	many     	more     	squirrels	are      	there    	than     	nuts     	?        
    WRB      	JJ       	RBR      	NNS      	VBP      	RB       	IN       	NNS      	.        

## Problem inference
    I think this problem is about squirrels and nuts in a tree and than nuts and asks a single question.

## Parsed problem
    There               	are                 	4                   	squirrels           	in                  	1                   	tree                	with                	2                   	nuts                	.                   
    exestential         	pre_ind_plu         	constant            	unit                	conjunction         	constant            	subordinate         	conjunction         	constant            	unit                	punctuation         

    How many            	more                	squirrels           	are                 	there               	than                	nuts                	?                   	tree                
    asking              	rel_more            	unit                	pre_ind_plu         	exestential         	conjunction         	subordinate         	punctuation         	subordinate_inferred


## Question 1

### Question text
    How many more squirrels are there than nuts?

### Answer interpretation
    The answer is the increase in value of squirrels with respect to nuts in a tree.

## Data extraction

### Sentence 1
    nuts in a tree = 2
    squirrels in a tree = 4

## Correct response
    2 squirrels

***

# Zoidberg Solution

## The problem
    Mrs. Hilt has two pennies, two dimes, and two nickels. 
    Jacob has four pennies, one nickel, and one dime. 
    Who has more money? 
    How much more? 
    Who has more pennies?
    How many more?
    
## Digested problem
    Mrs.   	Hilt   	has    	two    	pennies	,      	two    	dimes  	,      	and    	two    	nickels	.      
    NNP    	NNP    	VBZ    	CD     	NNS    	,      	CD     	NNS    	,      	CC     	CD     	NNS    	.      

    Jacob  	has    	four   	pennies	,      	one    	nickel 	,      	and    	one    	dime   	.      
    NNP    	VBZ    	CD     	NNS    	,      	CD     	NN     	,      	CC     	CD     	NN     	.      

    Who    	has    	more   	money  	?      
    WP     	VBZ    	JJR    	NN     	.      

    How    	much   	more   	?      
    WRB    	JJ     	RBR    	.      

    Who    	has    	more   	pennies	?      
    WP     	VBZ    	JJR    	NNS    	.      

    How    	many   	more   	?      
    WRB    	JJ     	RBR    	.      

## Problem inference
    I think this problem is about Mrs. Hilt and Jacob grouping pennies, dimes, nickels, and money and asks multiple questions.

## Parsed problem
    Mrs. Hilt               	has                     	2                       	pennies                 	,                       	2                       	dimes                   	,                       	and                     	2                       	nickels                 	.                       
    context                 	operator                	constant                	unit                    	punctuation             	constant                	unit                    	punctuation             	coordinating_conjunction	constant                	unit                    	punctuation             

    Jacob                   	has                     	4                       	pennies                 	,                       	1                       	nickel                  	,                       	and                     	1                       	dime                    	.                       
    context                 	operator                	constant                	unit                    	punctuation             	constant                	unit                    	punctuation             	coordinating_conjunction	constant                	unit                    	punctuation             

    Who                     	has                     	more                    	money                   	?                       
    asking                  	q_start                 	rel_more                	unit                    	punctuation             

    How much                	more                    	?                       	money                   
    asking                  	rel_more                	punctuation             	unit_inferred           

    Who                     	has                     	more                    	pennies                 	?                       
    asking                  	q_start                 	rel_more                	unit                    	punctuation             

    How many                	more                    	?                       	pennies                 
    asking                  	rel_more                	punctuation             	unit_inferred           


## Question 1

### Question text
    Who has more money?

### Answer interpretation
    The answer is the unknown owner of more money.

## Question 2

### Question text
    How much more?

### Answer interpretation
    The answer is the increase in value of money owned by Mrs. Hilt with respect to Jacob.

## Question 3

### Question text
    Who has more pennies?

### Answer interpretation
    The answer is the unknown owner of more pennies.

## Question 4

### Question text
    How many more?

### Answer interpretation
    The answer is the increase in value of pennies owned by Jacob with respect to Mrs. Hilt.

## Data extraction

### Sentence 1
    money owned by Mrs. Hilt = 0.02
    money owned by Mrs. Hilt + 0.1
    money owned by Mrs. Hilt + 0.2
    nickels owned by Mrs. Hilt = 2
    dimes owned by Mrs. Hilt = 2
    pennies owned by Mrs. Hilt = 2

### Sentence 2
    money owned by Jacob = 0.04
    money owned by Jacob + 0.05
    money owned by Jacob + 0.1
    dime owned by Jacob = 1
    nickel owned by Jacob = 1
    pennies owned by Jacob = 4

## Correct response

### Response 1
    Mrs. Hilt

### Response 2
    13 cents

### Response 3
    Jacob

### Response 4
    2 pennies
