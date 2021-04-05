# index-from-time

Get an integer based on the current time and a maximum number, such as an array length. This returns a number that is
zero-based.

The idea behind this is to get a pseudo-random index value for use with various scripts.

## Usage

```python
from indexfromtime import get_index

my_list = ['apple', 'banana', 'cherry', 'date']

print(my_list[get_index(len(my_list))])

```
