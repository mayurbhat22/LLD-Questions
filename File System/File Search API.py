from collections import deque
class File:
    def __init__(self, name, size, file_type):
        self.name = name
        self.size = size
        self.file_type = file_type

class Directory:
    def __init__(self, name:str, subdirectories:list = [], files:list = []):
        self.name = name
        self.subdirectories = subdirectories
        self.files = files
    
    def add_files(self, file):
        self.files.append(file)
    
    def add_subdirectory(self, directory):
        self.subdirectories.append(directory)

class Filter:
    def match(self, file):
        pass

class NameFilter(Filter):
    def __init__(self, name):
        self.name = name
    
    def match(self, file):
        return file.name.lower() == self.name.lower()

class SizeFilter(Filter):
    def __init__(self, size):
        self.size = size
    
    def match(self, file):
        return file.size == self.size

class FileTypeFilter(Filter):
    def __init__(self, file_type):
        self.file_type = file_type
    
    def match(self, file):
        return self.file_type.lower() == file.file_type.lower()

class ANDFilter(Filter):
    def match(self, filter_class, file):
        return all([filter.match(file) for filter in filter_class])

class ORFilter(Filter):
    def match(self, filter_class, file):
        return any([filter.match(file) for filter in filter_class])

class Search:
    def __init__(self, filter_dict):
        self.initial_directory = filter_dict["starting_folder"]
        self.filters = filter_dict["filters"]
    
    def find(self):
        filters = {
            "name": NameFilter,
            "size": SizeFilter,
            "extension": FileTypeFilter
        }
        logic_filter = {
            "OR": ORFilter(),
            "AND": ANDFilter()
        }
        filter_class = []
        logic_filters = []
        for filter_name, value in self.filters.items():
            if filter_name in filters:
                filter_class.append(filters[filter_name](value))
            if value in logic_filter:
                logic_filters.append(logic_filter[value])
        
        res = set()
        root = self.initial_directory

        q = deque([root])

        while q:
            curr_dire = q.popleft()

            for file in curr_dire.files:
                if logic_filters[0].match(filter_class, file):
                    res.add(file.name)

            for dir in curr_dire.subdirectories:
                q.append(dir)
        
        return res


    
if __name__ == "__main__":
   resume =  File("Resume", 12000, "pdf")
   cover_letter = File("Cover Letter", 10000, "pdf")
   job_search = Directory("Job Search", [], [resume, cover_letter])

   transcript = File("Transcript", 5000, "DOC")
   root = Directory("/", [job_search], [transcript])
   res = Search({
    "starting_folder": root,
    "filters": {
        "name": "Resume",
        "extension": "DOC",
        "logic": "OR"
    }
}).find()
   print(res)

# Root
# -- transcript.doc
# -- Job Search
#     -- Resume.pdf
#     -- Cover Letter.pdf

# {
#     "starting_folder": "root",
#     "filters": {
#         "name": "Resume",
#         "extension": "pdf"
#     }
# }