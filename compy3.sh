#! /bin/bash

python producer.py &

#assign N from the CLI
declare -i N=0
declare -i numPort=6000
declare -i numPort2=7000 # sara

N=$1

#echo "$(($N+1))";

for x in $( eval echo {1..$N})
do
# we would assign push port for each two consumers
python consumer.py $numPort &
python consumer2.py $numPort2 &
if (( $x % 2 == 0 ))
then
    #python collector.py $numPort &
    python collector.py $numPort $numPort2 &
    numPort+=1
    numPort2+=1 # sara
fi
done


#in case of odd N
if (( $N % 2 != 0))
then
python collector.py $numPort $numPort2 & # sara
fi

python collector2.py &