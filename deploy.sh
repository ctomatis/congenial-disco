ZIP=lambda.zip

rm -f $ZIP
cd .env/lib/python3.8/site-packages
zip -r --exclude=*__pycache__* ../../../../$ZIP .
cd ../../../../
zip $ZIP lambda_function.py templates/*
aws lambda update-function-code --function-name report --zip-file fileb://$ZIP