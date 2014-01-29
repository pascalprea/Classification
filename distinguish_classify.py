#! /usr/bin/env python
# -*- coding: utf-8 -*-


"""

This program is an implementation of the algorithm presented in :

    P. Préa & M. Rolbert : Distinguishing and Classifying from n-ary Properties, submited to Journal of Classification.
    
You can freely use/adapt/etc this program. Just please cite the above paper.




Data are in DICTIONNAIRE "Data". Its structure is : (cf. "Construction_data ()")
    each entity is a key of the dictionary
    The elements of the dictionary "Data" are also dictionaries :
        - the keys are properties
        - the elements are lists which contain tuple which match 
	
        "Data ['John'] = {"likes" : [('Audrey',), ('Grace',)], "eats" : [('food', 'instr1')]}" means that John :
            likes Ann
            likes Mary
            eats food with instr1
            
            notice that ('Ophelia',),  ('food', 'instr1') are tuples and not lists

3 examples of Data sets are given, in the functions Construction_Data (), Construction_data_Bis () and Construction_Data_Ter ()
Treating these 3 data sets takes less than one second.
    
 
 
The hierarchy is built step by step, top bottom, in the list "Tree"
"Depth" indicates the current step
"Tour" takes alternatively value 1 and 0
"Tree[Tour]" is the set of classes at step "Depth", "Tree[1-Tour]" the set of classes at step "Depth-1"
A class is represented by one of its element
"Code" gives, for every entity, its class, "Code [Tour]" at step "Depth", and "Code[1-Tour]" at step "Depth-1"

"""

#   GLOBAL VARIABLES :  #
                        #
Data = None             #
Tree = None             #
Code = None             #
Tour = None             #
Depth = None            #
                        #
#########################


  
#####################################################
#                                                   #
#                   DATA CONSTRUCTION               #
#                                                   #
#####################################################
                        
def Construction_Data () :
    """Constructs a data set corresponding to :
        instr1  is a fork ; instr2 is a spoon ; food is chicken
        John likes Audrey and Grace ; Paul likes Marilyn and Liz
        Hamlet loves Ophelia
    """
    global Data
    Data = {}
    Data ['John'] = {"likes" : [('Audrey',), ('Grace',)], "eats" : [('food', 'instr1')]}
    Data ['Paul'] = {"likes" : [('Marilyn',), ('Liz',)], "eats" : [('food', 'instr2')]}
    Data ['Audrey'] = {"is_liked_by" : [('John',)]}
    Data ['Marilyn'] = {"is_liked_by" : [('Paul',)]}
    Data ['Grace'] = {"is_liked_by" : [('John',)]}
    Data ['Liz'] = {"is_liked_by" : [('Paul',)]}
    Data ['Ophelia'] = {"is_loved_by" : [('Hamlet',)]}
    Data ['Hamlet'] = {"loves" : [('Ophelia',)]}
    Data ['food'] = {"chicken" : []}
    Data ['instr1'] = {"fork" : []}
    Data ['instr2'] = {"spoon" : []}
    
def Construction_Data_Bis () :
    """ Constructs Data corresponding to Figure 1 of 
    "Distinguishing and Classifying from n-ary properties"
    """
    global Data
    Data ={}
    Data ['b1'] = {"ball" : [], "is_In" : [('c1',)]}
    Data ['b2'] = {"ball" : [], "is_In" : [('c2',)]}
    Data ['b3'] = {"ball" : [], "is_In" : [('c3',)]}
    Data ['b4'] = {"ball" : [], "is_In" : [('c5',)]}
    Data ['b5'] = {"ball" : [], "is_On" : [('floor',)]}
    Data ['c1'] = {"cup" : [], "contains" : [('b1',)], "is_On" : [('t1',)]}
    Data ['c2'] = {"cup" : [], "contains" : [('b2',)], "is_On" : [('t1',)]}
    Data ['c3'] = {"cup" : [], "contains" : [('b3',)], "is_On" : [('t2',)]}
    Data ['c4'] = {"cup" : [], "contains" : [('f',)], "is_On" : [('t2',)]}
    Data ['c5'] = {"cup" : [], "contains" : [('b4',)], "is_On" : [('floor',)]}
    Data ['c6'] = {"cup" : [],  "is_On" : [('floor',)]}
    Data ['f'] = {"flower" : [], "is_In" : [('c4',)]}
    Data ['t1'] = {"table" : [], "is_On" : [('floor',)], "has_on" : [('c1',), ('c2',)]}
    Data ['t2'] = {"table" : [], "is_On" : [('floor',)], "has_on" : [('c3',), ('c4',)]}
    Data ['floor'] = {}

