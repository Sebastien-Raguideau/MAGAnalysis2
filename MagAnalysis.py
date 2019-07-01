#!/usr/bin/env python

from os.path import abspath, realpath, dirname
import subprocess 
import argparse
import os,sys

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(dest='mode',help="either concoct or metabat : select input bin format, If concoct, a contig file as well as a clustering file are expected. If metabat, a folder with one fasta by bin is expected")
	#------- concoct case ------------ 
	# define a subparser
	parser_concoct = subparsers.add_parser('concoct')
	# add argument to subparser
	parser_concoct.add_argument("contigs",help='contig fasta file')
	parser_concoct.add_argument("bin_composition",help='csv file outputed by concoct giving the assignement of each contig to each bin')
	parser_concoct.add_argument("output",help='output folders')
	parser_concoct.add_argument("-t",help='number of threads',default=1)
	parser_concoct.add_argument('-s', nargs=argparse.REMAINDER,help="Pass additional argument directly to snakemake")

	#------- metabat ------------ 
	# define a subparser
	parser_metabat = subparsers.add_parser('metabat')
	# add argument to subparser
	parser_metabat.add_argument("bin_folder",help='folder where the bins are located')
	parser_metabat.add_argument("output",help='output folders')
	parser_metabat.add_argument("-t",help='number of threads',default=1)
	parser_metabat.add_argument('-s', nargs=argparse.REMAINDER,help="Pass additional argument directly to snakemake")

	#------ get values ----------
	args = parser.parse_args()
	if args.mode == 'concoct':
		fasta_file=abspath(realpath(args.contigs))
		bin_composition=abspath(realpath(args.bin_composition))
		bin_folder="bins/"
	if args.mode== 'metabat':
		fasta_file=""
		bin_composition=""
		bin_folder=abspath(realpath(args.bin_folder))
	threads=args.t		
	output=abspath(realpath(args.output))+"/MAGAnalysis"

	# setup snakemake
	script_path = dirname(abspath(realpath( __file__ )))+"/"
	os.system("mkdir -p "+output)
	base_params = ["snakemake", "--directory", abspath(realpath(output)), "--cores", str(threads), "--config", "CONTIGS=" + fasta_file ,"BIN_COMPOSITION="+bin_composition,"BIN_FOLDER="+bin_folder, "--latency-wait", "120",'--snake',script_path+"MagAnalysis.snake"]

	# additional argument : 
	if args.s :
	    base_params.extend(args.s)
	
	# finally launch snakemake
	subprocess.check_call(base_params, stdout=sys.stdout, stderr=sys.stderr)

