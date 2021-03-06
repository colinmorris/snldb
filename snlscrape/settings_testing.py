# Some settings overrides for unit tests
import settings

ITEM_PIPELINES = settings.ITEM_PIPELINES.copy()
del ITEM_PIPELINES['snlscrape.pipelines.MultiJsonExportPipeline']
# Don't include the json output pipeline during testing

LOG_LEVEL = 'WARN'

# Currently there are no unit tests for crawling ratings from IMDB.
SNL_SCRAPE_IMDB = False