def Construction_Data_Ter () :
    """ Constructs Data corresponding to Figure 3 of 
    "Distinguishing and Classifying from n-ary properties"
    """
    global Data
    Data ={}
    Data ['b1'] = {"ball" : [], "is_In" : [('c1',)]}
    Data ['b2'] = {"ball" : [], "is_In" : [('c2',)]}
    Data ['b3'] = {"ball" : [], "is_In" : [('c3',)]}
    Data ['b4'] = {"ball" : [], "is_In" : [('c6',)]}
    Data ['b5'] = {"ball" : [], "is_In" : [('c7',)]}
    Data ['f1'] = {"flower" : [], "is_In" : [('c4',)]}
    Data ['f2'] = {"flower" : [], "is_In" : [('c5',)]}
    Data ['f3'] = {"flower" : [], "is_In" : [('c8',)]}
    Data ['f4'] = {"flower" : [], "is_In" : [('c9',)]}
    Data ['f5'] = {"flower" : [], "is_In" : [('c10',)]}
    Data ['t1'] = {"table" : [], "has_on" : [('c1',), ('c2',), ('c3',), ('c4',), ('c5',)]}
    Data ['t2'] = {"table" : [], "has_on" : [('c6',), ('c7',), ('c8',), ('c9',), ('c10',)]}
    Data ['c1'] = {"cup" : [], "contains" : [('b1',)], "is_On" : [('t1',)]}
    Data ['c2'] = {"cup" : [], "contains" : [('b2',)], "is_On" : [('t1',)]}
    Data ['c3'] = {"cup" : [], "contains" : [('b3',)], "is_On" : [('t1',)]}
    Data ['c4'] = {"cup" : [], "contains" : [('f1',)], "is_On" : [('t1',)]}
    Data ['c5'] = {"cup" : [], "contains" : [('f2',)], "is_On" : [('t1',)]}
    Data ['c6'] = {"cup" : [], "contains" : [('b4',)], "is_On" : [('t2',)]}
    Data ['c7'] = {"cup" : [], "contains" : [('b5',)], "is_On" : [('t2',)]}
    Data ['c8'] = {"cup" : [], "contains" : [('f3',)], "is_On" : [('t2',)]}
    Data ['c9'] = {"cup" : [], "contains" : [('f4',)], "is_On" : [('t2',)]}
    Data ['c10'] = {"cup" : [], "contains" : [('f5',)], "is_On" : [('t2',)]}


#####################################################
#                                                   #
#               END DATA CONSTRUCTION               #
#                                                   #
#####################################################



def printing () :
    """ At each level of the resulting hierarchy, print the classes
    """
    global Tree
    global Code
    global Tour
    global Depth
    print ("\n"  + str(len(Tree[Tour]))+ ' Classes at Depth '+ str(Depth)+':\n')
    for classe in range(len(Tree[Tour])) :
            string = 'CLASS ' + str(classe) + ' :='
            for ii in Data :
                if Code[Tour][ii] == classe :
                    string = string + ' ' + str( ii)
            print(string)


def Initial_Construction ():
    """ BUILDS, IN "Tree[Tour]", THE CLASSES FOR 0-DISTINGUISHABILITY
    """
    global Tree
    global Code
    global Tour
    global Depth
    Tree = [[],[]]
    Code = [{},{}]
    Tour = 0
    Depth = 0
    for ii in Data :
        non_treated = True
        for num in range(len(Tree[Tour])) :
            if Data[ii].keys() == Data[Tree[Tour][num][0]].keys() :
                to_do = True
                for prop in Data[ii].keys() :
                    if len(Data[ii][prop]) != len(Data[Tree[Tour][num][0]][prop]) :
                        to_do = False
                if to_do :
                    Tree[Tour][num].append(ii)
                    Code[Tour][ii] = num
                    non_treated = False
        if non_treated :
            Code[Tour][ii] = len(Tree[Tour])
            Tree[Tour].append([ii])
    printing ()


def Do_Edge (ii,jj) :
	""" FOR THE CONSTRUCTION OF THE GRAPH (CF 'Matching'), SAYS IF AN EDGE IS 
	NEEDED BETWEEN VERTICES 'ii' AND 'jj'.
	"""
	tt = 1 - Tour
	for i in range(len(ii)) :
		if Code[tt][ii[i]] != Code[tt][jj[i]] :
			return False
	return True
	
    
def alternat_path (ii, Dat_I, Dat_J, matching_J) :
	""" BUILDS AN ALTERNANTING PATH SATRING FROM VERTEX 'ii' IN A BIPARTITE GRAPH
    WITH VERTICES 'Dat_I' + 'Dat_J' AND ALREADY WITH A MATCHING 'matching_J'
 	"""
	Dist_I = dict.fromkeys(Dat_I, [-1, None])
	Dist_J = dict.fromkeys(Dat_J, -1)
	Dist_I[ii] = [0, None]
	d = 0
	nb = 1
	while nb > 0 :
		nb = 0
		for i in Dist_I :
			if Dist_I[i][0] == d :
				for j in Dat_I[i] :
					if Dist_J[j] == -1 :
						nb = 1
						Dist_J[j] = [d+1, i]
						if matching_J[j] == None :
							path = [j, Dist_J[j][1]]
							while path[-1] != ii :
								x = Dist_I[path[-1]][1]
								path.extend[x, Dist_J[x][1]]
							path.reverse()
							return path
						else :
							Dist_I[matching_J[j]] = [d+2, j]
		d = d + 2
	return []

	
