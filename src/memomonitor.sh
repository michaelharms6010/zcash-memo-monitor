set -x
while true
do
    ./zcash-cli z_listreceivedbyaddress zs1n5m4szkmqup6ht9nuwke9j5w6pwcd527l4sm8u2aqqhaedjv5at64el6eyazm6engqplx0ht6x9 | python memoprocessor.py
    sleep 60
done