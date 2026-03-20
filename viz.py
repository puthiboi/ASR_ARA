import pandas as pd
import matplotlib.pyplot as plt
from main import df
import numpy as np

#df = df[~df['Dialekt'].isin(['Levantine (Israel)', 'Levantine (Gaza)'])]
df = df[df['Project File Name'].isin(['Tire'])]

print(df)
# reading the database
#data = pd.read_csv("/Users/anisheit/Documents/Python/file1.csv")
N=9
ind = np.arange(N)
width = 0.27 
##WhisperLarge
meanWER_WhisperLarge =df.loc[:, 'WER WhisperLarge'].mean() *100
meanCER_WhisperLarge =df.loc[:, 'CER WhisperLarge'].mean() * 100
meanWER_WhisperTurbo =float(df.loc[:, 'WER WhisperTurbo'].mean())*100
meanCER_WhisperTurbo =float(df.loc[:, 'CER WhisperTurbo'].mean())*100
meanWER_WhisperSmall =float(df.loc[:, 'WER Small'].mean())*100
meanCER_WhisperSmall =float(df.loc[:, 'CER Small'].mean())*100
meanWER_vosk_model_ar_022_linto_110 =df.loc[:, 'WER vosk_model_ar_022_linto_110'].mean() *100
meanCER_vosk_model_ar_022_linto_110 =df.loc[:, 'CER vosk_model_ar_022_linto_110'].mean() *100

meanWER =[meanWER_WhisperLarge, meanWER_WhisperTurbo, meanWER_WhisperSmall, meanWER_vosk_model_ar_022_linto_110, df.loc[:, 'WER vosk_model_ar_mgb2'].mean()*100, df.loc[:, 'WER vosk_model_ar_tn_01_linto'].mean()*100, df.loc[:, 'WER transkriptor'].mean()*100, df.loc[:, 'WER gemini_ara_IL'].mean()*100, df.loc[:, 'WER azureSpeech_ar_IL'].mean()*100]
meanCER=[meanCER_WhisperLarge, meanCER_WhisperTurbo, meanCER_WhisperSmall, meanCER_vosk_model_ar_022_linto_110, df.loc[:, 'CER vosk_model_ar_mgb2'].mean()*100, df.loc[:, 'CER vosk_model_ar_tn_01_linto'].mean()*100,df.loc[:, 'CER transkriptor'].mean()*100, df.loc[:, 'CER gemini_ara_IL'].mean()*100, df.loc[:, 'CER azureSpeech_ar_IL'].mean()*100]
labellist = ['Whisper\n large-v3', 'Whisper\n large-v3-turbo', 'Whisper\n small', 'vosk_model\n_ar_022_linto_110', 'vosk_model\n_ar_mgb2', 'vosk_model\n_ar_tn_01_linto', 'Transkriptor', 'gemini\n_ara_IL', 'azureSpeech\n_ar_IL']

def sort_both(list1, list2,list3):
    pairs = list(zip(list1, list2, list3))
    pairs_sorted_index0 = sorted(pairs, key=lambda x: x[0])
    pairs_sorted_index1 = sorted(pairs, key=lambda x: x[1])
    return pairs_sorted_index0, pairs_sorted_index1



meanWER_sorted, meanCER_sorted = sort_both(meanWER,meanCER, labellist)
a_sorted, b_sorted, labels_sorted = zip(*meanCER_sorted)

fig = plt.figure()
ax = plt.subplot(111)
rects1 = ax.bar(ind, a_sorted, width, color='royalblue')
rects2 = ax.bar(ind+width, b_sorted, width, color='plum')
#


ax.set_ylabel('Percent')
ax.set_xticks(ind+width)
ax.set_xticklabels( (labels_sorted) )
ax.legend( (rects1[0], rects2[0]), ('WER', 'CER') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

plt.title('Mean Word Error Rate & Character Error Rate\n Tire \nfor selected SpeechRec Models\n sorted by CER')

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