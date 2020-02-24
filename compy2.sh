#! /bin/bash

#python producer.py &

#assign N from the CLI
declare -i N=0
declare -i numPort2=7000

N=$1

#echo "$(($N+1))";
python collector2.py &
for x in $( eval echo {1..$N})
do
# we would assign push port for each two consumers
python consumer2.py $numPort2 &
if (( $x % 2 == 0 ))
then
    #python collector.py $numPort &
    numPort2+=1
fi
done



#in case of odd N
# if (( $N % 2 != 0))
# then
# python collector.py $numPort &
# fi
