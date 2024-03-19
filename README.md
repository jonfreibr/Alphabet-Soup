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
* Edit alphasoup.py to reflect YOUR source spreadsheet (fully qualified path)
    The program user must have read access to this file. Write/modify
    access is NOT needed.

### Executing program

* python alphasoup.py
* python alphasoup.py -f an/alternate/spreadsheet.xls
* python alphasoup.py --file an/alternate/spreadsheet.xls

## Help

* python alphasoup.py -h
* python alphasoup.py --help

## Authors

Jon Freivald
jfreivald@brmedical.com

## Version History

* v 1.03(g)
    * 240319    : Reverted themes to a manual list of select themes to address a cross-platform issue
    where a multi-screen long list was unselectable. Update the list to your favorites.
* v 1.03(f)
    * 240109    : Added sort to data instead of depending on source sort. This eliminated having to arrow/mouse down to items that should have been under the selection highlight.
    * 240112    : Created testdata.xlsx and updated tests.py to perform all tests using data in this file. DO NOT modify the spreadsheet without updating tests to match. No code changes to program source.
    * Somewhere between here and v 1.02(a) I renamed as.py to alphasoup.py becuase "import as as s" simply did not work when implementing unittest
* v 1.03(e)
    * Updated event capturing return key to perform cross-platform.
    * 231205	: Added date to comments, because I always forget to update it in the header.
* v 1.03(d)
    * Fixed bug in window respawn scheme.
* v 1.03(c)
    * Minor tweak to dynamic theme scheme. Window will only respawn if theme was actually changed.
* v 1.03(b)
    * Change theme now takes effect immediately.
* v 1.03(a)
    * Added display of currently selected theme to menu bar.
* v 1.03
    * Completely redid Theme menu -- now pulls all available themes from PySimpleGui as options for the users to choose.
* 1.02(a)
    * Minor layout tweaks.
* 1.02
    * Aparently "Done" was confusing, so changed button text to "Quit"
* 1.01
    * First bug -- a network latency/vpn connectivity hiccup
* 1.0
    * Initial Release

## License

This project is licensed under the GNU GPL v3 License - see the LICENSE file for details

## Acknowledgments

This project would not have been possible without PySimpleGui or openpyxl. These are some
amazing and easy to use packages!

# Alphabet-Soup
 Acronym Lookup Tool
