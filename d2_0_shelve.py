from __future__ import print_function
import shelve

shelve_storage = shelve.open('shelve_storage',
                             writeback=True)  # just a name


if 'count' in shelve_storage:
    shelve_storage['count'] += 1
else:
    shelve_storage['count'] = 1

message = "The Programe is opened for {} times"
print(message.format(shelve_storage['count']))


shelve_storage.close()
