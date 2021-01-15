# Exeter Maths School Outreach - NLP Project

## Setup

The packages we require are only guaranteed to work in Python 3.7.

If you already have Python 3.7 installed and want to jump straight in 
skip to step 4. 

If you want an environment built from the ground up follow steps 1 to 4.

1.) Install Miniconda from [here](https://docs.conda.io/en/latest/miniconda.html)

You can check it is installed properly with
```
>>> conda -V
```

If it is not, you need to find the path of your conda installation and run
```
>>> conda init <SHELL_NAME>
```

If you don't know what to put for <SHELL_NAME> run
```
>>> echo $SHELL
```

2.) Create a Python 3.7 virtual environment

```
>>> conda create -n venv python=3.7 anaconda
```

3.) Activate your environment

```
>>> source activate venv
```

4.) Install the requirements

```
>>> pip install -r requirements.txt
```

## Notebooks

[0](notebooks/0_IntroToJupyter.ipynb) -
Learn how to use Jupyter notebooks.

[1](notebooks/1_PreparingTextData.ipynb) - 
Learn how to clean and prepare the headlines dataset.

[2](notebooks/2_EDA.ipynb) -
Explore the headlines dataset.
 
[3](notebooks/3_JaccardDistance.ipynb) -
Learn about a metric for sentence similarity based on sets.
 
[4](notebooks/4_CosineSimilarity.ipynb) -
Learn about a metric for word similarity based on word embeddings.

[5](notebooks/5_WordMoversDistance.ipynb) -
Learn about a metric for sentence similarity based on the cosine similarity.
 
[6](notebooks/6_Classifiers.ipynb) -
Build a model to predict if a headline is sarcastic or genuine.