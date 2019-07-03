# MAGAnalysis2
Snakemake version of Maganalysis (https://github.com/chrisquince/MAGAnalysis)

### Dependencies : 
- you need the following availlable in your path :
	- prodigal
	- rpsblast
	- mafft
	- trimal
	- FastreeMP
- you need the cog database formated for rpsblast (currently hard link in the snakemake)
### Instalation

     git clone git@github.com:Sebastien-Raguideau/MAGAnalysis2.git output_directory

Then you can  create a symbolic link of MagAnalysis.py to your bin directory or any such directory in your path, to call it from wherever you want. 
### Launch MAGAnalysis
MAGAnalysis support two types of inputs. 
Bins as outputed by **concoct (actually not debuged yet)** :

    MagAnalysis.py concoct contig contig_bin_assignment.csv output -t Threads  
- contig : a fasta file containing the contigs used for binning
- contig_bin_assignment.csv : clustering file outputed by concoct, the first column is a contig id, the second is a bin number.
- output: path/name of the directory where output will be placed
	
Bins as outputed by **metabat2** :  

    MagAnalysis.py metabat bin_dir  output -t Threads  

- bin_dir : directory where all the fasta files of the bins are stored, MagAnalysis.py will consider any file ending with a fasta file containing the contigs used for binning
- output: path/name of the directory where output will be placed

### Directory structuration
- bins_analysis : store data about bins, such as SCG table and list of good quality bins. 
- bins : folder where, for each bin, a symbolic link is created
- MAGs : folder where, for each Mag, a symbolic link is created
- Tree : 
	- scg : folder of extracted single copy core genes + refferences scg
	- trimal :
	- mafft :
	- fastree : tree is here
