# PPD_MLSD

### Pull the repo
```git clone git@github.com:rafmkyrie/PPD_MLSD.git```

or

```git clone https://github.com/rafmkyrie/PPD_MLSD.git```

### Create Docker Image
```docker build -t torchmoji .```

### Run container in interactive mode with a volume
```docker run -v .:/app -it torchmoji /bin/sh```

### Run score script
```python examples/score_texts_emojis.py```



