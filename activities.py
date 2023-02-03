import  pandas as pd

def build():
 obj = pd.read_excel('ActivitiesServices.xlsx')
 keys = obj.keys()[7:]
 l = list(obj.columns)
 for i in range(len(l)):
     l[i] = str(l[i]).replace('\xa0','')
     l[i] = str(l[i]).replace(' ', '')
 obj.columns = l
 keys = obj.keys()[7:]
 headers = keys
 emotions_to_events = dict()
 for i in range(len(headers)):
     head = str(headers[i]).strip()
     emotions_to_events[head] = []
     for j in range(len(head)):
         if obj[headers[i]][j] == 1:
             df_simple = dict(obj.iloc[j][:7])
             emotions_to_events[head].append(df_simple)
     return emotions_to_events        