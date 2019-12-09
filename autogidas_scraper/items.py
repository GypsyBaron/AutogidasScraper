# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def remove_whitespace(value):
    return value.strip()

def remove_whitespace_inside(value):
    return value.replace(" ", "")

class AutogidasScraperItem(scrapy.Item):
    marke = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    modelis = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    kaina = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace, remove_whitespace_inside),
        output_processor = TakeFirst()
    )
    metai = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    variklis = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    kuro_tipas = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    kebulo_tipas = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    spalva = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    pavaru_deze = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    rida = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    varomieji_ratai = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    defektai = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    vairo_padetis = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    duru_skaicius = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    sedymu_vietu_skaicius = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    cilindru_skaicius = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    pavaru_skaicius = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    svoris = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    vin_kodas = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    ratlankiai = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    co2 = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    euro_standartas = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    pirmoji_registracijos_salis = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    ta = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_whitespace),
        output_processor = TakeFirst()
    )
    # modelis = scrapy.Field()
    # metai = scrapy.Field()
    # variklis = scrapy.Field()
    # kuro_tipas = scrapy.Field()
    # kebulo_tipas = scrapy.Field()
    # spalva = scrapy.Field()
    # pavaru_deze = scrapy.Field()
    # rida = scrapy.Field()
    # varomieji_ratai = scrapy.Field()
    # defektai = scrapy.Field()
    # vairo_padetis = scrapy.Field()
    # duru_skaicius = scrapy.Field()
    # sedymu_vietu_skaicius = scrapy.Field()
    # vin_kodas = scrapy.Field()
    # ratlankiai = scrapy.Field()
    # pirmoji_registracijos_salis = scrapy.Field()
