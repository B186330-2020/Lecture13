#!/bin/python3
flygenedata = open("data.csv")
for geneline in flygenedata :
	gene_info = geneline.split(",")
	species_name = gene_info[0]
	sequence = gene_info[1].upper()
	sequence_length = len(gene_info[1])
	gene_name = gene_info[2]
	expression_level = int(gene_info[3])
	atcontent = (sequence.count('A') + sequence.count('T'))/sequence_length
	atstatus = "low" 
	if (atcontent >=0.45 and atcontent <= 0.65) :
		atstatus="medium"
	if (atcontent>0.65) :
		atstatus="high"
	if "melanogaster" in species_name or "simulans" in species_name:
		print("Q1: Gene from melanogaster or simulans " + gene_name)
	else: 
		print("Q1 fail: " + species_name + gene_name) 
	if sequence_length < 90 and sequence_length < 110 :
		print("Q2: Gene between 90 and 110 bases " + gene_name)
	else: 
                print("Q2 fail: " + species_name + gene_name)
	if atcontent < 0.5 and expression_level > 200:
		print("Q3: AT content more than 0.5 and expression level over 200 " + gene_name) 
	else: 
                print("Q3 fail: " + species_name + gene_name)
	if (gene_name.startswith("k") or gene_name.startswith("h")) and ("Drosophila melanogaster" not in species_name):
		print("Q4: Begins with k or h, not d. melanogaster" + gene_name)
	else: 
                print("Q4 fail: " + species_name + gene_name)
	print("Q5: " + gene_name + " AT status is " + atstatus)
