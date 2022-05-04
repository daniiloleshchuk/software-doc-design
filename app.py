from db import init_db
from utils import write_from_csv_to_db, generate_csv

if __name__ == '__main__':
    init_db()
    generate_csv('input_data.csv')
    write_from_csv_to_db('input_data.csv', ['User', 'Story', 'Message', 'StoryReaction'])
