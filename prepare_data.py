"""Reproduce Assignment 5 data with Python 3 standard library only.
Run from this file's folder: python prepare_data.py
Source snapshot: NYC Open Data wyih-3nzf, retrieved September 23, 2026.
"""
import json,csv,datetime,calendar
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parent
raw=json.loads((ROOT/'data/raw-snapshot.json').read_text())
fields=['the_geom','oftcode','geoborough','onstreetna','fromstreet','tostreetna','dateprotec','dateprot_1','shape_stle']
missing={k:sum(k not in r or r[k] is None or r[k]=='' for r in raw) for k in fields}
seen=set();clean=[]
for row in raw:
 key=json.dumps(row,sort_keys=True)
 if key not in seen:seen.add(key);clean.append(dict(row))
names={'M':'Manhattan','X':'Bronx','B':'Brooklyn','Q':'Queens','S':'Staten Island'}
reference=datetime.date(2026,9,23);cutoff=datetime.date(2027,9,23)
records=[];export=[];expired=0;future=0;invalid=0;anniversaries=0
for row in clean:
 for k in ['geoborough','onstreetna','fromstreet','tostreetna']:row[k]=row[k].strip().upper()
 try:start=datetime.date.fromisoformat(row['dateprotec'][:10]);end=datetime.date.fromisoformat(row['dateprot_1'][:10])
 except (ValueError,KeyError):invalid+=1;continue
 if end<start or row['geoborough'] not in names:invalid+=1;continue
 anniversary=start.replace(year=start.year+5,day=min(start.day,calendar.monthrange(start.year+5,start.month)[1]));anniversaries+=end==anniversary
 status='expired' if end<reference else 'future' if start>reference else 'active'
 expired+=status=='expired';future+=status=='future'
 export.append({**row,'the_geom':json.dumps(row['the_geom'],separators=(',',':')),'borough':names[row['geoborough']],'status':status,'duration_days':(end-start).days})
 if status!='active':continue
 records.append({'id':len(records),'borough':row['geoborough'],'street':row['onstreetna'],'from':row['fromstreet'],'to':row['tostreetna'],'start':str(start),'end':str(end),'oft':row['oftcode'],'lines':[[[round(x,6),round(y,6)] for x,y,*_ in line] for line in row['the_geom']['coordinates']]})
counts=Counter(r['borough'] for r in records);soon=Counter(r['borough'] for r in records if r['end']<=str(cutoff))
audit={'source':'https://data.cityofnewyork.us/Transportation/Protected-Streets-Block-Dataset-/wyih-3nzf','retrieved':'2026-09-23','source_last_updated':'2026-09-21','reference_date':str(reference),'raw_rows':len(raw),'original_fields':len(fields),'exact_duplicates_removed':len(raw)-len(clean),'deduplicated_rows':len(clean),'missing_by_field':missing,'expired_excluded':expired,'future_excluded':future,'invalid_excluded':invalid,'active_rows':len(records),'unique_oft_codes_after_dedup':len({r['oftcode'] for r in clean}),'five_calendar_year_matches':anniversaries,'borough_counts':dict(counts),'expiring_by_2027_09_23':dict(soon),'geometry_note':'Coordinates rounded to six decimal places for display only. Original coordinates remain in raw snapshot and cleaned CSV. Length field not converted or analyzed.'}
(ROOT/'data/streets.json').write_text(json.dumps({'audit':audit,'records':records},separators=(',',':')))
(ROOT/'data/cleaning-audit.json').write_text(json.dumps(audit,indent=2))
with (ROOT/'data/cleaned-records.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(export[0]));w.writeheader();w.writerows(export)
print(json.dumps(audit,indent=2))
assert len(raw)==24435 and len(clean)==24434 and len(records)==24404
assert sum(soon.values())==5014 and all(v==0 for v in missing.values()) and invalid==0
