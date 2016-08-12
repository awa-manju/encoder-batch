function file_old(){
  TODAY=$(date +%s)
  ARG1_DATE=$(date +%s -r $1)
  expr $TODAY - $ARG1_DATE
}

function days2sec(){
  expr 3600 \* 24 \* $1
}

function list_aged_files(){
  local DIR=$1
  local FNAME=$2
  local AGE_DAYS=$3
  for i in $(find $DIR/$FNAME); do
    if [ $(file_old $i) -gt $(days2sec $AGE_DAYS) ]; then
      echo $i
    fi
  done
}
