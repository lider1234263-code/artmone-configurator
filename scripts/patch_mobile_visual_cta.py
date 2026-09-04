from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

css = r'''
/* MOBILE_VISUAL_CTA */
.mobile-visual-cta{display:none}
.mobile-visual-return{display:none}
@media(max-width:900px){
  .mobile-visual-cta{display:block;margin:6px 0;border:1px solid #e7e0d6;background:#fbfaf7;border-radius:12px;padding:10px 12px;cursor:pointer}
  .mobile-visual-cta-inner{display:flex;align-items:center;gap:10px}
  .mobile-visual-cta-icon{width:30px;height:30px;flex:0 0 30px;border-radius:50%;background:#f5f2ed;border:1px solid #e6dfd6;display:grid;place-items:center;color:#4e4a45}
  .mobile-visual-cta-icon svg{width:17px;height:17px;display:block;stroke:currentColor;stroke-width:1.8;fill:none;stroke-linecap:round;stroke-linejoin:round}
  .mobile-visual-cta-copy{min-width:0;flex:1}
  .mobile-visual-cta-title{font-weight:750;font-size:13px;line-height:1.18;margin-bottom:2px}
  .mobile-visual-cta-text{font-size:10.5px;line-height:1.28;color:var(--muted)}
  .mobile-visual-cta-link{display:inline-block;margin-top:4px;font-size:10.5px;font-weight:700;text-decoration:underline;text-underline-offset:2px;color:var(--text)}
  .mobile-visual-cta-arrow{font-size:16px;line-height:1;color:#77716a}
  .mobile-visual-return.visible{display:flex;align-items:center;justify-content:center;margin:-8px 36px 10px auto;width:38px;height:38px;border-radius:50%;border:1px solid #ded8cf;background:#fff;color:#292725;box-shadow:0 3px 12px rgba(0,0,0,.06);cursor:pointer;position:relative;z-index:4}
  .mobile-visual-return svg{width:18px;height:18px;stroke:currentColor;stroke-width:1.9;fill:none;stroke-linecap:round;stroke-linejoin:round}
}
'''
css_pattern = re.compile(r'/\* MOBILE_VISUAL_CTA \*/.*?(?=</style>)', re.S)
if css_pattern.search(s):
    s = css_pattern.sub(css + '\n', s, count=1)
else:
    s = s.replace('</style>', css + '\n</style>', 1)

js = r'''
/* MOBILE_VISUAL_CTA_JS */
(function(){
  const oldCard=document.getElementById('mobileVisualCta');
  if(oldCard) oldCard.remove();
  const oldReturn=document.getElementById('mobileVisualReturn');
  if(oldReturn) oldReturn.remove();

  const printsEl=document.getElementById('prints');
  if(!printsEl) return;
  const printPanel=printsEl.closest('.panel');
  if(!printPanel) return;

  const card=document.createElement('div');
  card.id='mobileVisualCta';
  card.className='mobile-visual-cta';
  card.setAttribute('role','button');
  card.setAttribute('tabindex','0');
  card.innerHTML='<div class="mobile-visual-cta-inner"><div class="mobile-visual-cta-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M2.5 12s3.5-6 9.5-6 9.5 6 9.5 6-3.5 6-9.5 6-9.5-6-9.5-6Z"></path><circle cx="12" cy="12" r="2.8"></circle></svg></div><div class="mobile-visual-cta-copy"><div class="mobile-visual-cta-title">Побачити вашу комбінацію</div><div class="mobile-visual-cta-text">Стрічка + колір друку вже показані на фото</div><div class="mobile-visual-cta-link">Переглянути візуалізацію ↑</div></div><div class="mobile-visual-cta-arrow">↑</div></div>';
  printPanel.insertAdjacentElement('afterend',card);

  const thumbs=document.getElementById('galleryThumbs');
  const returnBtn=document.createElement('button');
  returnBtn.id='mobileVisualReturn';
  returnBtn.type='button';
  returnBtn.className='mobile-visual-return';
  returnBtn.setAttribute('aria-label','Повернутися до налаштування');
  returnBtn.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"></path></svg>';
  if(thumbs) thumbs.insertAdjacentElement('afterend',returnBtn);

  const goUp=()=>{
    const gallery=document.querySelector('.photo-gallery');
    if(!gallery) return;
    returnBtn.classList.add('visible');
    gallery.scrollIntoView({behavior:'smooth',block:'start'});
  };
  const goBack=()=>{
    card.scrollIntoView({behavior:'smooth',block:'center'});
    returnBtn.classList.remove('visible');
  };

  card.addEventListener('click',goUp);
  card.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();goUp();}});
  returnBtn.addEventListener('click',goBack);
})();
'''
js_pattern = re.compile(r'/\* MOBILE_VISUAL_CTA_JS \*/.*?(?=</script>)', re.S)
if js_pattern.search(s):
    s = js_pattern.sub(js + '\n', s, count=1)
else:
    pos = s.rfind('</script>')
    if pos < 0:
        raise SystemExit('No script closing tag found')
    s = s[:pos] + js + '\n' + s[pos:]

p.write_text(s, encoding='utf-8')
print('refined mobile visualization CTA with return button')
