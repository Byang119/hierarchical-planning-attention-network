# hierarchical-planning-attention-network
  
## Data
The dataset WIKIBIO is available from [https://github.com/DavidGrangier/wikipedia-biography-dataset](https://github.com/DavidGrangier/wikipedia-biography-dataset)  
  
We preprocess the data following the work of [Liu et al. 2018](https://tyliupku.github.io/papers/aaai2018_liu.pdf). You can download the `original_data` from [https://github.com/tyliupku/wiki2bio](https://github.com/tyliupku/wiki2bio)

### Preprocess
Firstly, we extract words, keys and positions from the original infoboxes.
	python prepro.py
Then we order the input attributes according to the order in which they appear in the summaries.
	python prepro/preprocess_order.py


## Train  
The code will be released soon.  

## Test
The test results of our model from the test set of WIKIBIO are stored in the `test` directory `test/test.summary_hplan`.

