import os
import subprocess

import pypandoc
from pypandoc.pandoc_download import download_pandoc

download_pandoc()

HTMLS_PATH = './html'
OUTPUT_PATH = './source'

if not os.path.exists(OUTPUT_PATH):
  os.makedirs(OUTPUT_PATH)

files = []
for filename in os.listdir(HTMLS_PATH):
  if filename.endswith('.html'):
    files.append(filename)

print('\nStarting conversion...')

files_processed = 0
for file in files:
  print(f'Processing {file}')

  in_path = os.path.join(HTMLS_PATH, file)
  out_name =  os.path.basename(file).replace('.html', '.rst')
  out_path = os.path.join(OUTPUT_PATH, out_name)

  rst = pypandoc.convert_file(in_path, 'rst', outputfile=out_path)
  files_processed += 1

print(f'\nDone. {files_processed} files converted')
