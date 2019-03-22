# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:01:53 2019

@author: Fachry Firdaus
"""
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir
import sys
 
ix = open_dir("indexdir")
 
# query_str is query string
lanjut = "Y"

while(lanjut=="Y"):
    query_str = input('Apa yang ingin anda telusuri? \n')
# Top 'n' documents as result
    topN = 50
    with ix.searcher(weighting=scoring.Frequency) as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        results = searcher.search(query,limit=topN)
        for i in range(topN):
            print("Nama dokumen : ",results[i]['title'], "\tscore : ", str(results[i].score),"\n",results[i]['textdata'],"\n")
    
    lanjut = input("Ingin menelusuri lagi? Y/N \n")