#!/bin/bash

FILE=$1
BUCKET=$2
EXP_S=$3

aws s3 cp $FILE s3://$BUCKET/

aws s3 presign --expires-in $EXP_S s3://$BUCKET/$FILE




