class L_Language:


    def __init__(self, seed, axioms):
        self.seed = seed
        self.axioms = axioms
    
    def loop_n_times(self, n):
        sentence = self.seed

        for i in range(0,n):
            new_sentence = ""

            for c in sentence:
                if c in self.axioms.keys():
                    new_sentence += self.axioms[c]
                else:
                    new_sentence += c
            sentence = new_sentence

        return sentence