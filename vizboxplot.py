import pandas as pd
import matplotlib.pyplot as plt
from main import df
import numpy as np
import seaborn as sns
from IPython.display import display

"""
    Mit den Boxplots hab ich Geduld und Zeit verloren und schließlich ChatGPT verwendet. Hat halbwegs funktioniert, muss reichen. ¯\_(ツ)_/¯
"""



# Long format
df= df.drop('Original File Name', axis='columns')
df= df.drop('Project File Name', axis='columns')
df= df.drop('YTLink', axis='columns')
df= df.drop('Dialekt', axis='columns')
df= df.drop('Länge', axis='columns')
display(df)

df_long = df.melt(var_name="metric_model", value_name="value")

# Split in zwei Spalten
df_long[["metric", "model"]] = df_long["metric_model"].str.split(" ", n=1, expand=True)
df_long = df_long.drop(columns=["metric_model"])

models = df_long["model"].unique()

data = []
labels = []

for m in models:
    #wer = df_long[(df_long["model"] == m) & (df_long["metric"] == "WER")]["value"]
    cer = df_long[(df_long["model"] == m) & (df_long["metric"] == "CER")]["value"]
    
    #data.extend([wer, cer])
    data.extend([cer])

    labels.extend([f"{m}"])
    #labels.extend([f"{m}\nWER"])


import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))
plt.boxplot(data)

plt.xticks(range(1, len(labels)+1), labels, rotation=45, ha="right")
plt.ylabel("Error Rate")
#plt.title("WER & CER per Model")

plt.tight_layout()


positions = []
pos = 1

for _ in models:
    positions.extend([pos])
    pos += 1  # Abstand zwischen Modellen

plt.figure(figsize=(14, 6))
plt.boxplot(data, positions=positions)

plt.xticks(positions, labels, rotation=45, ha="right")

plt.show()

"""
N=9
ind = np.arange(N)
width = 0.27 
##WhisperLarge
meanWER_WhisperLarge =df.loc[:, 'WER WhisperLarge']
meanCER_WhisperLarge =df.loc[:, 'CER WhisperLarge']
meanWER_WhisperTurbo =df.loc[:, 'WER WhisperTurbo']
meanCER_WhisperTurbo =df.loc[:, 'CER WhisperTurbo']
meanWER_WhisperSmall =df.loc[:, 'WER Small']
meanCER_WhisperSmall =df.loc[:, 'CER Small']
meanWER_vosk_model_ar_022_linto_110 =df.loc[:, 'WER vosk_model_ar_022_linto_110']
meanCER_vosk_model_ar_022_linto_110 =df.loc[:, 'CER vosk_model_ar_022_linto_110']

meanWER =[meanWER_WhisperLarge, meanWER_WhisperTurbo, meanWER_WhisperSmall, meanWER_vosk_model_ar_022_linto_110, df.loc[:, 'WER vosk_model_ar_mgb2'], df.loc[:, 'WER vosk_model_ar_tn_01_linto'], df.loc[:, 'WER transkriptor'], df.loc[:, 'WER gemini_ara_IL'], df.loc[:, 'WER azureSpeech_ar_IL']]
meanCER=[meanCER_WhisperLarge, meanCER_WhisperTurbo, meanCER_WhisperSmall, meanCER_vosk_model_ar_022_linto_110, df.loc[:, 'CER vosk_model_ar_mgb2'], df.loc[:, 'CER vosk_model_ar_tn_01_linto'],df.loc[:, 'CER transkriptor'], df.loc[:, 'CER gemini_ara_IL'], df.loc[:, 'CER azureSpeech_ar_IL']]
labellist = ['Whisper\n large-v3', 'Whisper\n large-v3-turbo', 'Whisper\n small', 'vosk_model\n_ar_022_linto_110', 'vosk_model\n_ar_mgb2', 'vosk_model\n_ar_tn_01_linto', 'Transkriptor', 'gemini\n_ara_IL', 'azureSpeech\n_ar_IL']

sns.boxplot(data=df.explode('WER WhisperLarge'), x='index', y='WER WhisperLarge', palette='magma')



def sort_both(list1, list2,list3):
    pairs = list(zip(list1, list2, list3))
    pairs_sorted_index0 = sorted(pairs, key=lambda x: x[0])
    pairs_sorted_index1 = sorted(pairs, key=lambda x: x[1])
    return pairs_sorted_index0, pairs_sorted_index1



#meanWER_sorted, meanCER_sorted = sort_both(meanWER,meanCER, labellist)
#a_sorted, b_sorted, labels_sorted = zip(*meanCER_sorted)

fig = plt.figure()
ax = plt.subplot(111)
rects1 = ax.boxplot(ind, meanWER)
rects2 = ax.boxplot(ind + width,meanCER)
#


ax.set_ylabel('Percent')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Whisper\n large-v3', 'Whisper\n large-v3-turbo', 'Whisper\n small', 'vosk_model\n_ar_022_linto_110', 'vosk_model\n_ar_mgb2', 'vosk_model\n_ar_tn_01_linto', 'Transkriptor', 'gemini\n_ara_IL', 'azureSpeech\n_ar_IL') )
#ax.legend( (rects1[0], rects2[0]), ('WER', 'CER') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

plt.title('Mean Word Error Rate & Character Error Rate \nfor selected SpeechRec Models\n sorted by CER')

plt.show()





def barplot_sorted(meanWER, meanCER,ind, width):

    fig = plt.figure()
    ax = plt.subplot(111)
    rects1 = ax.bar(ind, meanWER, width, color='royalblue')
    rects2 = ax.bar(ind+width, meanCER, width, color='plum')
    #


    ax.set_ylabel('Percent')
    ax.set_xticks(ind+width)
    ax.set_xticklabels( ('Whisper\n large-v3', 'Whisper\n large-v3-turbo', 'Whisper\n small', 'vosk_model\n_ar_022_linto_110', 'vosk_model\n_ar_mgb2', 'vosk_model\n_ar_tn_01_linto', 'Transkriptor', 'gemini\n_ara_IL', 'azureSpeech\n_ar_IL') )
    ax.legend( (rects1[0], rects2[0]), ('WER', 'CER') )

    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                    ha='center', va='bottom')

    plt.title('Mean Word Error Rate & Character Error Rate \nfor selected SpeechRec Models')

    plt.show()


sort_both(meanWER, meanCER)

"""
