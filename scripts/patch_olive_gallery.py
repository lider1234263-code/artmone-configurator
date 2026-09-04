from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

# New storage namespace so old test value (e.g. 500 m) does not override the 100 m default.
s=s.replace('const CONFIG_STORAGE_KEY="artmone_satin_config_v1";', 'const CONFIG_STORAGE_KEY="artmone_satin_config_v2";')

css='''
/* ALL_RIBBONS_11_CARD_GALLERY */
#galleryThumbs.gallery-11{grid-template-columns:repeat(6,1fr)}
#galleryThumbs.gallery-11 .thumb{position:relative;display:grid;place-items:center;background:#f4f1eb;border:1px solid var(--line);overflow:hidden}
#galleryThumbs.gallery-11 .thumb .gallery-placeholder{display:grid;place-items:center;width:100%;height:100%;font:700 10px "DM Sans",sans-serif;color:#8b847b;background:linear-gradient(145deg,#f7f4ef,#ebe5dc)}
#galleryThumbs.gallery-11 .thumb img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
#galleryThumbs.gallery-11 .thumb.active{outline:2px solid #171717;outline-offset:-2px}
.gallery-expand{position:absolute;right:16px;top:16px;z-index:12;width:42px;height:42px;border:1px solid rgba(255,255,255,.65);border-radius:50%;background:rgba(255,255,255,.9);color:#171717;font-size:25px;line-height:1;display:grid;place-items:center;box-shadow:0 5px 18px rgba(0,0,0,.12);cursor:pointer}
.gallery-main-placeholder{position:absolute;inset:0;display:grid;place-items:center;text-align:center;padding:30px;color:#777068;background:linear-gradient(145deg,#f3eee7,#e5dacf);font:600 14px/1.5 "DM Sans",sans-serif}
.gallery-lightbox{position:fixed;inset:0;z-index:5000;display:none;align-items:center;justify-content:center;padding:22px;background:rgba(15,14,13,.92)}
.gallery-lightbox.open{display:flex}
.gallery-lightbox img{max-width:96vw;max-height:92vh;object-fit:contain;border-radius:8px}
.gallery-lightbox .lightbox-placeholder{display:grid;place-items:center;width:min(900px,92vw);aspect-ratio:1;background:#eee8df;border-radius:12px;color:#6f6962;font:700 18px "DM Sans",sans-serif}
.gallery-lightbox-close{position:fixed;right:20px;top:20px;width:44px;height:44px;border:0;border-radius:50%;background:#fff;color:#111;font-size:28px;cursor:pointer}
@media(max-width:900px){#galleryThumbs.gallery-11{grid-template-columns:repeat(6,1fr);gap:5px}.gallery-expand{right:12px;top:12px;width:38px;height:38px;font-size:22px}}
'''

# Replace prior AM567-only gallery CSS if present; otherwise append.
pat_css=re.compile(r'/\* AM567 11-card studio gallery \*/.*?(?=</style>)',re.S)
if pat_css.search(s):
    s=pat_css.sub(css+'\n',s,count=1)
elif '/* ALL_RIBBONS_11_CARD_GALLERY */' not in s:
    s=s.replace('</style>',css+'\n</style>',1)

