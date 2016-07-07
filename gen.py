#!/usr/bin/env python
################### gen.py #################
# Filename:     gen.py
# Version :     1.0
# Date :        Jul 3rd 2016
# Author  :     Rick Rune (rick at runeg dot net)
# Help :        rick at runeg dot net
# Licence :     GPL - http://www.fsf.org/licenses/gpl.txt
# TODO :        
# Changelog:
# Requires:     Requires Python Imaging Library, 
#				BlueImp's bootstrap: https://blueimp.github.io/Bootstrap-Image-Gallery/
# Notes:       
################################################################
def main():
	from os import listdir, mkdir
	from os.path import isfile, join, exists
	from Image import open as Image_open

	subject = "fireworks"
	base = "/var/www/html/pg/"
	begin = base + "gen/begin.html"
	end = base + "gen/end.html"

	subject_base = base + subject + "/"
	img_dir = base + "images/%s/" % subject
	th_dir = base + "images/th/%s/" % subject
	new_index = base + subject + ".html" 

	html_images_path = "./images/%s/" % subject
	html_th_images_path = "./images/th/%s/" % subject

	size = (102, 76)

	with open(begin) as f:
	    begin_html = f.read()

	with open(end) as f:
	    end_html = f.read()

	# Working with files only.
	images = [f for f in listdir(img_dir) if isfile(join(img_dir, f))]

	img_html = ""

	if not exists(th_dir):
		mkdir(th_dir)

	for filename in images:
		#Generate thumbnail
		infile = img_dir + filename
		outfile = th_dir + "th_" + filename
		im = Image_open(infile)
		im.thumbnail(size)
		im.save(outfile, "JPEG")

		# Generate image html
        img_html += """
		    <a href="%s%s" title="%s" data-gallery>
		        <img src="%s%s" width=102 height=76 alt="%s">
		    </a>
		""" % (html_images_path, filename, filename, html_th_images_path, filename, filename)

	f = open(new_index, "w")
	# Delete previous index.html
	f.seek(0)
	f.truncate()

	f.write(begin_html)
	f.write(img_html)
	f.write(end_html)
	f.close()

if __name__ == '__main__':
	main()