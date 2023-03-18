# ========== nthBday ==========


**nthBday** is a an open-source python package to find business/working days of a month.

##### Please Note: The holidays taken here are Indian holidays. In the next versions our countries holidays will be added too.

## Installation

nthBday requires [Python 3](https://www.python.org/downloads/) and [pandas](https://pandas.pydata.org/) to execute.

To install using pip, use

`pip install nthBday`

[![Downloads](https://static.pepy.tech/badge/nthbday/month)](https://pepy.tech/project/nthbday)

## Features 

### nthBday package contains different functions such as:
* **first_working_day**: Returns the first working day of a month
* **second_working_day**: Returns the second working day of a month
* **third_working_day**: Returns the third working day of a month
* **fourth_working_day**: Returns the fourth working day of a month
* **fifth_working_day**: Returns the fifth working day of a month
* **nth_working_day**: Returns the n-th working day of a month
* **last_working_day**: Returns the last working day of a month
* **nth_last_working_day**: Returns the n-th last working day of a month
* **last_sun**: Returns the last sunday of a month
* **last_sat**: Returns the last saturday of a month
* **last_fri**: Returns the last friday of a month
* **last_thu**: Returns the last thursday of a month
* **last_wed**: Returns the last wednesday of a month
* **last_tue**: Returns the last tuesday of a month
* **last_mon**: Returns the last monday of a month
* **second_sat**: Returns the second saturday of a month
* **fourth_sat**: Returns the fourth saturday of a month


## Usage

* **Import the library**:

``` python
import nthBday as nb
```

## Examples


``` python
import nthBday as nb
nb.first_working_day(2,2023)
```

returns,

``` Python
datetime.date(2023, 2, 1)
```


``` python
import nthBday as nb
nb.nth_working_day(2,2023,17)
```

returns,

``` Python
datetime.date(2023, 2, 23)
```



``` python
import nthBday as nb
nb.last_working_day(2,2023)
```

returns,

``` Python
datetime.date(2023, 2, 28)
```


``` python
import nthBday as nb
nb.nth_last_working_day(2,2023,17)
```

returns,

``` Python
datetime.date(2023, 2, 6)
```



``` python
import nthBday as nb
nb.last_thu(3,2023)
```

returns,

``` Python
datetime.date(2023, 3, 30)
```


``` python
import nthBday as nb
nb.second_sat(3,2023)
```

returns,

``` Python
datetime.date(2023, 3, 11)
```








## License

##### MIT

