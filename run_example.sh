clear
echo "" > EXAMPLE.md
MAX_IDX=19

for i in $(seq 1 $MAX_IDX); do
    cat calibrations/$i.txt | zoidberg | tee -a EXAMPLE.md
    if [[ $i != $MAX_IDX ]]; then
        echo -e "\n***\n" | tee -a EXAMPLE.md
    fi
done

cp ~/.zoidberg.brain.json example.brain.json
