"""
nato_kaj.py: Analyse interest for Nato in Wikipedias by language
- compare overall interest 2016-2021 with the ten days starting 24.2.2022
"""

from mwviews.api import PageviewsClient
import urllib.request

def stat_by_article(lang, article):
    p = PageviewsClient(user_agent="<kaj@projektfredrika.fi>")
    wikipedia = f'{lang}.wikipedia'
    try:
        fresh = p.article_views(wikipedia, article, start='20220224', end='20220305')
        all = p.article_views(wikipedia, article, start='20160101', end='20211231', granularity='monthly')
        c_fresh = 0
        for row in fresh:
            c_fresh += fresh[row][article]
        c_all = 0
        for row in all:
            c_all += all[row][article]
        fresh_per_day = c_fresh / 10
        all_per_day = c_all / 2192 # 6 x 365 + 2
        ratio = fresh_per_day / all_per_day 
        s = f"{lang},{article},{c_fresh},{c_all},{fresh_per_day:.0f},{all_per_day:.0f},{ratio:.0f}"
        print(s)
        return s
    except Exception as e:
        print(f"---{lang} {article}")
        return ""

def title_by_lang(q_code):
    url = f"https://www.wikidata.org/w/api.php?action=wbgetentities&format=xml&props=sitelinks&ids={q_code}&sitefilter=xxwiki"
    try:
        fp = urllib.request.urlopen(url)
    except Exception as e:
        print(e)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    languages = []
    for i, row in enumerate(mystr.split('<sitelink site="')):
        if i == 0:
            continue
        wiki, skip1, title, skip2 = row.split('"')
        minor_language = len(wiki) > 6
        if minor_language:
            continue
        title = title.replace("&#039;", "'") 
        title = title.replace("&quot;", '"')
        title = title.replace(" ", "_")
        language = wiki[0:2]
        languages.append([language, title])
    return languages

def wikipedia_stats(q_code):
    s = "lang,title,days,years,perday1,perday2,factor\n"
    languages = title_by_lang(q_code)
    for lang, title in languages:
        stat = stat_by_article(lang, title) 
        if stat != "":
            s +=  stat + "\n"
    out_file = "lang_stat.csv"
    with open(out_file, "w") as fh:
        fh.write(s)
    print(f"Wrote wikipedia stats for Q-code {q_code} into {out_file} {len(s)}")

nato = "Q7184"
wikipedia_stats(nato)