from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

css_marker = '/* MOBILE_VISUAL_CTA */'
css = r'''
/* MOBILE_VISUAL_CTA */
.mobile-visual-cta{display:none}
@media(max-width:900px){
  .mobile-visual-cta{display:block;margin:8px 0;border:1px solid #e7d2ad;background:#f7efe2;border-radius:14px;padding:14px 15px;cursor:pointer}
  .mobile-visual-cta-inner{display:flex;align-items:center;gap:12px}
  .mobile-visual-cta-icon{width:38px;height:38px;flex:0 0 38px;border-radius:50%;background:#fff;border:1px solid #e3d7c4;display:grid;place-items:center;font-size:18px}
  .mobile-visual-cta-copy{min-width:0;flex:1}
  .mobile-visual-cta-title{font-weight:800;font-size:14px;line-height:1.2;margin-bottom:4px}
  .mobile-visual-cta-text{font-size:11px;line-height:1.35;color:var(--muted)}
  .mobile-visual-cta-link{display:inline-block;margin-top:6px;font-size:11px;font-weight:800;text-decoration:underline;color:var(--text)}
  .mobile-visual-cta-arrow{font-size:20px;line-height:1}
}
'''
if css_marker not in s:
    s = s.replace('</style>', css + '\n</style>', 1)

js_marker = '/* MOBILE_VISUAL_CTA_JS */'
js = r'''
/* MOBILE_VISUAL_CTA_JS */
(function(){
  if(document.getElementById('mobileVisualCta')) return;
  const printsEl=document.getElementById('prints');
  if(!printsEl) return;
  const printPanel=printsEl.closest('.panel');
  if(!printPanel) return;
  const card=document.createElement('div');
  card.id='mobileVisualCta';
  card.className='mobile-visual-cta';
  card.setAttribute('role','button');
  card.setAttribute('tabindex','0');
  card.innerHTML='<div class="mobile-visual-cta-inner"><div class="mobile-visual-cta-icon">◉</div><div class="mobile-visual-cta-copy"><div class="mobile-visual-cta-title">Побачити вашу комбінацію</div><div class="mobile-visual-cta-text">Стрічка + колір друку вже показані на фото</div><div class="mobile-visual-cta-link">Переглянути візуалізацію ↑</div></div><div class="mobile-visual-cta-arrow">↑</div></div>';
  printPanel.insertAdjacentElement('afterend',card);
  const go=()=>{
    const gallery=document.querySelector('.photo-gallery');
    if(!gallery) return;
    gallery.scrollIntoView({behavior:'smooth',block:'start'});
  };
  card.addEventListener('click',go);
  card.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();go();}});
})();
'''
if js_marker not in s:
    pos = s.rfind('</script>')
    if pos < 0:
        raise SystemExit('No script closing tag found')
    s = s[:pos] + js + '\n' + s[pos:]

p.write_text(s, encoding='utf-8')
print('patched mobile visualization CTA')
