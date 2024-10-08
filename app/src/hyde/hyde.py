import numpy as np


class HyDE:
    def __init__(self, promptor, generator, encoder, searcher):
        self.promptor = promptor
        self.generator = generator
        self.encoder = encoder
        self.searcher = searcher
    
    def prompt(self, query):
        return self.promptor.build_prompt(query)

    def generate(self, query):
        prompt = self.promptor.build_prompt(query)
        hypothesis_documents = self.generator.generate(prompt)
        return hypothesis_documents
    
    def encode(self, query, hypothesis_documents):
        all_emb_c = []
        for c in [query] + hypothesis_documents:
            c_emb = self.encoder.encode(c)
            all_emb_c.append(np.array(c_emb))
        all_emb_c = np.array(all_emb_c)
        avg_emb_c = np.mean(all_emb_c, axis=0)
        hyde_vector = avg_emb_c.reshape((1, len(avg_emb_c)))
        return hyde_vector
    
    def search(self, hyde_vector, k=10):
        hits = self.searcher.search(hyde_vector, k=k)
        return hits
    

    def e2e_search(self, query, k=10):
        prompt = self.promptor.build_prompt(query)
        hypothesis_documents = self.generator.generate(prompt)
        hyde_vector = self.encode(query, hypothesis_documents)
        hits = self.searcher.search(hyde_vector, k=k)
        return hits