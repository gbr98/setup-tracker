# setup-tracker 💸
Price tracking software for shopping lists.

Python script to track prices of items in shopping sites. The script was created to track the price of my whole computer setup, using different stores for each of the components. It uses a list of links filled into a text file and return the sum of the prices found in each of the links. It can keep executing repeatedly if the number of seconds to wait is specified on the command line, so it keeps scanning for the price of your shopping list.

## Installation
Requirements:
- python3 (3.7+)
- python-venv
- compatible browser (Firefox or Chrome)

Clone this repository to a local folder:
```bash
git clone https://github.com/gbr98/setup-tracker
```
Move to the project folder, activate the venv and execute the main script
```bash
cd setup-tracker
source venv/bin/activate
python3 tracker.py
```
