import itertools

from google.cloud.translate_v2.client import ENGLISH_ISO_639
from google.cloud import translate_v2 as translate
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/ladmin/Downloads/algolia-344913-a591a17dca04.json"
client = translate.Client()
import cyrtranslit 
res = client.translate("However, his form this season has drawn some scrutiny and United have slipped to sixth in the Premier League table in a turbulent campaign that has seen manager Ole Gunnar Solskjaer sacked and Ralf Rangnick take charge as interim head coach.", target_language="mk", source_language=ENGLISH_ISO_639)["translatedText"].split(".")
print(res)
f1 = "/Users/ladmin/Desktop/TestClassla21.csv"
f2 = "/Users/ladmin/Desktop/PrevodMakedonski.csv"
