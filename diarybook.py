class Diary:
    last_id = 0

    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        Diary.last_id += 1
        self.id = Diary.last_id

    def match(self, keyword):
        return keyword in self.memo or keyword in self.tags

class Diarybook:
    def __init__(self):
        self.diaries = []

    def new_diary(self, memo, tags=''):
        self.diaries.append(Diary(memo, tags))

    def search_diary(self, keyword):
        filtered_diaries = [diary for diary in self.diaries if diary.match(keyword)]
        return filtered_diaries

    def get_diary_by_id(self, diary_id):
        for diary in self.diaries:
            if diary.id == diary_id:
                return diary
        return None
