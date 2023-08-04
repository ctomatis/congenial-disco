ZIP=lambda.zip

rm -f $ZIP
#.env/bin/python3 -m pip install .
cd .env/lib/python3.8/site-packages
zip -r --exclude=*__pycache__* ../../../../$ZIP .
cd ../../../../
zip $ZIP lambda_function.py templates/*
aws lambda update-function-code --function-name report --zip-file fileb://$ZIP


#aws lambda update-function-code --function-name myFunction \
#--s3-bucket myBucketName --s3-key myFileName.zip