#! /bin/bash

python producer.py &

#assign N from the CLI
declare -i N=0
declare -i numPort=6000

N=$1

#echo "$(($N+1))";

for x in $( eval echo {1..$N})
do
# we would assign push port for each two consumers
python consumer.py $numPort &
if (( $x % 2 == 0 ))
then
    python collector.py $numPort &
    numPort+=1
fi
done


#in case of odd N
if (( $N % 2 != 0))
then
python collector.py $numPort &
fi
