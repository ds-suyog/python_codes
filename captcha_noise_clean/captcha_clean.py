import sys
from PIL import Image

#imgFile = "c1a.png"
imgFile = sys.argv[1]   # type 'str'
im = Image.open(imgFile, 'r')
#print im.size
pix_val_list = list(im.getdata()) # list of tuples
pix_val2 = pix_val_list[:]
# import pdb; pdb.set_trace()

def find_pixel_stats(pix_val_list):
	distinct_tuples = []
	stat_distinct_tuples = dict()  #{'tup': count }
	# print("pix val list = {}".format(len(pix_val_list)))

	total_pixels = len(pix_val_list)
	print("total_pixes = {}".format(total_pixels))

	for tupl in pix_val_list:
		if tupl not in distinct_tuples:
			distinct_tuples.append(tupl)
			stat_distinct_tuples[tupl] = 1

		if tupl in distinct_tuples:
			stat_distinct_tuples[tupl] = stat_distinct_tuples[tupl] + 1

	print("\ndistinct_tuples = {}".format(distinct_tuples))
	print("\nstats distinct_tuples = {}".format(stat_distinct_tuples))

	hex_stats = dict()
	for k,v in stat_distinct_tuples.items():
		hex_val = '0x'
		for val in k:
			hex_val = hex_val + hex(val)[2:]
		hex_stats[hex_val] = v

	# print("\nhex_stats = {}".format(hex_stats))

	import operator
	# x = {'a': 2, 'b': 4, 'c': 3, 'd': 1, 'e': 0}
	x = hex_stats
	sorted_x = sorted(x.items(), reverse = True, key=operator.itemgetter(1))
	# print("sorted_x = {}".format(sorted_x))

	# for tup in sorted_x:
	# 	print("{}: {}:  {}%".format(tup[0], tup[1], round(tup[1]/total_pixels,5)))

	text_n_noise = sorted_x[0:3]
	print("\ntop 3 pixels by freq in hex= {}".format(text_n_noise))
	pixel_tups_list = []
	for k,v in text_n_noise:
		col_1_hex = '0x' + k[2:4]
		col_1_int = int(col_1_hex, 16)
		col_2_hex = '0x' + k[4:6]
		col_2_int = int(col_2_hex, 16)
		col_3_hex = '0x' + k[6:]
		col_3_int = int(col_3_hex, 16)
		# tup = tuple((col_1, col_2, col_3))
		tup = tuple((col_1_int, col_2_int, col_3_int))		
		pixel_tups_list.append(tup)
	print("top 3 pixels freq in decimal = {}".format(pixel_tups_list))

	pix_val_list_edited = pix_val_list.copy()

	count = 0
	for i,v in enumerate(pix_val_list_edited):
	   if v not in pixel_tups_list:
	     pix_val_list_edited[i]=(255,255,255)
	     count += 1
	     # print("count = {}".format(count))


	distinct_tuples2 = []
	stat_distinct_tuples2 = dict()  #{'tup': count }

	for tupl in pix_val_list_edited:
		if tupl not in distinct_tuples2:
			distinct_tuples2.append(tupl)
			stat_distinct_tuples2[tupl] = 1

		if tupl in distinct_tuples:
			stat_distinct_tuples2[tupl] = stat_distinct_tuples2[tupl] + 1
	# white pixels before 14016, add 479 , new count = 14495
	print("\ndistinct_tuples2 = {}".format(distinct_tuples2))
	print("\nstats distinct_tuples2 = {}".format(stat_distinct_tuples2))

	# im2 = Image.new(im.mode, im.size)
	# im2.putdata(pix_val_list_edited)
	# im2.show()


find_pixel_stats(pix_val_list)

# for i in range(0,len(pix_val2)):
#   if sum(pix_val2[i]) >=300:
#     pix_val2[i] = (255,255,255)

# im2 = Image.new(im.mode, im.size)
# im2.putdata(pix_val2)
# im2.show()

# im2.save(imgFile.split(".")[0] + "_cleaned.png","PNG")

