from typing import Dict, Sequence, Text

from newsapi import NewsAPI

from .config import Config


class NewsAPIWrapper(NewsAPI):
    """Just a simple wrapper for NewsAPI

    Arguments:
        NewsAPI {type} -- original NewsAPI class as base class    
    """

    def __init__(self, config: Config):
        self._config = config
        super().__init__(config.newsapi_key)

    def sources_lang(self, language: Text) -> Sequence[Dict]:
        """Gets sources available in NewsAPI with language filtering

        Arguments:
            language {Text} -- language of news sources. Format: 'en', 'pl', etc.

        Returns:
            Sequence[Dict] -- list of dicts containing info about sources
        """

        return self._filter_language(language, self.sources())

    def _filter_language(self, language: Text, sources: Sequence[Dict]) -> Sequence[Dict]:
        return list(filter(lambda info: info['language'] == language, sources))
