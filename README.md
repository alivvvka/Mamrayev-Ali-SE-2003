# CoinGecko

The CoinGecko data market APIs are a set of robust APIs that developers can use to not only enhance their existing apps and services but also to build advanced crypto market apps. The team is also responsive to feedback and the occasions that we did these were quickly implemented into their api services.

## Installation


```bash
pip install pycoingecko
```

## Usage

```python
from pycoingecko import CoinGeckoAPI

# returns list of cryptocurrency (in usd price)
list = cg.get_coins_markets("usd")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
