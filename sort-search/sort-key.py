import random
import copy

class User(object):
    # def __init__(self):
    #     self.name = ''
    #     self.surname = ''
    #     self.phone = -1

    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __repr__(self):
        l = ['name: {}'.format(self.name)]
        l.append('surname: {}'.format(self.surname))
        l.append('phone: {}'.format(self.phone))
        return '|'.join(l)

    def __eq__(self, other):
        return self.name == other.name




if __name__ == '__main__':
    # user_list = [User() for _ in xrange(10)]
    user_list = []
    for i in xrange(10):
        # user_list[i].name = ''.join([chr(random.randint(97, 122)) for _ in xrange(10)])
        # user_list[i].surname = ''.join([chr(random.randint(97, 122)) for _ in xrange(10)])
        # user_list[i].phone = random.randint(1111, 9999)
        name = ''.join([chr(random.randint(97, 122)) for _ in xrange(10)])
        surname = ''.join([chr(random.randint(97, 122)) for _ in xrange(10)])
        phone = random.randint(1111, 9999)
        u = User(name, surname, phone)
        # user_list.append(copy.deepcopy(u))
        # user_list.append(User(name, surname, phone))
        user_list.append(u)
        # print user_list[-1]
    print user_list

    print sorted(user_list, key=lambda u: (u.phone))