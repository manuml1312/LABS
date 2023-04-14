print("Am in")
from pymongo import MongoClient
# from transformers import pipeline
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

client = MongoClient('mongodb+srv://root:iwbM0Q9GVzOmsEF6@cluster0.zovhiec.mongodb.net/?retryWrites=true&w=majority')
mydb=client['AI360']
myc1=mydb['NLP']

d={}
i=0
for x in myc1.find({},{'_id':0}):
  d[i]=x
  i=i+1
print(d)
# summarizer=pipeline('summarization',model='lidiya/bart-base-samsum')

# df=pd.DataFrame(d)
# text=list(df[0].values)

# x=''
# ops={}
# for i in d[0].keys():
#   x=summarizer(d[0][i])
#   ops[i]=x[0]['summary_text']


# client = MongoClient('mongodb+srv://Manu:Manu1312@cluster0.ja3xqvn.mongodb.net/?retryWrites=true&w=majority')
# mydb=client['ai_360']
# myc2=mydb['summaries']
# myc2.insert_one(ops)