def Exists_Matching (Dat_I, Dat_J, Edges) :
	"""CHECK IF THERE EXISTS A PERFECT MATCHING IN THE BIPARTITE GRAPH WITH
	VERTICES = 'Dat_I' + 'Dat_J' & EDGES = 'Edges'.
	USES  alternat_path
	"""
	matching_I = dict.fromkeys(Dat_I)
	matching_J = dict.fromkeys(Dat_J)
	for i in Dat_I :
		if matching_I[i] == None : 
			path = alternat_path (i, Dat_I, Dat_J, matching_J)
			if path == [] :
				return False
			else :
				for k in range(len(path)/2) :
					matching_I [path[k]] = path[k+1]
					matching_J [path[k+1]] = path[k]
	return True
	
    
def Matching (ii, jj, prop) :
	""" TESTS IF, FOR ENTITIES 'ii' & 'jj', THERE EXISTS A PERFECT MATCHING BETWEEN
	THE TUPLES WHICH "MATCHENT" 'ii' & THOSE WHICH  MATCHENT" 'jj' FOR PROPERTY 'prop'
	"""
	Dat_ii = dict.fromkeys(Data[ii][prop])
	for i in Dat_ii :
		Dat_ii[i] = []
	Dat_jj = dict.fromkeys(Data[jj][prop]) 
	for j in Dat_jj :
		Dat_jj[j] = []
	Edges = {}
	for i in Dat_ii :
		for j in Dat_jj :
			if Do_Edge(i,j) :
				Dat_ii[i].append (j)
				Dat_jj[j].append (i)
				Edges[(i,j)] = 0
	return Exists_Matching (Dat_ii, Dat_jj, Edges)


def Confusable (ii, jj) :
	"""TESTS IF ENTITIES 'ii' & 'jj' ARE CONFUSABLE
	"""
	for prop in Data[ii] :
		if len(Data[ii][prop]) > 0 :
			if len(Data[ii][prop]) != len(Data[jj][prop]) :
				return False
			elif not Matching (ii, jj, prop) :
				return False
	return True


def Up_Date () :
    """BUILDS, IN  'Tree[Tour]', THE CLASSES FOR K-DISTINGUISHABILIY, FOR K>0
    'Depth' IS THE VALUE K (IN DISTINGUISHABILIY).
    FOR EACH ENTITY 'ii', WE TEST IF'ii' IS CONFUSABLE WITH THE REPRESENTANT OF THE ALREADY TREATED CLASSES.
    IF 'ii' IS CONFUSABLE WITH NONE OF THEM, A NEW CLASS IS CREATED, WITHH REPRESENTANT 'ii'.
    """
    global Tree
    global Code
    global Tour
    global Depth
    Depth = Depth + 1
    Tour = 1 - Tour
    Tree[Tour] = []
    Same_Code = list(Tree[1 - Tour]) 
    for i in range(len(Same_Code)) : 
        Same_Code[i] = [] 
    Code[Tour] = {}
    continuation = False
    for ii in Data :
        the_code = Code[1-Tour][ii] 
        the_list = Same_Code[the_code] 
        non_treated = True
        num_L = 0 
        while (num_L < len(the_list)) and non_treated:
            num = the_list[num_L]
            if (Code[1-Tour][ii] == Code[1-Tour][Tree[Tour][num][0]]) :
                if  Confusable (ii, Tree[Tour][num][0]) :
                    Tree[Tour][num].append(ii)
                    Code[Tour][ii] = num
                    non_treated = False
                else :
                    continuation = True
            num_L += 1
        if non_treated :
            Code[Tour][ii] = len(Tree[Tour])
            the_list.append(len(Tree[Tour]))
            Tree[Tour].append([ii])
    if continuation :
        printing () 
        Up_Date ()





print ('\n\n\n')
print ('John likre Audrey and Grace, Paul likes Marilyn and Liz,... :\n')

Construction_Data ()
Initial_Construction ()
Up_Date ()

print ('\n\n\n')
print ('From Figure 1 of "Distinguishing and Classifying from n-ary properties" :\n')

Construction_Data_Bis ()
Initial_Construction ()
Up_Date ()

print ('\n\n\n')
print ('From Figure 3 of "Distinguishing and Classifying from n-ary properties" :\n')

Construction_Data_Ter ()
Initial_Construction ()
Up_Date ()

print ('\n\n\n')

