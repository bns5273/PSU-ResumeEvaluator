import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  iam_apikey='BU11gy3frJMRMKz4XQ_sPJ_HGF3p-qEr74xUlEVTWvsY',
  version='2018-03-19')

response = natural_language_understanding.analyze(
  text='IBM is an American multinational technology company '
       'headquartered in Armonk, New York, United States, '
       'with operations in over 170 countries.',
  features=Features(
    entities=EntitiesOptions(
      emotion=True,
      sentiment=True,
      limit=2),
    keywords=KeywordsOptions(
      emotion=True,
      sentiment=True,
      limit=2))).get_result()

print(json.dumps(response, indent=2))
