ls | sort -R | tail -$N | while read file; do
    cp $file /home/dcml/Downloads/testdata/evaluation/$file
done
