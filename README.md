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

### CER
Project File Name |Dialekt |Länge |WER WhisperLarge |WER WhisperTurbo | WER Whisper Small | WER vosk ar_022_linto_110 | WER vosk ar_mgb2 | WER vosk ar_tn_01_linto | WER transkriptor | WER gemini_ara_IL | WER azureSpeech_ar_IL|
| --- | --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |  --- |
| AlJazeera | MSA|  04:15 |  0.1004598514 |  0.09161655465 |  0.1234524231 |  0.1114255394 |  0.1085956845 |  0.3731871242 |  0.2900601344 |  0.1779271312 |  0.1047046339 |
| ArchitektLangsam | Levantine (Gaza) |  00:44 |  0.05882352941 |  0.05411764706 |  0.08941176471 |  0.1152941176 |  0.1058823529 |  0.2117647059 |  0.2376470588 |  0.1294117647 |  0.05176470588 |
| ArchitektSchnell | Levantine (Gaza) |  00:58 |  0.08705882353 |  0.07294117647 |  0.1647058824 |  0.1482352941 |  0.1505882353 |  0.5317647059 |  0.2776470588 |  0.2329411765 |  0.08705882353 |
| LernvideoSchule | MSA |  01:43 |  0.1028446389 |  0.04814004376 |  0.1006564551|  0.04595185996 |  0.08315098468 |  0.3326039387 |  0.2035010941 |  0.1094091904 |  0.09409190372 |
| Tire | Levantine (Israel) |  04:42 |  0.2052761748 |  0.2201154163 |  0.3664468261 |  0.3318219291 |  0.339653751 |  0.4744435284 |  0.48928277 |  0.2774113768 |  0.1962077494 |
| Werbevideo | MSA |  03:23 |  0.07684580613 |  0.04771471622 |  0.05725765947 |  0.06479156203 |  0.06730286288 |  0.4239075841 |  0.2124560522 |  0.1662481165 |  0.05775991964 |
