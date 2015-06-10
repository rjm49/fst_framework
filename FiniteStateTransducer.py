'''
Created on 19 May 2015

@author: Russell
'''

class FiniteStateTransducer(object):
    '''
    classdocs
    '''
    
    #(Sigma, Q, E, i, F, lambda, rho)

    def __init__(self):
        '''
        Constructor
        '''
        self._num_states=0
        self.alphabet = []
        #self.states = []
        
        self.arcs = []
        self.arcs_by_start = {}
        self.arcs_by_end = {}
        
        self.final_states = []
        self.initial_weight = 0
        self.final_weight = {lambda args: None }
        self.state = 0
       
    def start_state(self):
        self.state = 0
        return self.state
       
    def new_state(self):
        self._num_states += 1
        self.state = self._num_states
        return self.state
       
    def newest_state(self):
        return self._num_states

    def add_arc(self, prev, l_in, l_out, wgt, nxt):
        arc = (prev, l_in, l_out, wgt, nxt)
        if arc not in self.arcs:
            self.arcs.append(arc)
            
            if prev not in self.arcs_by_start.keys():
                self.arcs_by_start[prev]=[]

            if nxt not in self.arcs_by_end.keys():
                self.arcs_by_end[nxt]=[]
            
            self.arcs_by_start[prev].append(arc)
            self.arcs_by_end[nxt].append(arc)
        
        
    def get_poss_transitions(self, state, label):
        key = (state, label)
        all_arcs = self.transitions(state)
        poss_arcs = []
        for arc in all_arcs:
            needs_label = arc[1]
            if not needs_label or needs_label==label:
                poss_arcs.append(arc)
        return poss_arcs
    
    def transitions(self,state):
        return self.arcs_by_start[state]
    
    
    def get_possible_paths(self, seq):
        labels = seq.split()
        s = self.start_state()
        return self._get_possible_paths([], [],s,labels)


    def _get_possible_paths(self, all_paths, history, cstate, remlabs):
        #history is the arcs we took to get here
        #cstate is the current state of the fst
        #remlabs is the labels remaining
        if not remlabs:
            print 'no more labels...', history
            pathweight = 0.0
            for step in history:
                pathweight += step[3]
            all_paths.append((history, pathweight))            
        else:
            poss_arcs = self.get_poss_transitions(cstate, remlabs[0])
            if not poss_arcs:
                print 'no more possible arcs'
            else:
                for arc in poss_arcs:
                    inpath2 = list(history)
                    inpath2.append(arc)
                    nxt = arc[4]
                    if len(arc[1]): #if the arc accepts a label
                        remlabs2=remlabs[1:]
                    else:
                        remlabs2=remlabs   
                    self._get_possible_paths(all_paths, inpath2, nxt, remlabs2)
        return all_paths
        
    def __str__(self):
        strg = ''
        for a in self.arcs:
            strg += (str(a) + '\n')
        return strg    
    
     