import os
import subprocess

import pypandoc
from pypandoc.pandoc_download import download_pandoc

download_pandoc()


def html2rst(html):
  p = subprocess.Popen(
    ['pandoc', '--from=html', '--to=rst'],
    stdin=subprocess.PIPE, stdout=subprocess.PIPE
  )
  return p.communicate(html)[0]

HTMLS_PATH = './html'
OUTPUT_PATH = './source/html'

files = []
for filename in os.listdir(HTMLS_PATH):
  if filename.endswith('.html'):
    files.append(filename)

print('\nStarting conversion...')

for file in files:
  print(f'Processing {file}')

  in_path = os.path.join(HTMLS_PATH, file)
  out_name =  os.path.basename(file).replace('.html', '.rst')
  out_path = os.path.join(OUTPUT_PATH, out_name)

  rst = pypandoc.convert_file(in_path, 'rst', outputfile=out_path)

print(f'\nDone. {len(files)} files converted')
