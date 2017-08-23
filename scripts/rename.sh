a=1
for i in *.jpg; do
  new=$(printf "%03d.jpg" "$a") #0 pad to length of 
  mv -i -- "$i" "$new"
  let a=a+1
done
