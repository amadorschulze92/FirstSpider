from sqlalchemy.orm import sessionmaker
from models import People, db_connect, create_deal_table

class SpiderPipeline(object):
    """Livingsocial pipeline for storing scraped items in the database"""
    def __init__(self):
        """Initializes database connection and sessionmaker.
        Creates deal table.
        """
        engine = db_connect()
        create_deal_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save people in the database.
        This method is called for every item pipeline component.
        """
        session = self.Session()
        people = People(**item)

        try:
            session.add(people)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item