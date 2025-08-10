#!/usr/bin/env python3
import re, sys, pathlib

def minify_css(code):
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.S)
    code = re.sub(r'\s+', ' ', code)
    code = re.sub(r'\s*([{};:,])\s*', r'\1', code)
    return code.strip()

def minify_js(code):
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.S)
    code = re.sub(r'(?<!:)//.*', '', code)
    code = re.sub(r'\s+', ' ', code)
    code = re.sub(r'\s*([{};:,()\[\]=+\-*/<>])\s*', r'\1', code)
    return code.strip()

def process_file(path):
    code = path.read_text()
    if path.suffix == '.css':
        minified = minify_css(code)
        out = path.with_suffix('.min.css')
    elif path.suffix == '.js':
        minified = minify_js(code)
        out = path.with_suffix('.min.js')
    else:
        return
    out.write_text(minified)

if __name__ == '__main__':
    for fname in sys.argv[1:]:
        process_file(pathlib.Path(fname))
