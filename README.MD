# Everlastly
Everlastly API for Python. Notarize data using the blockchain. Asynchronous version is [here](https://github.com/Everlastly-team/python-async).

## Installation
```
pip install everlastly
```
## Usage
```python
from everlastly import Everlastly

# Sign up and get your keys at https://everlastly.com/keys
e=Everlastly('pub key', 'priv key')

example_hash="3e79ffa0e95c435ec8ee50ebb6959259968b4c66852d4fba4fc0876e83b4a0e1"

anchor_result = e.anchor(example_hash, metadata={"additional info":"隨機詞"})
#...
#Wait for it
if anchor_result["success"]:
  print(e.get_receipts([ anchor_result["receiptID"], ])

```

# Feedback

Contact us via support@everlastly.com 

