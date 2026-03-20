# ASR_ARA


## Übersicht
ASR Ergbnisse liegen in Out, die Visualisierungen liegen unter figs, die manuelle Transkription unter manuelle Transkription.

## Datensatz

[Youtube Link](https://youtube.com/playlist?list=PLd4j42hRYCNWjih3bCiIEzne2Dd6KfKeT&si=JlwDJaey8Uitt6yL)


## Code

Der Code ist sehr unstrukturiert. Für die jeweiligen ASR-Systeme habe ich wenn möglich eigene Python Scripts erstellt und einzeln ausgeführt. Whisper und VOSK habe ich schließlich direkt im Terminal und die Befehle in den entsprechenden .py Dateien lediglich hinterlegt. Der Code in gemini.py wurde nicht lokal ausgeführt, sondern direkt in der Google Cloud Console.

## Ergebnisse
### WER
Project File Name |Dialekt |Länge |WER WhisperLarge |WER WhisperTurbo | WER Whisper Small | WER vosk ar_022_linto_110 | WER vosk ar_mgb2 | WER vosk ar_tn_01_linto | WER transkriptor | WER gemini_ara_IL | WER azureSpeech_ar_IL|
| --- | --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |
| AlJazeera | MSA|  04:15 |  0.1277890467 |  0.1054766734 |  0.2292089249 |  0.1419878296 |  0.1359026369 |  0.6937119675 |  0.3468559838 |  0.4340770791 |  0.2170385396 |
| ArchitektLangsam | Levantine (Gaza) |  00:44 |  0.2307692308 |  0.1666666667 |  0.2307692308 |  0.3333333333 |  0.2820512821 |  0.4871794872 |  0.3974358974 |  0.5512820513 |  0.2564102564 |
| ArchitektSchnell | Levantine (Gaza) |  00:58 |  0.2307692308 |  0.2051282051 |  0.4102564103 |  0.3974358974 |  0.4102564103 |  0.8205128205 |  0.4615384615 |  0.641025641 |  0.4487179487 |
| LernvideoSchule | MSA |  01:43 |  0.0404040404 |  0 |  0.1212121212 |  0.07070707071 |  0.1111111111 |  0.5757575758 |  0.2828282828 |  0.3535353535 |  0.5050505051 |
| Tire | Levantine (Israel) |  04:42 |  0.429844098 |  0.4766146993 |  0.7171492205 |  0.5567928731 |  0.579064588 |  0.846325167 |  0.7527839644 |  0.5634743875 |  0.4832962138 |
| Werbevideo | MSA |  03:23 |  0.1114285714 |  0.09428571429 |  0.1742857143 |  0.1628571429 |  0.1771428571 |  0.7828571429 |  0.28 |  0.54 |  0.2685714286 |
