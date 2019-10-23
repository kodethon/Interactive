if [ -z $1 ]; then
    echo "Usage: sh run.sh <PATH-TO-FILE>"
    exit
fi

image_name=interactive-text-build
textbook_name=$(basename $1)

docker build -t $image_name .
docker run -v /tmp:/tmp -v "$1:/root/$textbook_name" $image_name python driver.py $textbook_name
