# python-puzzles

A collection of small, self-contained Python puzzles — one directory per puzzle, each holding a single script with the solution function plus a `print(...)` call demonstrating it.

Every script runs standalone with no dependencies beyond the standard library. Developed against **Python 3.13**.

```bash
python3 puzzle_one/puzzle.py
```

Running a script executes the demo calls at the bottom of the file and prints the results.

## The puzzles

Listed in the order they were written.

### 1. `puzzle_one/puzzle.py` — filter strings containing "a"

`filter_strings_containing_a(input_str: list[str]) -> list[str]`

Returns the strings from a list that contain a lowercase `"a"`. Built with an explicit accumulator loop.

```python
filter_strings_containing_a(['apple', 'banna', 'cherry', 'date'])
# ['apple', 'banna', 'date']
```

### 2. `sum_if_less_than_fifty/sum_if_less_than_fifty.py` — capped sum

`sum_if_less_than_fifty(input_1: int, input_2: int) -> int | None`

Adds two integers and returns the total only if it is under 50; otherwise returns `None`. A first look at `int | None` as a return type.

```python
sum_if_less_than_fifty(30, 10)  # 40
sum_if_less_than_fifty(40, 10)  # None
```

### 3. `sum_even/sum_even.py` — sum of even numbers

`sum_even(numbers: list[int]) -> int`

Sums only the even values in a list.

```python
sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 30
```

### 4. `remove_vowels/remove_vowels.py` — strip vowels

`remove_vowels(input_str: str) -> str`

Removes vowels from a string by looping over a vowel list and calling `str.replace` for each one. Only lowercase vowels are stripped — the `"e"` in `"Hello"` goes, the `"o"` in `"World"` goes, but a capital `"O"` would survive.

```python
remove_vowels("Hello, World!")  # 'Hll, Wrld!'
```

### 5. `get_longest_string/get_longest_string.py` — longest string

`get_longest_string(list: list[str]) -> str`

Tracks the longest string seen while iterating. Since the comparison is strictly greater-than, ties resolve to the **first** of the tied strings, and an empty input returns `''`.

```python
get_longest_string(["a", "b", "c", "d"])  # 'a'
```

### 6. `filter_even_length_string/filter_even_length_string.py` — shortest strings

`filter_even_length_strings(list: list[str]) -> list[str]`
`get_lenth_value(string: str) -> int`

Returns every string tied for the shortest length in the list, with `[]` for empty input.

```python
filter_even_length_strings(["cat", "dog", "fish", "elephant"])  # ['cat', 'dog']
```

> **Note:** the directory and function names say "even length", but the implementation filters for **shortest** length — worth reconciling one way or the other. The `get_lenth_value` helper is also unused (and misspelled).

### 7. `reverse_elements/reverse_elements.py` — reverse a list

`reverse_elements(list: list[int]) -> list[int]`

Reverses a list using a `[::-1]` slice, returning a new list rather than mutating in place.

```python
reverse_elements([1, 2, 3, 4, 5])  # [5, 4, 3, 2, 1]
```

### 8. `filter_type_str/filter_type_str.py` — keep only strings

`filter_type_str(inputList: list[str | int])`

Filters a mixed list down to just its string elements using `isinstance`.

```python
filter_type_str(["www", 112, 22, 'ff', '3'])  # ['www', 'ff', '3']
```

### 9. `string_to_morse_code/string_to_morse_code.py` — Morse encoder

`string_to_morse_code(string: str)`

Encodes text to Morse using a lookup table covering a–z, 0–9, and common punctuation. Input is lowercased first, spaces become `/`, and letters are separated by a space. Characters outside the table raise a `KeyError`.

```python
string_to_morse_code("HELLO, WORLD!")
# '.... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.-- '
```

### 10. `get_second_largest_number/get_second_largest_number.py` — second largest

`get_second_largest_number(list2: list[int]) -> int | None`

Sorts the list's unique values descending and returns the runner-up, or `None` when fewer than two distinct values exist. Deduplicating via `set` means `[5, 5, 3]` gives `3`, not `5`.

```python
get_second_largest_number([1])  # None
```

### 11. `format_number_with_commas/format_number_with_commas.py` — thousands separators

`format_number_with_commas(num: int) -> str`

Formats an integer with comma separators using the `f"{num:,}"` format spec.

```python
format_number_with_commas(1000000)  # '1,000,000'
```

### 12. `ascii_map/ascii_map.py` — ASCII lookup table

`CHAR_TO_DEC`

A module-level dict mapping each character to its decimal code point for 0–126. Guarded by `if __name__ == "__main__"`, so importing it gives you the table without printing all 127 rows.

```bash
python3 ascii_map/ascii_map.py
# '\x00': 0
# '\x01': 1
# ...
```

### 13. `string_to_ascii/string_to_ascii.py` — ASCII round-trip

`string_to_ascii(text: str) -> list[int]`
`ascii_to_string(list_ascii: list[int]) -> str`

Converts a string to a list of ASCII codes and back again, each direction building its own lookup dict over 0–127. Non-ASCII input raises a `KeyError`.

```python
string_to_ascii("Programming puzzles!")
# [80, 114, 111, 103, 114, 97, 109, 109, 105, 110, 103, 32, ...]
ascii_to_string(string_to_ascii("Programming puzzles!"))
# 'Programming puzzles!'
```

### 14. `filter_strings_with_vowels/filter_strings_with_vowels.py` — strings with vowels

`filter_strings_with_vowels(str_list: list[str]) -> list[str]`

Keeps strings containing at least one lowercase vowel, using `any()` over a generator.

```python
filter_strings_with_vowels(["apple", "banana", "zyxvb"])  # ['apple', 'banana']
```

### 15. `reverse_first_five_positions/reverse_first_five_positions.py` — partial reverse

`reverse_first_five_positions(items: list[int]) -> list[int]`

Reverses the first five elements and leaves the rest in order, via slice-reverse-concatenate. Lists shorter than five elements are simply reversed whole — the slices handle that without a special case.

```python
reverse_first_five_positions([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
```

## Layout

```
python-puzzles/
├── ascii_map/
│   └── ascii_map.py
├── filter_even_length_string/
│   └── filter_even_length_string.py
├── filter_strings_with_vowels/
│   └── filter_strings_with_vowels.py
├── filter_type_str/
│   └── filter_type_str.py
├── format_number_with_commas/
│   └── format_number_with_commas.py
├── get_longest_string/
│   └── get_longest_string.py
├── get_second_largest_number/
│   └── get_second_largest_number.py
├── puzzle_one/
│   └── puzzle.py
├── remove_vowels/
│   └── remove_vowels.py
├── reverse_elements/
│   └── reverse_elements.py
├── reverse_first_five_positions/
│   └── reverse_first_five_positions.py
├── string_to_ascii/
│   └── string_to_ascii.py
├── string_to_morse_code/
│   └── string_to_morse_code.py
├── sum_even/
│   └── sum_even.py
└── sum_if_less_than_fifty/
    └── sum_if_less_than_fifty.py
```

## Conventions

Puzzles in this repo follow a consistent shape:

- One directory per puzzle, named after the puzzle; the script inside carries the same name.
- The solution is a single function with type annotations on parameters and return value.
- Demo `print(...)` calls sit at module level at the bottom of the file, so running the script shows the solution working. `ascii_map` is the exception — it guards its demo with `if __name__ == "__main__"`.
