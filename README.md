# Alphabet Soup

A quick acronym lookup tool.

## Description

Stop paging through lists or scrolling through listings of thousands of acronyms!
The idea for this tool hit me when my acronym sheet hit 3 pages -- my collection
is now over 8000 and growing.

Alphabet Soup uses an Excel spreadsheet as the data source. It will automatically
refresh data every time the spreadsheet is saved.

The spreadsheet is expected to contain a sheet named "AlphabetSoup" with acronyms 
in column A starting in Row 5 and definitions in column B. Feel free to edit the
code to reflect your existing spreadsheet.

## Getting Started

Create your spreadsheet, add some acronyms and definitions, and launch. Instead of
scrolling through a long list (my list is already > 8000 acronyms long, hence the need
for a better way!), you simply type-in to the acronym you need. Typing the first letter
starts a predictive list showing you the first 5 choices based on what you type. The
more you type, the more precise the list gets. The search is not case sensitive. Once 
you have started typing, you can use the arrow keys to scroll up and down the
predictive list.

### Dependencies

* Python (3.11.5)
* PySimpleGui (4.60.5)
* openpyxl (3.1.2)
* pytz (2023.3)

### Installing

* https://github.com/jonfreibr/Alphabet-Soup
* Install Python
* "pip install -r {Alphabet-Soup Directory}\requirements.txt"
* Edit as.py to reflect YOUR source spreadsheet (fully qualified path)
    The program user must have read access to this file. Write/modify
    access is NOT needed.

### Executing program

* python as.py
* python as.py -f an/alternate/spreadsheet.xls
* python as.py --file an/alternate/spreadsheet.xls

## Help

* python as.py -h
* python as.py --help

## Authors

Jon Freivald
jfreivald@brmedical.com

## Version History

* 1.0
    * Initial Release
* 1.01
    * First bug -- a network latency/vpn connectivity hiccup
* 1.02
    * Aparently "Done" was confusing, so changed button text to "Quit"
* 1.02(a)
    * Minor layout tweaks.

## License

This project is licensed under the GNU GPL v3 License - see the LICENSE file for details

## Acknowledgments

This project would not have been possible without PySimpleGui or openpyxl. These are some
amazing and easy to use packages!

# Alphabet-Soup
 Acronym Lookup Tool
