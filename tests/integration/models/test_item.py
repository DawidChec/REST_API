from models.item import ItemModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context:
            item = ItemModel('test', 19.99)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              f"Found an item name {item}, but expected not to.".format(item.name))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'),
                              f"Did not found an item name {item}, but expected to do.".format(item.name))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'),
                              f"Found an item name {item}, but expected not to.".format(item.name))