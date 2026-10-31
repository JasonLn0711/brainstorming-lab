from pathlib import Path
import csv
import json

p = Path(__file__).resolve().parent
sources = {
    'S01': 'https://www.cna.com.tw/news/aipl/202610300323.aspx',
    'S02': 'https://www.knews.com.tw/news/A67D351B5D30D9D46E6079BD4655D045',
    'S03': 'https://puma.taipei/policies/都市微森林',
    'S04': 'https://www.gov.taipei/News_Content.aspx?n=74806083EBDF5A03&s=28831B7E8102EB08&sms=72544237BBE4C5F6',
    'S05': 'https://health.gov.taipei/News_Content.aspx?n=4F01EBDF8F61F315&s=DCBFD4023728AD25&sms=72544237BBE4C5F6',
    'S06': 'https://news.pts.org.tw/article/833610',
    'S07': 'https://www.dorts.gov.taipei/cp.aspx?n=E564EC7795D2B5BC&s=A2FB381EE02F7F35',
    'S08': 'https://sec.gov.taipei/News_Content.aspx?n=49B4C3242CB7658C&s=C628D074125A7699&sms=72544237BBE4C5F6',
    'S09': 'https://tct.gov.taipei/News_Content.aspx?n=B4C9AF5D5D4BF947&s=5A90280F3910EEAC&sms=72544237BBE4C5F6',
    'S10': 'https://www.gov.taipei/News_Content.aspx?n=F0DDAF49B89E9413&s=2901CE52FEA18C4A&sms=72544237BBE4C5F6',
    'S11': 'https://www.gov.taipei/News_Content.aspx?n=F0DDAF49B89E9413&s=B3DED2A7DE8D2120&sms=72544237BBE4C5F6',
    'S12': 'https://news.tvbs.com.tw/politics/4043894',
    'S13': 'https://www.fountmedia.io/article/437744',
    'S14': 'https://www.gov.taipei/News_Content.aspx?n=D6946078AE437FF0&s=04D0B4F162ED6055&sms=14AEF9A8536E3B5E',
    'S15': 'https://www.netflix.com/tudum/articles/how-to-watch-alex-honnold-skyscraper-climb-live-netflix',
    'S16': 'https://uro.gov.taipei/News_Content.aspx?n=FDB0CAB1DD42E805&s=4D7E11B11A945852&sms=72544237BBE4C5F6',
    'S17': 'https://tct.gov.taipei/News_Content.aspx?n=B4C9AF5D5D4BF947&s=DDA779781380304A&sms=72544237BBE4C5F6',
    'context': '依相鄰語句及同音字校訂；尚未人工聽校，不代表網路證實原句。',
}
rules = []
def add(old, new, source):
    rules.append((old, new, source))
for old in ['沈柏楊', '沈柏揚', '沈博洋', '沈榮洋', '沈榮耀', '沈不揚', '沈浦洋']:
    add(old, '沈伯洋', 'S01')
for old in ['講完先生', '蔣萬先生', '蔣安先生', '蔣灣先生']:
    add(old, '蔣萬安先生', 'S01')
for old, new in [('沈博雁消息人','沈伯洋先生'),('沈瑋琳','沈委員'),('蔣華安','蔣萬安'),('黃欣樺','黃星樺'),('李雯儀','李文儀'),('凡啟明','樊啓明'),('黃映瑩','黃彥怡'),('黃彥宜','黃彥怡'),('黃妍儀','黃彥怡')]:
    add(old, new, 'S01')
for old, new in [('開場生論','開場申論'),('聲論','申論'),('深論','申論'),('宣論','申論'),('交互接問','交互詰問'),('交叉接問','交叉詰問'),('交叉解問','交叉詰問')]:
    add(old, new, 'S01')
