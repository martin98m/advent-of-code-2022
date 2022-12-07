class Folder:
    def __init__(self, name, parent):
        self.name, self.files, self.parent = name, {}, parent

    def get_size(self):
        folder_sizes.append(folder_size:=sum(ff.get_size() for ff in self.files.values()))
        return folder_size

class File:
    def __init__(self, string):
        idk = string.split()
        self.name, self.size = idk[1], int(idk[0])

    def get_size(self):
        return self.size

#instructions = open('test.txt', 'r', encoding='utf-8').read().splitlines()
instructions = open('input.txt', 'r', encoding='utf-8').read().splitlines()

filesystem, folder_sizes = Folder('idk', None), []
filesystem.files['/'] = Folder('/', filesystem)
path = filesystem
for i, line in enumerate(instructions):
    if line.startswith('$ cd ..'):
        path = path.parent
    elif line.startswith('$ cd'):
        path = path.files[line[5:]]
    elif not line.startswith('$ ls'):
        if instructions[i].startswith('dir'):
            path.files[instructions[i][4:]] = Folder(instructions[i][4:], path)
        else:
            path.files[instructions[i]] = File(instructions[i])

root_size = filesystem.files['/'].get_size()
print('P1> ', sum(filter(lambda x: x < 10e4, sorted(folder_sizes))))
print('P2> ', list(filter(lambda x: x >= (30e6 - (70e6-root_size)), sorted(folder_sizes)))[0])
