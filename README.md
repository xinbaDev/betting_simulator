# Betting Simulator

### README English | [中文](README.zh.md)

Betting Simulator is a program that aims at helping people study different betting strategies.

## Where the idea comes from?

A few years ago, a friend of mine told me he earned a few thousand dollars from betting with the help from his algorithm. The algorithm, simply speaking, was --- once a gambler lost a bet, the betting amount for the next round would be doubled, through which the lost from the previous game could be covered. The assumption behind this algorithm was every single bet was an independent incident, therefore the probability of losing continuously for n times was P(lose)^n. As soon as the gambler won a bet, all lose could all be covered , or even earned a few more coins because the possibility of losing continuously for n times was relatively low.

Another friend told me a similar algorithm when we had lunch together. The only difference would be he was doing online gambling rather than betting with this algorithm.  He earned a bit at the beginning but lost all his money at the end. My thought at that time was online gambling was irrational because the betting rate could be set artificially but it did not mean the algorithm could not be applied.

One year later, the World Cup held every 4 years finally arrived. I opened a TAB account by chance, beginning my journey of betting. Let’s get started from my achievement. From 17th June, the initial investment was $100 and the final balance displayed in my account on 8th July was $168.85, with the rate of return of 68.85%.

Within less than a month, I kept betting frequently almost every single day. Every single bet was not huge, basically around 10% of the principal, therefore I did not earn much from a single bet. The thing that I cared about was whether the algorithm was effective or not rather than making profit. Don’t look down on the 68% return rate. If there is a 50% steady increase for every month, then after one year, the principal will be (1+0.5）^12, which is 130 times! Hence the initial $100 becomes $13K after a year, which will turn out to be $218,416,400 🤑🤑🤑 in three years.
It feels like the financial independence is waving at you, doesn’t it? However, something deep inside tells me that something is a bit weird, because it is too good to be true. But I can’t tell what’s wrong, so I come up with an idea to verify the profitability of this algorithm using programming.


## Installation
```
pip3 install -r requirements.txt
```

## Usage
1. Download this project to local and point Mac Terminal or Windows Command Line to the project folder. E.g:
```
cd /betting/
```
2. Run the program by executing this command:
```
python3 start.py
```
or
```
python start.py
```

## Configuration
This program stores and reads your settings in _config.py_. Modify values in the following files to manipulate the program behaviour.

### betting_data_settings
This setting stores betting data config for the program.

| Key | Description | Example |
| --- | --- | --- |
| shuffle | whether to shuffle betting data | True |



### betting_settings
This setting stores betting config for the program.

| Key | Description | Example |
| --- | --- | --- |
| strategy | the name of the strategy to be used | double_betting_after_lossing |
| initial_money | the initial money before betting | 10000 |
| initial_bet | the initial money for first betting| 100 |



### visualization_setting
This settings stores visualization information.

| Key | Description | Example |
| --- | --- | --- |
| plugin | the visualization plugin name | money_history |
| title | the title of the generated picture | betting history |
| file | the destination to store the image file| \simulation_result\visualization\double_betting_after_lossing.html |
