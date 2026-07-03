# Cutlist Calculator v4.5
#### Video Demo:  <https://youtu.be/TYj2wRJ3b3M>
### Description:
The Cutlist Calculator is an app that allows contractors and DIYers alike to calculate the total amount of raw materials needed for their projects.
Users are able to browse their PC and select any *correctly formatted Excel Cutlist spreadsheet (A template for accepted cutlist formats is provided).
After the cutlist is selected, the user can load in the list and select basic parameters, such as; board types (e.g. 2x4, 4x4, etc) found in the list, as well as the stock length they intend to use, and finally the quantity of cutlists to figure for. The calculation outputs "Treated" and "Untreated" materials separate of each other, which is set within the Cutlist spreadsheet.

The method in which the Calculator uses assumes that the cutlist will be cutout starting with the longest pieces, and working down from there, using leftover cutoffs where ever possible.
While this is not the most efficient way to calculate, it still comes out reasonably close while maintaining practicality in the order and method it will need to be cut out in the real world.

### Features:
* Free of large python libraries, minimal application size for a "onefile" python application.
* Quick file load and calculation algorithm
* Decent GUI
* On the fly cutlist quantity adjustment
* On the the fly stock length adjustment
* Invalid File type or bad spreadsheet formatting handling
* Invalid stock length (Too short to satisfy cut lengths in cutlist given) handling
* Good luck getting it to crash (I'll probably eat my words)

### Cutlist Spreadsheet Formatting
Please look at the Excel speadsheet provided in the application folder labeled "Cutlist Template" and note the following:

1. The name of your cutlist is specified in A:1
    - This is mainly for your reference, and can be changed to whatever you prefer. It is also displayed in the app upon loading the file, just for more confirmation on the process.
2. Quantity, Board type, and Cut Length must remain in columns B, C, E.
    - This is crucial for the calculator to properly pull the data off of the spreadsheet.

3. You must specify at least one of either "treated" or "untreated" tags and:
    - It must be in column A.
    - It must be exactly one row above where the cutlist values start.
    - If both "treated" and "untreated" tags are to be used, there must be at least 1 blank row after the values before calling the second tag.
    - It does not matter in which order you specify "treated" and "untreated".
4. Only Whole numbers should be stored in QT. (Quantity)
5. You can use any value you like within Board Type.
6. Cut length must be whole numbers, or whole numbers with a space between a fraction.
    - The fraction must be typed manually, using a slash, no built in fractions charecters should be used.
    - Optionally a double quote (") may be used afterwards to specify inches, but it is not required.
7. At this time, angles are not taken into calculation, and can be formatted to your liking. Angles may be taken into consideration in a future version.
8. Categorizing is allowed within Column A as you like, as long as:
    - The name is not "treated" or "untreated".
    - The row directly above the values to be calculated is reserved for "treated" and "untreated".
9. You can use as much space beyond Column F and below you last value to be calculated, for more details that pertain to your project, etc., as that space will be ignored by the Calculator.
10. Font size, and styling/ Cell boarders is permitted as you desire.
