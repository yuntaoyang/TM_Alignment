# TM_Alignment
A python script that can generate an aligned PDB file from two PDB files and also print TM-score.
1. Run the following command to clone this git repo.
```
git clone git@github.com:yuntaoyang/TM_Alignment.git
```
2. Test the script using the test_data.
```
python scripts/tm_align.py --pdb_dir_1 test_data/input/A0FGR8-1.pdb --pdb_dir_2 test_data/input/A0FGR8-2.pdb --out_dir test_data/output/A0FGR8-1_A0FGR8-2.pdb
```
3. It will return `test_data/output/A0FGR8-1_A0FGR8-2.pdb` as the aligned PDB file and also print the TM-score.
4. Apply the script to your data by checking `python scripts/tm_align.py -h`.