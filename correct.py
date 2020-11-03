#!/bin/python3
input_seqs = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']
for_range = list(range(0,len(input_seqs)))
for Xaxis_item in for_range:
	first_query = list(input_seqs[Xaxis_item])
	for Yaxis_item in for_range:
		distance = 0
		other_query = list(input_seqs[Yaxis_item]
		for base in list(range(0,len(first_query))):
			print("Index" + str(base) + ":" +
			str(first_query[base]) + "," + str(other_query[base]) + "...")
			if first_query[base] == other_query[base]:
				distance = distance + 1
			if input_seqs[Xaxis_item] != input_seqs[Yaxis_item]:
				print(str(distance) + " identities between " + input_seqs[Xaxis_item] +
				" and " + input_seqs[Yaxis_item])
				print("\t" + str(int(100*(distance/len(input_seqs[Xaxis_item])))) +
				" percent similarity between " + input_seqs[Xaxis_item] + " and " + input_seqs[Yaxis_item])
