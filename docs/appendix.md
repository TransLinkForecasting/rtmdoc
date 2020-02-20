# Appendix

In this section, you will find some useful infomation you may need to use in your RTM application project. Some of them are RTM assumptions and some of them are the calibrated factors. This document could be a dictionary of the model components.

## Time of Assginment

The RTM model only handles 3 scenarios in each databank. Each scenario stores one-hour assignment result, and it is used to represent various periods throughout the day.

Peak Period | Hour | Hours of the day represented
----------- | ---- | ----------------------------
AM | 07:30 - 08:30 | 06:00 - 10:00
MD | 12:00 - 13:00 | 10:00 - 15:00, 18:00 - 06:00
PM | 16:30 - 17:30 | 15:00 - 18:00


## Expansion Factor
The traffic expansion factor is to convert the model assigned hourly traffic volume to daily volume. The factor set has a generic set and categorized set. Both sets can be used according to the study purpose.
### All Class
AM | MD | PM
-- | -- | --
3.68 | 9.20 | 3.11

### By Category
Class | AM | MD | PM
-- |-- | -- | --
SOV | 3.44 | 8.41 | 3.95
HOV | 1.51 | 8.58 | 5.32
SOV+HOV | 3.22 | 8.63 | 4.05
LGV | 3.59 | 5.63 | 6.17
HGV | 4.88 | 5.43 | 6.36
LGV+HGV | 3.83 | 5.81 | 6.63

### Transit Ridership
The transit expansion factor converts the hourly transit ridership to daily value. Like auto traffic, the factor set is classed by different types of service. The value shows below. (*SeaBus has the same factor with Rail)

Transit mode | AM | MD | PM
-- |-- | -- | --
Bus | 2.54 | 9.44 | 2.57
SkyTrain | 2.53 | 9.54 | 2.92
WCE | 3.34 | - | 2.02

matrix
ensembles

