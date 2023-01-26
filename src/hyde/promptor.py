WEB_SEARCH = """Please write a passage to answer the question.
Question: {}
Passage:"""


SCIFACT = """Please write a scientific paper passage to support/refute the claim.
Claim: {}
Passage:"""


ARGUANA = """Please write a counter argument for the passage.
Passage: {}
Counter Argument:"""


TREC_COVID = """Please write a scientific paper passage to answer the question.
Question: {}
Passage:"""


FIQA = """Please write a financial article passage to answer the question.
Question: {}
Passage:"""


DBPEDIA_ENTITY = """Please write a passage to answer the question.
Question: {}
Passage:"""


TREC_NEWS = """Please write a news passage about the topic.
Topic: {}
Passage:"""


MR_TYDI = """Please write a passage in {} to answer the question in detail.
Question: {}
Passage:"""


class Promptor:
    def __init__(self, task: str, language: str = 'en'):
        self.task = task
        self.language = language
    
    def build_prompt(self, query: str):
        if self.task == 'web search':
            return WEB_SEARCH.format(query)
        elif self.task == 'scifact':
            return SCIFACT.format(query)
        elif self.task == 'arguana':
            return ARGUANA.format(query)
        elif self.task == 'trec-covid':
            return TREC_COVID.format(query)
        elif self.task == 'fiqa':
            return FIQA.format(query)
        elif self.task == 'dbpedia-entity':
            return DBPEDIA_ENTITY.format(query)
        elif self.task == 'trec-news':
            return TREC_NEWS.format(query)
        elif self.task == 'mr-tydi':
            return MR_TYDI.format(self.language, query)
        else:
            raise ValueError('Task not supported')
