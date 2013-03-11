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

## Answer formulation

### How many balloons does she have now?
The answer is the unknown value of balloons owned by Jane at the end of the problem.
# Zoidberg Solution

## The problem
Mrs. Jones bought some bananas. Her friends ate 5 bananas. She gave the remaining 4 bananas to her friends. How many bananas did she buy in the beginning?

## Digested problem
    Mrs.     	Jones    	bought   	some     	bananas  	.        
    NNP      	NNP      	VBD      	DT       	NNS      	.        

    Her      	friends  	ate      	5        	bananas  	.        
    PRP$     	NNS      	VBP      	CD       	NNS      	.        

    She      	gave     	the      	remaining	4        	bananas  	to       	her      	friends  	.        
    PRP      	VBD      	DT       	VBG      	CD       	NNS      	TO       	PRP$     	NNS      	.        

    How      	many     	bananas  	did      	she      	buy      	in       	the      	beginning	?        
    WRB      	JJ       	NNS      	VBD      	PRP      	VB       	IN       	DT       	NN       	.        

## Problem inference
I think this problem is about Mrs. Jones and her friends exchanging bananas and asks a single question.

## Parsed problem
    Mrs. Jones 	bought     	some       	bananas    	.          
    context    	operator   	noise      	unit       	punctuation

    her friends	ate        	5          	bananas    	.          
    context    	operator   	constant   	unit       	punctuation

    Mrs. Jones 	gave       	the        	remaining  	4          	bananas    	to         	her friends	.          
    context    	operator   	noise      	unknown    	constant   	unit       	unknown    	context    	punctuation

    How many   	bananas    	did        	Mrs. Jones 	buy        	in         	the        	beginning  	?          
    asking     	unit       	q_start    	context    	q_stop     	conjunction	noise      	subordinate	punctuation

## Answer formulation

### How many bananas did she buy in the beginning?
The answer is the unknown value of bananas owned by Mrs. Jones at the beginning of the problem.
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
    Tony       	has        	19         	jars       	.          
    context    	operator   	constant   	unit       	punctuation

    Tony       	gives      	16         	jars       	to         	his sister 	.          
    context    	operator   	constant   	unit       	unknown    	context    	punctuation

    How many   	jars       	does       	Tony       	have       	now        	?          
    asking     	unit       	q_start    	context    	q_stop     	subordinate	punctuation

## Answer formulation

### How many jars does he have now?
The answer is the unknown value of jars owned by Tony at the end of the problem.
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
    Lucy       	has        	8          	dolls      	.          
    context    	operator   	constant   	unit       	punctuation

    Ethelle    	has        	4          	more       	dolls      	than       	her        	.          
    context    	operator   	constant   	unknown    	unit       	conjunction	unknown    	punctuation

    How many   	dolls      	does       	Ethelle    	have       	?          
    asking     	unit       	q_start    	context    	q_stop     	punctuation

## Answer formulation

### How many dolls does Ethelle have?
The answer is the unknown value of dolls owned by Ethelle.
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
    Joey       	has        	13         	toy cars   	.          
    context    	operator   	constant   	unit       	punctuation

    Chandler   	has        	6          	toy cars   	.          
    context    	operator   	constant   	unit       	punctuation

    How many   	fewer      	toy cars   	does       	Chandler   	have       	than       	Joey       	?          
    asking     	unknown    	unit       	q_start    	context    	q_stop     	conjunction	context    	punctuation

## Answer formulation

### How many fewer toy cars does Chandler have than Joey?
The answer is the unknown value of toy cars owned by Joey.
