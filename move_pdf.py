import os, shutil, glob

src_fldr = '/storage/emulated/0/Download'; ## Edit this

dst_fldr = '/storage/emulated/0/Documents'; ## Edit this

#try:
#  os.makedirs(dst_fldr); ## it creates the destination folder
#except:
#  print "Folder already exist or some error";
  
for pdf_file in glob.glob(src_fldr+"/*.pdf"):
  shutil.move(pdf_file, dst_fldr);