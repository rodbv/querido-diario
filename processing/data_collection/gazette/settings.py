BOT_NAME = "gazette"
SPIDER_MODULES = ["gazette.spiders"]
NEWSPIDER_MODULE = "gazette.spiders"
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
    "gazette.pipelines.GazetteDateFilteringPipeline": 50,
    "gazette.pipelines.DefaultValuesPipeline": 60,
    "scrapy.pipelines.files.FilesPipeline": 100,
    "gazette.pipelines.SQLDatabasePipeline": 300,
}
FILES_STORE = "/mnt/data/"

QUERIDODIARIO_DATABASE_URL = "sqlite:///querido-diario.db"
