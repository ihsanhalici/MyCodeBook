from scrapy.item import Item, Field

class OrumcekItem(Item):
    title       = Field()
    description = Field()
    #post        = Field()
    date        = Field()