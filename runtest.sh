#! /bin/bash

#PBS -l walltime=2:00:00
#PBS -l nodes=1:ppn=24
#PBS -N pyboost
#PBS -W group_list=newriver
#PBS -q dev_q
#PBS -A crawdad
#change this line to your email
##PBS -M amjames2@vt.edu
#PBS -m bea

cd $PBS_O_WORKDIR
module load gcc/4.7.2 Anaconda Anaconda-boost/1.58.0
source activate myenv

for i in {1..12};do
  export OMP_NUM_THREADS=${i}
  echo "running test ${i} thread(s)"
  mprof run runtest.py
done;
echo "done!"
