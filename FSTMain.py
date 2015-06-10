'''
Created on 19 May 2015

@author: Russell
'''
from FiniteStateTransducer import FiniteStateTransducer
SEG = '<s>'

if __name__ == '__main__':
    prosodic = FiniteStateTransducer()
    
#     state = prosodic.start_state()
#     sentence = "the cat"
#     words = sentence.split()
#     
#     for w in words:
#         prosodic.add_arc(state, w, w, 1.0, prosodic.new_state())
#         state = prosodic.newest_state()
#         nxt = prosodic.new_state()
#         prosodic.add_arc(state, '', '', 0.5, nxt)
#         prosodic.add_arc(state, '', SEG, 0.5, nxt)
#         state = nxt
    
    prosodic.add_arc(0, 'the','the', 1.0, prosodic.new_state())
    the = prosodic.newest_state()
    prosodic.add_arc(the, 'cat','cat',1.0, prosodic.new_state())
    prosodic.add_arc(the, 'dog','dog',1.0, prosodic.new_state())
    dog = prosodic.newest_state()
    prosodic.add_arc(dog, 'jumped','jumped',1.0, prosodic.new_state())
    prosodic.add_arc(dog, '','',1.0, prosodic.new_state())   
    prosodic.add_arc(prosodic.newest_state(), 'jumped','jumped',1.0, prosodic.new_state())
        
    print prosodic
    
    st = prosodic.start_state()
    
    print prosodic.get_poss_transitions(0, 'the')
    paths = prosodic.get_possible_paths('the dog jumped')
    print paths