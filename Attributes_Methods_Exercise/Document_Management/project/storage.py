class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = [x for x in self.categories if x.id == category_id][0]
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [x for x in self.topics if x.id == topic_id][0]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = [x for x in self.documents if x.id == document_id][0]
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = [x for x in self.categories if x.id == category_id][0]
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [x for x in self.topics if x.id == topic_id][0]
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [x for x in self.documents if x.id == document_id][0]
        self.documents.remove(document)

    def get_document(self, document_id):
        document = [x for x in self.documents if x.id == document_id][0]
        return document

    def __repr__(self):
        for x in self.documents:
            return x.__repr__()


# from Python_OOP.Attributes_Methods_Exercise.Document_Management.project.category import Category
# from Python_OOP.Attributes_Methods_Exercise.Document_Management.project.document import Document
# from Python_OOP.Attributes_Methods_Exercise.Document_Management.project.topic import Topic
#
#
# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)
