class PigLatinMaker(object):
    '''Turn a sentence into fake latin.'''
    sentence = None

    def __init__(self,input):
        self.sentence = input


    def pig_latin(self):
        latin = ''

        if len(self.sentence) > 0:
            for word in sentence.lower().split(): 
                latin += word[ 1:]  + word[0] + 'ay '
                print(latin.capitalize())
        else:
            print('Oh no! An error happened.' 
            )
    
    def original(self):
        print(self.sentence)


if __name__ == '__main__':
    #you can run this file from terminal by typing python linting_example_2.py
    # note: if you are using python2, you will need to change the method input() below to raw_input()
    sentence = input('Please enter a sentence! ')

    print('Generating pig latin...')

    maker = PigLatinMaker(sentence)
    maker.pig_latin()
