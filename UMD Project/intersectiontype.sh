echo "type,intersection" > intersectiontype.csv
cat intersectiontype.txt | sed 's/ //g' | tr '=' ',' >> intersectiontype.csv