js='''
/* ALL_RIBBONS_GALLERY_11_JS */
(function(){
  const galleryItems=[
    ['recolor_01.webp','Фото 01'],['recolor_02.webp','Фото 02'],['recolor_03.webp','Фото 03'],['recolor_04.webp','Фото 04'],
    ['recolor_05.webp','Фото 05'],['recolor_06.webp','Фото 06'],['recolor_07.webp','Фото 07'],['studio_01.webp','Studio 01'],
    ['studio_02.webp','Studio 02'],['studio_03.webp','Studio 03'],['studio_white_bg_01.webp','White BG']
  ];
  let galleryIndex=0;
  const thumbs=document.getElementById('galleryThumbs');
  const visual=document.querySelector('.photo-gallery');

  function folderFor(code){
    return 'am-'+String(code||'').replace(/^AM\s*/i,'').trim().toLowerCase().replace(/\s+/g,'-');
  }
  function pathFor(i){
    const r=ribbons[colorIndex];
    return 'assets/mockups/'+folderFor(r&&r.code)+'/'+galleryItems[i][0];
  }
  function currentRibbon(){return ribbons[colorIndex]||{};}

  if(visual && !document.getElementById('galleryExpand')){
    const b=document.createElement('button');
    b.id='galleryExpand'; b.type='button'; b.className='gallery-expand';
    b.setAttribute('aria-label','Розгорнути фото'); b.textContent='+';
    visual.appendChild(b);
  }
  if(!document.getElementById('galleryLightbox')){
    const lb=document.createElement('div');
    lb.id='galleryLightbox'; lb.className='gallery-lightbox';
    lb.innerHTML='<button class="gallery-lightbox-close" type="button" aria-label="Закрити">×</button><img alt="Фото стрічки"><div class="lightbox-placeholder" style="display:none">Фото буде додано</div>';
    document.body.appendChild(lb);
    lb.querySelector('.gallery-lightbox-close').onclick=()=>lb.classList.remove('open');
    lb.addEventListener('click',e=>{if(e.target===lb)lb.classList.remove('open')});
  }

  function renderThumbs(){
    if(!thumbs)return;
    thumbs.className='thumbs gallery-11';
    thumbs.innerHTML=galleryItems.map((it,i)=>'<button class="thumb '+(i===galleryIndex?'active':'')+'" type="button" data-gallery-index="'+i+'" title="'+it[1]+'"><span class="gallery-placeholder">'+String(i+1).padStart(2,'0')+'</span><img src="'+pathFor(i)+'" alt="'+it[1]+'" onerror="this.style.display=\\'none\\'" onload="this.style.display=\\'block\\'"></button>').join('');
  }

  function showMainFallback(){
    if(!visual)return;
    let el=document.getElementById('galleryMainFallback');
    if(!el){
      el=document.createElement('div'); el.id='galleryMainFallback'; el.className='gallery-main-placeholder';
      visual.insertBefore(el,visual.firstChild);
    }
    const r=currentRibbon();
    el.innerHTML='<div><b>Фото '+String(galleryIndex+1).padStart(2,'0')+'</b><br>'+((r.name||'Стрічка')+' · '+(r.code||''))+'<br>Місце для фінального студійного фото</div>';
    el.style.display='grid';
  }
  function removeMainFallback(){const el=document.getElementById('galleryMainFallback');if(el)el.style.display='none'}

  function renderMain(){
    if(!visual)return;
    const placeholder=document.getElementById('mockupPlaceholder');
    const mockupMain=document.getElementById('mockupMain');
    const warehouseMain=document.getElementById('warehouseMain');
    if(warehouseMain)warehouseMain.style.display='none';
    if(placeholder)placeholder.style.display='none';
    if(mockupMain){
      mockupMain.style.display='block'; mockupMain.src=pathFor(galleryIndex); mockupMain.alt=galleryItems[galleryIndex][1];
      mockupMain.onerror=function(){this.style.display='none';showMainFallback()};
      mockupMain.onload=function(){removeMainFallback();this.style.display='block'};
    }
  }

  function renderGallery11(){
    renderThumbs(); renderMain();
    const r=currentRibbon(); const meta=document.getElementById('visMeta');
    if(meta)meta.textContent=(r.name||'Стрічка')+' · '+(r.code||'')+' · фото '+(galleryIndex+1)+' з 11';
  }

  if(thumbs)thumbs.addEventListener('click',e=>{
    const btn=e.target.closest('[data-gallery-index]'); if(!btn)return;
    galleryIndex=Number(btn.dataset.galleryIndex)||0; renderGallery11();
  });

  const expand=document.getElementById('galleryExpand');
  if(expand)expand.addEventListener('click',()=>{
    const lb=document.getElementById('galleryLightbox'); if(!lb)return;
    const img=lb.querySelector('img'), ph=lb.querySelector('.lightbox-placeholder');
    img.style.display='block'; ph.style.display='none'; img.src=pathFor(galleryIndex);
    img.onerror=()=>{img.style.display='none';ph.style.display='grid';ph.textContent='Фото '+String(galleryIndex+1).padStart(2,'0')+' буде додано'};
    lb.classList.add('open');
  });

  window.updateGallery=renderGallery11;
  renderGallery11();
})();
'''

# Replace old AM567-only injected JS block, which sits immediately before the final </script>.
old_marker='/* AM567_GALLERY_11_JS */'
new_marker='/* ALL_RIBBONS_GALLERY_11_JS */'
if old_marker in s:
    start=s.index(old_marker)
    end=s.rfind('</script>')
    s=s[:start]+js+'\n'+s[end:]
elif new_marker not in s:
    end=s.rfind('</script>')
    if end<0: raise SystemExit('No script closing tag found')
    s=s[:end]+js+'\n'+s[end:]

p.write_text(s,encoding='utf-8')
print('patched all ribbons gallery + default 100 m namespace')
