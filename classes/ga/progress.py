import numpy as np
from operator import attrgetter

from ..population import Population


class GAProgress:
    def __init__(self):
        self.gens = []
        self.means = []
        self.mins = []
        self.maxs = []
        self.pops = Population()

    def update(self, pop):
        self.gens.append(len(self.gens))
        self.pops.add_subpopulation(pop)
        
        if any(x.progress_params for x in pop):
            unscaled_var_mat = np.matrix([
                x.progress_params for x in pop if not 
                x.fitness_fail])

            self.maxs.append(np.max(unscaled_var_mat, axis=0).tolist()[0])
            self.mins.append(np.min(unscaled_var_mat, axis=0).tolist()[0])
            self.means.append(np.mean(unscaled_var_mat, axis=0).tolist()[0])
            
        else:
            self.means.append(pop.mean(lambda x : x.fitness))
            self.maxs.append(max(x.fitness for x in pop))
            self.mins.append(min(x.fitness for x in pop))
        

    def normalize(self, norm_func):
        norm_func(self.pops)
        
        self.gens = []
        self.mins = []
        self.means = []
        self.maxs = []
        for i, gen in enumerate(self.pops.populations, 1):
            self.gens.append(i)
            self.mins.append(min(gen, key=attrgetter('fitness')).fitness)
            self.means.append(gen.mean(attrgetter('fitness')))
            self.maxs.append(max(gen, key=attrgetter('fitness')).fitness)