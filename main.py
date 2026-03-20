import pandas as pd
from WER import calculate_wer, calculate_cer
from datasetcreation import eckdaten, manuelleTranskriptionen, whisperLarge, vosk_model_ar_022_linto_110, vosk_model_ar_mgb2, vosk_model_ar_tn_01_linto, transkriptor, gemini_ara_IL, azureSpeech_ar_IL, whisperTurbo, whisperSmall

transkriptionen = [whisperLarge, whisperTurbo, whisperSmall, vosk_model_ar_022_linto_110, vosk_model_ar_mgb2, vosk_model_ar_tn_01_linto, transkriptor, gemini_ara_IL, azureSpeech_ar_IL]
transkriptionen_sorted = []
for i in range(len(transkriptionen)):
    sorted_by_first = sorted(transkriptionen[i], key=lambda tup: tup[0])
    transkriptionen_sorted.append(sorted_by_first)

manuelleTranskriptionen_sorted = sorted(manuelleTranskriptionen, key=lambda tup: tup[0])
eckdaten = sorted(eckdaten, key = lambda x: x[1])
df = pd.DataFrame(eckdaten, columns = ['Original File Name', 'Project File Name', 'YTLink', 'Dialekt','Länge'])

for q in range(len(transkriptionen_sorted)):
    WER_List = []
    CER_List = []
    for t1 in transkriptionen_sorted[q]:
        for t2 in manuelleTranskriptionen:
            if t1[0] == t2[0]:
                word_error_rate = calculate_wer(t2[1],t1[1])
                WER_List.append(word_error_rate)
                print("WER: ")
                print(word_error_rate)

                char_error_rate = calculate_cer(t2[1], t1[1])
                CER_List.append(char_error_rate)
                print("CER: ")
                print(char_error_rate)
    if q == 0:
        df['WER WhisperLarge'] = WER_List
        df['CER WhisperLarge'] = CER_List
    if q == 1:
        df['WER WhisperTurbo'] = WER_List
        df['CER WhisperTurbo'] = CER_List
    if q == 2:
        df['WER Small'] = WER_List
        df['CER Small'] = CER_List
    if q == 3:
        df['WER vosk_model_ar_022_linto_110'] = WER_List
        df['CER vosk_model_ar_022_linto_110'] = CER_List
    if q == 4:
        df['WER vosk_model_ar_mgb2'] = WER_List
        df['CER vosk_model_ar_mgb2'] = CER_List
    if q == 5:
        df['WER vosk_model_ar_tn_01_linto'] = WER_List
        df['CER vosk_model_ar_tn_01_linto'] = CER_List
    if q == 6:
        df['WER transkriptor'] = WER_List
        df['CER transkriptor'] = CER_List
    if q == 7:
        df['WER gemini_ara_IL'] = WER_List
        df['CER gemini_ara_IL'] = CER_List
    if q == 8:
        df['WER azureSpeech_ar_IL'] = WER_List
        df['CER azureSpeech_ar_IL'] = CER_List
    

df.to_csv("file1.csv", sep='\t', encoding='utf-8', index=False, header=True)

#print(df)

   
