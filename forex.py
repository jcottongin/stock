#!/usr/bin/python3
from forex_python.converter import CurrencyRates
import pandas as pd

import time
c = CurrencyRates()
usd=c.get_rates('USD')
print(usd)
