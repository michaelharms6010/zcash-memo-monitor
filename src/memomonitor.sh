set -x
while true
do
    ./zecwallet-cli list | python memoprocessor.py
    sleep 60
done