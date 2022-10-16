from googlesearch import search


class GoogleSearch:
    """A class for managing searches using googlesearch-python"""
    def __init__(self, terms, state):
        """
        Initialize the attributes of the query.
        Defaults to English, 10 results per page, and terminates the search after 10 results.
        Explicitly exclude websites from search by setting exclude attribute
        to string in form of "-inurl:website1.com -inurl:website2.com ..."
        """
        self.terms = terms
        self.state = state
        self.lang = "en"
        self.num = 10
        self.start = 1
        self.stop = 10
        self.pause = 2.0
        self.agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
                     "(KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        self.exclude = ""

    def query(self):
        """Return query as a list."""
        return list(search(
            query=f"{self.terms} {self.state} {self.exclude}",
            num=self.num, lang=self.lang, start=self.start, stop=self.stop, pause=self.pause, user_agent=self.agent))
