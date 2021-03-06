#!/usr/bin/env python
# coding: utf-8

"""
This script takes in raw_html files and exports a clean JSON with the following information:

ToDo:
 * Document

JSON includes main text.
"""

import os
import json
from Article import Article # Article class from our utilities

files = os.listdir('../data/raw_html')

path = '../data/clean_json'
if not os.path.exists(path):
    os.makedirs(path)

for file in files:
    # Open its HTML and parse it.
    with open(f'../data/raw_html/{file}/{file}.html') as f:
        html = f.read()

    # Open the article's metadata
    with open(f'../data/raw_html/{file}/{file}.json') as f:
        meta = json.loads(f.read())

    # We feed the HTML and metadata to the Article class.
    article = Article(html = html, meta = meta)

    # We save the file using the method from the Article class.
    article.saveDict(path)
