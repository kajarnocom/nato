# nato
Show the interest in Nato as measured by Wikipedia article views, from 24.2.2022 onwards, compared to 2016-2021.

Spoiler alert: it exploded. More in `RESULTS.md`.

## Parameters
This sub-100-line program snippet takes the Wikidata code for Nato, Q7184 as its input. The dates (24.2.2022, 2016-2021) are hard coded.

## Results
The pure code output is shared in `lang_stat.csv`, so the user does not need to rerun the program just to view the results. This is in the interest of saving Wikipedia resources.

Beware that the presence of right-to-left languages (Arabic, Farsi, Hebrew, Yiddish) may complicate the browsing of the .csv file in some browsers.

A more comprehensive analysis (with manually added data based on the number of native speakers by language) is shared in `nato.csv` and `nato.pdf`. This is so far in Swedish. 

The results in `RESULTS.md` show a significantly higher interest in the NATO articles in languages spoken close to the North-Eastern border of Nato. Estonian, Finnish, Latvian, Norwegian, Swedish rank top five when put into proportion with the number of native speakers. There seems to be no correlation to whether the countries where the language is spoken currently are part of NATO or not. 

## Program logic
### title_by_lang
Using the given Wikidata code, identify the titles for the Wikipedia article on Nato for all "significant" languages. Define "significant" as a language with a two letter language code (eg. de for German, but not bar for Bavarian).

### stat_by_article
For the Wikipedia articles in each of the languages, retrieve daily statistics for the ten days from 24.2.2022 onwards and monthly statistics for 2016-2021. Sum the numbers.

Create statistics with the per-day number of views for both the short ("fresh") and the long ("all") time periods. Compare the two in a ratio, showing the explosive growth.

### wikipedia_stats
Overall routine that first calls title_by_lang, then loops through the found articles, calling stat_by_article for them. Last saving them.

The saved list is uploaded to Github on 

## Further analysis by language size, NATO membership

The number of views by language could be put into proportion by comparing the views to the number of native speakers of the language in question.

This part was done manually in a spreadsheet, entering the number of speakers through a SPARQL query https://w.wiki/4w4s kindly provided by Robert Silén.

Not languages but countries are members of NATO. Some languages (eg. English, French, German, Serbocroatian, Spanish) are officially spoken both in NATO membership countries and outside them. Languages not official in any current NATO country are colour-coded in the output. Also here, there is no one-to-one relationship between language and country (eg. Swedish spoken both in Finland and Sweden, neither of which are NATO members).    

The output of the manually created spreadsheet is shared as `nato.csv` and `nato.pdf`.

## Prerequisites
`pip install mwviews` to get Media Wiki statistics from Wikipedia

## Known bugs
* language codes for bihari and tamil (bh and ta) produce bugs
