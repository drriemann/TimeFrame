import sys
from schedule_table import db, TimeFrame
from csv2tf import data


def create_true_tf():
    for e in data:
        time = TimeFrame(timef=e[0],
                         monday=e[1],
                         tuesday=e[2],
                         wednesday=e[3],
                         thursday=e[4],
                         friday=e[5],
                         saturday=e[6])
        db.session.add(time)
    db.session.commit()
    print(f'done.')


if __name__ == '__main__':
    create_true_tf()
