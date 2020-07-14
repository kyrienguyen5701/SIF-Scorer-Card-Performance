import get_data as src
import json

for i in range(2456):
    card = src.getDataByID(i + 1)
    if card != 'This is a N card' and card['skill_effect_type'] == 11: #scorer type
        with open('Data_Dump/{}.json'.format(i + 1), 'w') as data_file:
            json.dump(card,data_file, ensure_ascii=False, indent=4)

