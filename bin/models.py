from discogs_client import Release
from PyQt6.QtCore import QStringListModel, Qt, QAbstractTableModel, QModelIndex
import pprint

class ListModelSearchResult(QStringListModel):

    def __init__(self):
        super().__init__()
        self.titles = []
        self.ids = []

    def get_id(self, index):
        print(self.ids)
        if(index == -1):
            return 0
        return self.ids[index]

    def clear_search_result(self):
        self.titles = []
        self.ids = []

    def set_search_result(self, results):
        self.clear_search_result()
        for result in results:
            #pprint.pprint(vars(result))
            self.titles.append(result.title + " : " + str(result.id) + " [" + str(result.year) + "]")
            self.ids.append(result.id)
        self.setStringList(self.titles)

class TableModelTracklist(QAbstractTableModel):

    COLUMN_DICT = {'#':0, 'Title':1, 'Duration':2}

    def __init__(self, release_data : Release, init : bool):
        super().__init__()
        self._release_data = release_data
        self._init = init

    def set_release_data(self, release_data : Release):
        self._release_data = release_data
        print(self._release_data.tracklist)

    def columnCount(self, parent: QModelIndex) -> int:
        if self._init:
            return 0
        return len(self.COLUMN_DICT)

    def rowCount(self, parent: QModelIndex) -> int:
        if self._init:
            return 0
        return len(self._release_data.tracklist)

    def get_release_data(self):
        return self._release_data
        
    def data(self, index: QModelIndex, role: int):
        row_index = index.row()
        col_index = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if col_index == self.COLUMN_DICT['#']:
                if self._init :
                    return ''
                return self._release_data.tracklist[row_index].position
            elif col_index == self.COLUMN_DICT['Title']:
                if self._init :
                    return ''
                return self._release_data.tracklist[row_index].title
            elif col_index == self.COLUMN_DICT['Duration']:
                if self._init :
                    return ''
                return self._release_data.tracklist[row_index].duration
            else:
                return "ERROR"
        if role == Qt.ItemDataRole.TextAlignmentRole:
            if index.column() in [0, 2]:
                return Qt.AlignmentFlag.AlignCenter
    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return list(self.COLUMN_DICT.keys())[section]