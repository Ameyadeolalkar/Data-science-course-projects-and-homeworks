#Class 2 Homework

* **1. Look at the head and the tail of chipotle.tsv in the data subdirectory of this repo. Think for a minute about how the data is structured. What do you think each column means? What do you think each row means? Tell me! (If you're unsure, look at more of the file contents.)**


    _$ head chipotle.tsv
    order_id        quantity        item_name       choice_description      item_price
    1       1       Chips and Fresh Tomato Salsa    NULL    $2.39
    1       1       Izze    [Clementine]    $3.39
    1       1       Nantucket Nectar        [Apple] $3.39
    1       1       Chips and Tomatillo-Green Chili Salsa   NULL    $2.39
    2       2       Chicken Bowl    [Tomatillo-Red Chili Salsa (Hot), [Black Beans, Rice, Cheese, Sour Cream]]      $16.98
    3       1       Chicken Bowl    [Fresh Tomato Salsa (Mild), [Rice, Cheese, Sour Cream, Guacamole, Lettuce]]     $10.98
    3       1       Side of Chips   NULL    $1.69
    4       1       Steak Burrito   [Tomatillo Red Chili Salsa, [Fajita Vegetables, Black Beans, Pinto Beans,     Cheese, Sour Cream, Guacamole, Lettuce]]      $11.75
    4       1       Steak Soft Tacos        [Tomatillo Green Chili Salsa, [Pinto Beans, Cheese, Sour Cream,         Lettuce]]       $9.25

   $ tail chipotle.tsv
   1831    1       Carnitas Bowl   [Fresh Tomato Salsa, [Fajita Vegetables, Rice, Black Beans, Cheese, Sour    Cream, Lettuce]]       $9.25
   1831    1       Chips   NULL    $2.15
   1831    1       Bottled Water   NULL    $1.50 
   1832    1       Chicken Soft Tacos      [Fresh Tomato Salsa, [Rice, Cheese, Sour Cream]]        $8.75
   1832    1       Chips and Guacamole     NULL    $4.45
   1833    1       Steak Burrito   [Fresh Tomato Salsa, [Rice, Black Beans, Sour Cream, Cheese, Lettuce,    Guacamole]]       $11.75
   1833    1       Steak Burrito   [Fresh Tomato Salsa, [Rice, Sour Cream, Cheese, Lettuce, Guacamole]]       $11.75
   1834    1       Chicken Salad Bowl      [Fresh Tomato Salsa, [Fajita Vegetables, Pinto Beans, Guacamole,    Lettuce]]      $11.25
   1834    1       Chicken Salad Bowl      [Fresh Tomato Salsa, [Fajita Vegetables, Lettuce]]      $8.75
   1834    1       Chicken Salad Bowl      [Fresh Tomato Salsa, [Fajita Vegetables, Pinto Beans, Lettuce]]    $8.75_


   **Each Column provides a description of the data under it
   Each row provides details of the order**

* **2. How many orders do there appear to be?**

   _$ cut -f 1 chipotle.tsv | uniq | wc -l
   1835_

* **3. How many lines are in this file?**

   _$ wc -l chipotle.tsv
   4623 chipotle.tsv_

* **4. Which burrito is more popular, steak or chicken?**

   _adll@USNYW7WADLL ~/Documents/GitHub/Dat8/data (master)
   $ grep -i "chicken burrito" chipotle.tsv | wc -l
    553

   adll@USNYW7WADLL ~/Documents/GitHub/Dat8/data (master)
   $ grep -i "steak burrito" chipotle.tsv | wc -l
    368_

   **Chicken Burrito is more popular**

* **5. Do chicken burritos more often have black beans or pinto beans?**

   _adll@USNYW7WADLL ~/Documents/GitHub/Dat8/data (master)
   $ grep -i "chicken burrito" chipotle.tsv | grep -i "pinto beans" | wc -l
    105

   adll@USNYW7WADLL ~/Documents/GitHub/Dat8/data (master)
   $ grep -i "chicken burrito" chipotle.tsv | grep -i "black beans" | wc -l
    282_

   **Chicken burritos have black beans more often**


* **6. Make a list of all of the CSV or TSV files in the DAT8 repo (using a single command). Think about how    wildcard characters can help you with this task.**   

   _adll@USNYW7WADLL ~/Documents/GitHub/Dat8/data (master)
   $ find *.csv *.tsv
   airlines.csv
   chipotle.tsv
   sms.tsv_

* **7. Count the approximate number of occurrences of the word "dictionary" (regardless of case) across all files    in the DAT8 repo.**

   _$ grep -i "dictionary" *.csv *.tsv | wc -w
     92_

* **8.Optional: Use the the command line to discover something "interesting" about the Chipotle data. Try using the commands from the "advanced" section!**

  _adll@USNYW7WADLL ~/Documents/GitHub/Dat8/data (master)
  $ uniq chipotle.tsv | grep -i "chicken burrito" | grep -i "guacamole" | cut -f4

  174 unique orders have guacamole in them
  price of a chicken burrito goes up by $2.50 if you order guacamole "Quite pricey"_