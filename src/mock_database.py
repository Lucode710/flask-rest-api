from .prize import Prize
from src.exceptions import *

data = {
            1: [
                Prize(1, "Prize 1", "Description of prize 1", "https://example.com/image1.png"),
                Prize(2, "Prize 2", "Description of prize 2", "https://example.com/image2.png"),
                Prize(3, "Prize 3", "Description of prize 3", "https://example.com/image3.png"),
                Prize(4, "Prize 4", "Description of prize 4", "https://example.com/image4.png"),
                Prize(5, "Prize 5", "Description of prize 5", "https://example.com/image5.png"),
                Prize(6, "Prize 6", "Description of prize 6", "https://example.com/image6.png"),
            ],
            2: [
                Prize(10, "Prize 10", "Description of prize 10", "https://example.com/image10.png"),
                Prize(11, "Prize 11", "Description of prize 11", "https://example.com/image11.png"),
                Prize(12, "Prize 12", "Description of prize 12", "https://example.com/image12.png"),
            ],
        }

class MockDatabase:

    @staticmethod
    def get_prizes(catalog_id, filter=None, pagination=None):
        if catalog_id not in data:
            raise CatalogNotFound()

        filtered_prizes = data[catalog_id]

        if filter:
            if 'id' in filter:
                filtered_prizes = [prize for prize in filtered_prizes if prize.id == int(filter['id'])]
            if 'description' in filter:
                filtered_prizes = [prize for prize in filtered_prizes if filter['description'].lower() in prize.description.lower()]


        if pagination:
            page = pagination.get('page')
            per_page = pagination.get('per_page')
            start = (page - 1) * per_page
            end = start + per_page
            filtered_prizes = filtered_prizes[start:end]

        total = len(filtered_prizes)

        return total, filtered_prizes