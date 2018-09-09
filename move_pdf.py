#Moves pdf files from a source folder to a destination folder

import os, shutil, glob

src_fldr = '/storage/emulated/0/Download'; ## Edit this

dst_fldr = '/storage/emulated/0/Documents'; ## Edit this
  
for pdf_file in glob.glob(src_fldr+"/*.pdf"):
  shutil.move(pdf_file, dst_fldr);