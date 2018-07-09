# read file & store necessay data
filename_r = '../betting data/afl.csv'

raw_match_results = []
with open(filename_r, 'r') as fr:
    for line in fr:
        cols = line.split(",")
        score_home = cols[5]
        score_away = cols[6]
        odd_home  = cols[12]
        odd_away = cols[13]
        raw_match_results.append({"score_home":score_home, "score_away":score_away, "odd_home":odd_home, "odd_away":odd_away})


print(raw_match_results)
# process data and generate needed data ((1)win/loss (2)odds (3)odd_a (4)odd_b)
processed_match_results = []
for match_result in raw_match_results:
    try:
        odd_ratio = float(match_result['odd_home'])/float(match_result['odd_away'])
    except:
        continue
    else:
        if int(match_result['score_home']) > int(match_result['score_away']):
            processed_match_results.append({"home_result":"win", "odd_ratio":odd_ratio, 'odd_home':match_result['odd_home'], 'odd_away':match_result['odd_away']})
        else:
            processed_match_results.append({"home_result":"loss", "odd_ratio":odd_ratio, 'odd_home':match_result['odd_home'], 'odd_away':match_result['odd_away']})

print(processed_match_results)
# store into a file
filename_w = '../betting data/processed result/processed_result.csv'
with open(filename_w, "w") as fw:
    for match_result in processed_match_results:
        fw.write("{},{},{},{}\n".format(match_result['home_result'],
                                        match_result['odd_ratio'],
                                        match_result['odd_home'],
                                        match_result['odd_away']))
