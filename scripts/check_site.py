"""Validate the static site's routes, metadata, assets, and version contract."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import re

ROOT = Path(__file__).resolve().parents[1]

class Document(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.links, self.ids = path, [], set()
        self.language = self.title = self.description = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'Duplicate ID: {self.path}'
            self.ids.add(attrs['id'])
        if tag == 'html':
            self.language = attrs.get('lang') in ('en', 'zh-Hans')
        if tag == 'title':
            self.title = True
        if tag == 'meta' and attrs.get('name') == 'description':
            self.description = bool(attrs.get('content'))
        for attr in ('href', 'src'):
            if attr in attrs:
                url = urlsplit(attrs[attr])
                assert not url.scheme and not url.netloc, f'External URL: {self.path}'
                self.links.append(url)

pages = {}
for path in ROOT.rglob('*.html'):
    doc = Document(path)
    doc.feed(path.read_text(encoding='utf-8'))
    assert doc.language and doc.title and doc.description, f'Metadata: {path}'
    pages[path.resolve()] = doc
assert len(pages) == 5, 'Expected five public pages'
for path, doc in pages.items():
    for url in doc.links:
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        assert target.is_relative_to(ROOT), f'Link escapes site: {path}'
        if target.is_dir():
            target /= 'index.html'
        assert target.is_file(), f'Broken link: {path} -> {target}'
        if url.fragment:
            assert target in pages and url.fragment in pages[target].ids, f'Broken fragment: {path}'
assert 'href="zh/"' in (ROOT/'privacy/index.html').read_text()
assert 'href="../" lang="en"' in (ROOT/'privacy/zh/index.html').read_text()
css = (ROOT/'assets/css/style.css').read_text()
assert '@import' not in css and 'url(' not in css, 'External CSS dependency requires review'
for platform in ('ios', 'android'):
    data = json.loads((ROOT/f'config/v1/{platform}.json').read_text())
    assert type(data['schemaVersion']) is int and data['schemaVersion'] == 1
    for field in ('latestVersion', 'minimumSupportedVersion', 'updateMessage', 'storeUrl'):
        assert isinstance(data[field], str), f'{platform}: {field}'
    versions = []
    for field in ('latestVersion', 'minimumSupportedVersion'):
        assert re.fullmatch(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)', data[field])
        versions.append(tuple(map(int, data[field].split('.'))))
    assert versions[1] <= versions[0], 'Minimum version exceeds latest'
    assert isinstance(data['features'], dict)
    for feature in ('wordAssociation', 'imageGeneration'):
        assert type(data['features'][feature]) is bool
    store = urlsplit(data['storeUrl'])
    assert not data['storeUrl'] or (store.scheme == 'https' and store.hostname)
print(f'PASS: {len(pages)} HTML pages, internal links/fragments, bilingual links, local CSS, and 2 version configurations')
