# Betting Simulator

### README 中文 | [English](README.md)

测试赌博算法的获利性的模拟器

## Idea的来源
几年前， 有一天和一个朋友聊天，得知他使用一套算法已经通过赌球赚了几千刀。他的算法简单来说就是一旦输了，下一场就加倍赌注，通过这种方法来达到cover之前的损失。算法背后的assumption是，每一场的输赢都是独立事件，这样n次连续输球的概率就是p(输球概率)^n. 其中只要有一次是赢的，之前的全部损失都可以弥补，甚至有时可以小赚，因为连续n次输球的概率是比较小的。

之后在一次饭桌上，另一个朋友又和我说了类似的算法，不过他不是赌球而是线上赌博。一开始赚了些钱，但是后面都输掉了。我当时分析觉得，线上赌博不靠谱，因为赔率都是可以后台设定的，这并不能说明这个算法不行。

又过一年，终于4年一度的世界杯来了。各种巧合下我也开了一个TAB账号，开始了我的赌球之旅。先说一下战绩吧。 从6月17号开始，100刀的初始资金，到7月8号为止，账面上balance是168.85刀，收益率是68.85%。

在不到一个月的时间里面，基本上每天都会下注，操作还是比较频繁的。每次下注的金额都不大，基本都是本金的10%左右，所以每次赚得也不多。因为比起赚了多少钱，我更在意的是验证这个算法到底能不能保证稳定的正收益。不要小看68%的收益率，如果1个月能有稳定50%的增长，那么一年后，本金的增长就是（1+0.5）^12, 也就是接近130倍！这样一年后100刀就变成1.3w刀，三年后就是218,416,400 :money_mouth_face::money_mouth_face::money_mouth_face:。感觉财富自由就在招手有没有！
但是还是觉得哪里不对，因为这个too good to be true了。 但是具体哪里不对又一时看不出来。于是我产生了用程序来验证这套算法获利性的想法。


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
