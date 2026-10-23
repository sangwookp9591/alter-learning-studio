#!/usr/bin/env python3
"""Optional Chromium smoke test, requires Python Playwright + browser binary.

Uses set_content() to test the self-contained player without networking or file navigation.
Run: python3 scripts/smoke_browser.py --chromium /usr/bin/chromium
"""
import argparse
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def main():
    from playwright.sync_api import sync_playwright
    parser=argparse.ArgumentParser()
    parser.add_argument('--chromium',default=None)
    args=parser.parse_args()
    expected={
        'kubernetes-service.html':['400','33.3'],
        'cache-hit-rate.html':['800','200'],
        'probability-expected-value.html':['6.0','14.0']
    }
    with sync_playwright() as playwright:
        kw={'headless':True,'args':['--no-sandbox']}
        if args.chromium:kw['executable_path']=args.chromium
        browser=playwright.chromium.launch(**kw)
        for name,metrics in expected.items():
            content=(ROOT/'examples'/name).read_text(encoding='utf-8')
            page=browser.new_page(viewport={'width':1320,'height':960})
            errors=[]
            page.on('pageerror',lambda e:errors.append(str(e)))
            page.set_content(content,wait_until='load')
            assert page.locator('.node').count()>=4
            assert page.locator('.edge').count()>=3
            assert page.locator('.metric strong').all_inner_texts()==metrics,(name,page.locator('.metric strong').all_inner_texts())
            old=page.locator('#stepTitle').inner_text()
            page.locator('#next').click()
            assert page.locator('#stepTitle').inner_text()!=old
            page.locator('#timeline').fill('4000')
            assert '5 / 5'==page.locator('#counter').inner_text()
            page.locator('#play').click()
            assert page.locator('#play').get_attribute('aria-pressed')=='true'
            page.locator('#play').click()
            assert page.locator('#play').get_attribute('aria-pressed')=='false'
            # Continuous scrubbing must produce a meaningful frame, not just jump labels.
            page.locator('#timeline').fill('2500')
            assert page.locator('#counter').inner_text()=='3 / 5'
            assert page.locator('.beat.active').count()==1
            assert page.locator('.edge.active').count()>=1
            active=page.locator('.edge.active').first
            assert active.get_attribute('style') and 'stroke-dashoffset' in active.get_attribute('style')
            dash0=active.evaluate('(el)=>el.style.strokeDashoffset')
            page.locator('#timeline').fill('2850')
            dash1=active.evaluate('(el)=>el.style.strokeDashoffset')
            assert dash0 != dash1,(name,dash0,dash1)
            page.locator('#timeline').fill('2500')
            assert dash0 == active.evaluate('(el)=>el.style.strokeDashoffset'), 'scrub is nondeterministic'
            page.locator('.option').nth(1).click()
            assert '정답입니다.' in page.locator('#feedback').inner_text()
            page.set_viewport_size({'width':390,'height':844})
            assert page.locator('#stage').count()==1
            assert not errors,(name,errors)
            print('BROWSER PASS:',name)
            page.close()
        reduced=browser.new_context(reduced_motion='reduce')
        page=reduced.new_page()
        page.set_content((ROOT/'examples'/'kubernetes-service.html').read_text(encoding='utf-8'))
        assert page.locator('#stepTitle').inner_text()
        assert page.locator('.flow-dot').count()==0
        print('BROWSER PASS: reduced motion')
        reduced.close();browser.close()

if __name__=='__main__':main()