for old, new, source in [
    ('都市微生靈','都市微森林','S03'),('四萬里二期','斯文里二期','S02'),
    ('松基','松機','context'),('北市科','北士科','S09'),
    ('科技狼蛋','科技廊帶','context'),('AI 狼蛋','AI 廊帶','context'),
    ('黃金狼蛋','黃金廊帶','context'),('藝文狼蛋','藝文廊帶','context'),
    ('狼蛋','廊帶','context'),('廊袋','廊帶','context'),
    ('才化法','財劃法','S12'),('財化法','財劃法','S12'),
    ('好運專車','好孕專車','S11'),('ubike','YouBike','context'),
    ('耳虐','兒虐','context'),('肚根','都更','context'),
    ('零拖','臨托','context'),('領托','臨托','context'),('零托','臨托','context'),
    ('公管圓環','公館圓環','context'),('保齡茶室','寶林茶室','S05'),
    ('保齡跑不了','寶林跑不了','S05'),('清華國中','金華國中','context'),
    ('企業東數','茄苳樹','S04'),('茄東樹','茄苳樹','S04'),
    ('東門協同處','東門茄苳樹','S04'),('工研處','公園處','S04'),
    ('實驗性即便的檢驗組','食因性疾病的檢驗組','S10'),
    ('毒價','毒駕','S06'),('酒價','酒駕','S06'),('獨家酒駕','毒駕酒駕','S06'),
    ('下安站','廈安站','S07'),('達拉站','加蚋站','S07'),
    ('都更八件','都更八箭','S08'),('任性程式','韌性城市','context'),
    ('Alex Hanno','Alex Honnold','S15'),('五林街六十巷','虎林街六十巷','S16'),
    ('東京都知識小直百合子','東京都知事小池百合子','S17'),
    ('居住\n任性','居住\n韌性','context'),('權力轉換','權利轉換','context'),
    ('雙層論壇','雙城論壇','context'),('debug song','Debug 松','S13'),
    ('投降您神聖的一票','投下您神聖的一票','context'),
]:
    add(old, new, source)

def stamp(seconds):
    ms = round(seconds * 1000)
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f'{h:02}:{m:02}:{s:02},{ms:03}'

assert stamp(3661.234) == '01:01:01,234'
rows = [json.loads(s) for s in (p / 'segments.jsonl').read_text().splitlines()]
changes = []
corrected = []
timing_fixes = {1163:(5369.28,5378.88),1592:(6866.34,6873.94),2141:(8315.26,8316.78),3021:(11557.06,11560.98),3309:(12478.70,12482.58)}
timing_log = []
for number, row in enumerate(rows, 1):
    original = row['text'].strip()
    text = original
    for old, new, source in rules:
        if old in text:
            changes.append(dict(segment=number, start=row['start'], end=row['end'], old=old, new=new, source_id=source, source=sources[source], method='context_only' if source == 'context' else 'web_term_and_context'))
            text = text.replace(old, new)
    start, end = timing_fixes.get(number, (row['start'], row['end']))
    if number in timing_fixes:
        timing_log.append(dict(segment=number,old_start=row['start'],old_end=row['end'],new_start=start,new_end=end,evidence='timing_clips.jsonl',method='same_model_short_clip_word_timestamps',human_listening=False))
    corrected.append(dict(segment=number, start=start, end=end, text=text))
assert len(corrected) == len(rows) == 3328
assert all(a['start']==b['start'] and a['end']==b['end'] for n,(a,b) in enumerate(zip(rows,corrected),1) if n not in timing_fixes)
assert all(0<=r['start']<=r['end'] for r in corrected)
assert all(r['start']>=corrected[i-1]['end']-0.1 for i,r in enumerate(corrected) if i)
assert any('三規一章' in r['text'] for r in corrected), 'Preserve speaker wording; do not rewrite disputed claims.'
(p / 'segments_corrected.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in corrected))
(p / 'transcript_corrected.txt').write_text(''.join(r['text']+'\n' for r in corrected))
(p / 'transcript_corrected.srt').write_text(''.join(f"{r['segment']}\n{stamp(r['start'])} --> {stamp(r['end'])}\n{r['text']}\n\n" for r in corrected))
with (p / 'correction_log.csv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(changes[0]))
    writer.writeheader()
    writer.writerows(changes)
(p / 'correction_sources.json').write_text(json.dumps(sources, ensure_ascii=False, indent=2)+'\n')
(p / 'timing_corrections.json').write_text(json.dumps(timing_log,ensure_ascii=False,indent=2)+'\n')
(p / 'correction_receipt.json').write_text(json.dumps(dict(status='in_progress',segments=len(rows),changed_segments=len({c['segment'] for c in changes}),replacement_events=len(changes),full_audio_listening=False,web_fact_check='in_progress',original_preserved=True),ensure_ascii=False,indent=2)+'\n')
print(f'{len(corrected)} segments; {len(changes)} replacement events; verification in progress')
