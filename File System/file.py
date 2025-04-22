from abc import abstractmethod
from collections import deque
class File:
    def __init__(self, name, extension_type, size):
        self._name = name
        self._extension_type = extension_type
        self._size = size


class Filter:
    @abstractmethod
    def match(self, value):
        pass

class NameFilter(Filter):
    def __init__(self, name):
        self.name = name
    
    def match(self, file: File):
        return file._name == self.name
    
class SizeFilter(Filter):
    def __init__(self, properties):
        self.size = properties[0]
        self.equivalance = properties[1]
    
    def match(self, file: File):
        return eval(str(file._size) + self.equivalance + str(self.size))

class ExtensionFilter(Filter):
    def __init__(self, extension_type):
        self.extension_type = extension_type
    
    def match(self, file: File):
        return file._extension_type == self.extension_type

class ANDFilter:
    def __init__(self, filters):
        self.filters = filters
    
    def match(self, file):
        matched_files = [instance.match(file) for instance in self.filters]
        return all(matched_files)

class ORFilter:
    def __init__(self, filters):
        self.filters = filters
    
    def match(self, file):
        matched_files = [instance.match(file) for instance in self.filters]
        return any(matched_files)


class FileSystem:
    def __init__(self, directory_name, subdirectories = [], files = []):
        self.directory_name = directory_name
        self.subdirectories = subdirectories
        self.files = files

class Search:
    def __init__(self, directory, filter_name, operator):
        self.directory = directory
        self.filter_name = filter_name
        self.operator = operator

    def file_search(self):
        FILTER_MAP = {
            "NameFilter": NameFilter,
            "ExtensionFilter": ExtensionFilter,
            "SizeFilter": SizeFilter,
        }

        OPERATOR_MAP = {
            "And" : ANDFilter,
            "Or": ORFilter
        }

        filters = []
        for filter_name, value in self.filter_name.items():
            f = FILTER_MAP.get(filter_name)
            if f:
                filters.append(f(value))

        operator = OPERATOR_MAP.get(self.operator)(filters)
        print(operator)
        q = deque([self.directory])
        res = []
        while q:
            curr = q.popleft()
            for file in curr.files:
                if operator.match(file):
                    res.append(file._name)
            for d in curr.subdirectories:
                q.append(d)
            
        return res

if __name__ == "__main__":
    resume = File("Resume", "pdf", 10)
    cover_letter = File("Cover_Letter", "pdf", 12)
    job_search = FileSystem("Job Search", [], [resume, cover_letter])

    transcript = File("Transcript", "docx", 15)
    school = FileSystem("School", [job_search], [transcript])

    python = File("LLD", "py", 4)
    java = File("Java Classes", "java", 20)
    root = FileSystem("/", [school], [python, java])

    result = Search(root, {"ExtensionFilter": "py", "SizeFilter": [10, "<="]}, "And").file_search()
    print(result)