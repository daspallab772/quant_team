## libraries and Modules call
import math


#class for binomial tree
class binomial_tree:
    def __init__(self,tree_len,curr_asst_pr,ast_up_rt,ast_dwn_rt):
            self.tree_len=tree_len
            self.curr_asst_pr=curr_asst_pr
            self.ast_up_rt=ast_up_rt
            self.ast_dwn_rt=ast_dwn_rt
            
    def price_n_step(self):
        self.total_tree=[[self.curr_asst_pr]]

        for iter in list(range(1,self.tree_len+1)):
            node_values=[0.0]*(iter+1)

            for x in list(range(0,iter)):
                node_values[x]= (self.total_tree[(iter-1)][x])*self.ast_up_rt
                node_values[x+1]= (self.total_tree[(iter-1)][x])*self.ast_dwn_rt
               
            self.total_tree=self.total_tree+([node_values])

        return(self.total_tree)


#calling binoial tree for testing
b1=binomial_tree(5,100.0,1.5,0.5)
print(b1.price_n_step())
