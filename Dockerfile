FROM public.ecr.aws/lambda/python:3.11
#FROM python:3.10
MAINTAINER "vinod.lakk@gmail.com"
# RUN mkdir /code
ADD . ${LAMBDA_TASK_ROOT}

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#CMD ["python", "/code/app.py"]
CMD ["lambda_function.lambda_handler"]
