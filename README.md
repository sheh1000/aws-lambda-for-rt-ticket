# aws-lambda-for-rt-ticket

Use https://github.com/nficano/python-lambda project to deploy Lambda function to AWS

If you got the error 

    "ImportError: No module named rtapi" 
    
then just copy __rtapi.py__ to __/root/.virtualenvs/pylambda/local/lib/python2.7/site-packages/__
    
before you ran __'lambda deploy'__ command
