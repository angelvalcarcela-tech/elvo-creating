from playwright.sync_api import sync_playwright
from pathlib import Path
D=Path('/home/user/elvo-creating/brands/elvo/web/galeria-alivio')
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    pg=b.new_page(viewport={'width':1200,'height':1200})
    for i in range(1,14):
        pg.goto(f'file://{D}/s{i}.html',wait_until='networkidle'); pg.wait_for_timeout(500)
        pg.screenshot(path=str(D/f'alivio-{i:02d}.png'))
    b.close()
