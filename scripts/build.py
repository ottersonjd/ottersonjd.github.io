"""Build a portable static portfolio using only Python's standard library."""
from pathlib import Path
from urllib.parse import urlparse
from html import escape
import json, shutil, re
ROOT=Path(__file__).resolve().parent.parent
projects=json.loads((ROOT/'projects.json').read_text())
def text(p,key):return escape(str(p.get(key,'')))
def attachments(p):
 links=[]
 if p.get('colab'):
  u=urlparse(p['colab'])
  if u.scheme!='https' or u.hostname!='colab.research.google.com':raise ValueError('Use a valid HTTPS Colab link.')
  links.append(f'<a href="{escape(p["colab"],quote=True)}" target="_blank" rel="noopener noreferrer">Open in Colab</a>')
 if p.get('notebookPath'):
  path=p['notebookPath']
  if not re.fullmatch(r'\./notebooks/[A-Za-z0-9._-]+\.ipynb',path):raise ValueError('Notebook path must be ./notebooks/name.ipynb')
  f=ROOT/path
  n=json.loads(f.read_text())
  if n.get('nbformat')!=4 or not isinstance(n.get('cells'),list):raise ValueError('Invalid notebook')
  links.append(f'<a href="{escape(path,quote=True)}" download>Download notebook</a>')
 return '<div class="attachments">'+''.join(links)+'</div>' if links else ''
cards=[];seen=set()
for i,p in enumerate(projects):
 if not re.fullmatch('[a-z0-9-]+',p['id']) or p['id'] in seen:raise ValueError('Project IDs must be unique URL-safe names.')
 seen.add(p['id'])
 sections=''.join(f'<div class="case-section"><h4>{h}</h4><p>{text(p,k)}</p></div>' for h,k in [('Business question','question'),('Approach','approach'),('Key finding','finding'),('Recommendation','recommendation'),('Scope & limitations','limitation')] if p.get(k))
 metric=f'<div class="metric">{text(p,"metric")}<span>{text(p,"metricLabel")}</span></div>' if p.get('metric') else ''
 cards.append(f'''<article id="{p['id']}" class="card {'blue' if i%2 else ''}" data-category="{text(p,'category')}"><p class="eyebrow">{text(p,'category')}</p><h3>{text(p,'title')}</h3><p class="context">{text(p,'company')} · {text(p,'year')}<br><span>{text(p,'label')}</span></p>{metric}<p>{text(p,'finding')}</p><p class="skill-list">{text(p,'tools')}</p><details class="case-study"><summary>Read case study</summary>{sections}</details>{attachments(p)}</article>''')
categories=['All']+list(dict.fromkeys(p['category'] for p in projects))
filters=''.join(f'<button type="button" data-filter="{escape(c,quote=True)}" aria-pressed="{str(c=="All").lower()}" class="{"active" if c=="All" else ""}">{escape(c)}</button>' for c in categories)
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Justin Otterson’s business analytics and strategy portfolio: sustainability, consumer insights, social impact, and investment research."><meta name="theme-color" content="#101f38"><title>Justin Otterson | Business Analytics & Strategy</title><link rel="icon" href="./favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="./styles.css"><script src="./site.js" defer></script></head><body><a class="skip-link" href="#work">Skip to selected work</a>'''
page+=(ROOT/'scripts/header.html').read_text()
page+=f'<section id="work"><div class="section-heading"><div><p class="eyebrow">SELECTED WORK / 01</p><h2>Analysis with a business purpose.</h2></div></div><div class="filters" aria-label="Filter projects" hidden>{filters}</div><p id="filter-status" class="filter-status" aria-live="polite" hidden></p><div class="cards">'+''.join(cards)+'</div></section>'
page+=(ROOT/'scripts/about.html').read_text()
page+='<footer><span>Justin Otterson · Los Angeles</span><a href="#work">Back to selected work ↑</a></footer></body></html>'
(ROOT/'index.html').write_text(page)
out=ROOT/'_site'
if out.exists():shutil.rmtree(out)
out.mkdir()
for name in ['index.html','styles.css','site.js','favicon.svg']:
 if (ROOT/name).exists():shutil.copy2(ROOT/name,out/name)
shutil.copytree(ROOT/'notebooks',out/'notebooks')
(out/'.nojekyll').touch()
print(f'Built {len(projects)} project case studies and {len(list((out/"notebooks").glob("*.ipynb")))} notebooks.')
