# Price Formatter

Script for formatting prices from 975843.230000 to 975 843.23 .

##Using

    $python3 format_price.py price
    
price parameter must be in format [integer_part.fractional_part]. If you want to format price without fractional part, just type integer_part.00 like 34.00 or 34.0.

You also can use format_data() from script in your code.
    
    from format_price import format_price
    
Script tests.py provide you to check script work with different data.
  

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
