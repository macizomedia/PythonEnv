# glob stands for global wildcard expansion
import csv
from typing import NamedTuple, DefaultDict, List, Dict
from pprint import pprint
import glob

Senator = NamedTuple('Senator', [('name', str), ('state', str),
                                 ('party', str)])
VoteValue = int
voteCount = DefaultDict(list)  # type: DefaultDict[Senator, List[VoteValue]]
vote_value = {
    'Yea': 1,
    'Nay': -1,
    'Not Voting': 0
}  # type: Dict[str, VoteValue]

# with open('congress_votes_117-2022_h463.csv', encoding='utf-8') as csv_file:

for filename in glob.glob('Datasets/*.csv'):
    with open(filename, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        topic = next(csv_reader)
        headers = next(csv_reader)
        for code, state, district, vote, name, party in csv_reader:
            senator = Senator(name, state, party)
            voteCount[senator].append(vote_value[vote])

record = {senator: tuple(votes) for senator, votes in voteCount.items()}

print(record)
