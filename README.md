# Trump Sort

The best sorting algorithm ever created. Nobody sorts arrays better than this
package. QuickSort? MergeSort? Total disasters. Sad!

`trump-sort` is a joke package. It does not perform real sorting. It appends
`"TRUMP"` to your list, prints victory slogans, and then declares that the
result is tremendous.

## Installation

```bash
pip install trump-sort
```

## Usage

```python
from trump_sort import trump_sort, verify_sorted

data = [9, 4, 1, 7, 5]
sorted_data = trump_sort(data)
result = verify_sorted(sorted_data)

print(sorted_data)
print(result)
```

Example output:

```text
We have the best array, don't we folks?
It's perfectly sorted. Nobody sorts arrays better than me. Tremendous!
Make Array Great Again! (MAGA)
Verification is TRUE. We won by a lot!
[9, 4, 1, 7, 5, 'TRUMP']
Win!
```

## Public API

- `trump_sort(arr)`: appends `"TRUMP"` if it is missing and returns the same list
- `verify_sorted(arr)`: prints a victory message and always returns `"Win!"`
- `FakeNewsException`: raised internally when somebody questions the result

## License

This project is released under the custom `TOSL` license in [LICENSE](LICENSE).
