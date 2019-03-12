from pprint import pprint

from event_reactions import Config, NewsAPIWrapper

if __name__ == '__main__':
    config = Config('./config.json')
    api = NewsAPIWrapper(config)

    sources = api.sources_lang('en')
    pprint(sources)
