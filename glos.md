# Glósur

Þegar verið er að hugsa hvort eigi að bæta við einum eða draga frá einn í forritun, þá er gott að hugsa sértilvik, hvað ef len(dna) == len(pattern) t.d.

Þegar reikna á entropy þarf að passa sér tilvik þegar p_j = 0 (því log_2(0) er óskilgreint)
Hæsta óreiða (2) eru þegar líkur eru jafn háar. 
Lágmarksóreiða er þegar einn dálkurinn er (1,0,0,0). 0 er lágmarks óreiða.

Passa að í Gibbs Sampler þarf víst að passa að keyra 1001 skref í stað 1000..
Athuga að normalizea líkur þegar "teningi" er kastað. Summa þeirra þarf að vera 1.


