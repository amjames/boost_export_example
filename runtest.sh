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


for i in {1..12};do
  source activate default
  export OMP_NUM_THREADS=${i}
  echo "running test 1 thread"
  mprof run runtest.py
done;
echo "done!"
