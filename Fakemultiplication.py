class Rohan:
    def __init__(self,num):
        self.num = num

    def multipleof(self):
        '''This function will return multiplication of given number but will return wrong calculation for any 1 num from 1 - 10 '''
        resultStore = []
        for i in range(1, 11):
            resultStore.append(self.num*i)
        choosing_oneNum = choice(resultStore)
        replacing_wrongval = choosing_oneNum + 3
        index_num = resultStore.index(choosing_oneNum)
        resultStore.insert(index_num, replacing_wrongval)
        del resultStore[index_num+1]
        return resultStore

    def isCorrect(self, wrong_multi):
        ''' This function will return correct multiplication of any num given by user '''
        correct_resultStore = []
        for i in range(1, 11):
            correct_resultStore.append(self.num*i)
        print(correct_resultStore)
        #this list stores the index where the rohan's multiplication gave wrong calculation
        new_list = []
        for i in range(len(correct_resultStore)):
            if correct_resultStore[i] != wrong_multi[i]:
                    new_list.append(i)
        return f'Rohan multiplication function has wrong calculation in {new_list[0]}' \
               f' index(Note: The index starts from 0).\nInstead of {wrong_multi[new_list[0]]}, the ' \
               f'value should be {correct_resultStore[new_list[0]]}.'


if __name__ == '__main__':
    from random import choice
    user = int(input("Give the number:"))
    r = Rohan(user)
    rohan_wrongTable = r.multipleof()
    print(rohan_wrongTable)
    correct_multi = r.isCorrect(rohan_wrongTable)
    print(correct_multi)


