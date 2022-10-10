import re
def read_template(path):
    '''
    function that takes in a path to text file and returns a stripped string of the file's contents.
    '''

    try:
       with open(path,'r') as f :
        result = f.read() 
        return result

    except:
        raise FileNotFoundError

def parse_template (text):
    '''
     function that takes in a template string and returns a string with language parts removed and a separate tuple of those language parts.
    '''
    regex = "{(.*?)}"
    words  = re.findall(regex, text)
    new_txt = re.sub('{.+?}', '{}', text)  
    return new_txt,(tuple)(words) 

def  merge(stripped, words):

     '''
    function takes two arguments ; one is str with empty curly brackets,
    and the values that will be inside the curly bracket.
    and return the string with values instead of empty curly brackets.
    '''
     return stripped.format(*words)    

def main_madllib ():
    path_file = 'assets/make_me_a_video_game_template.txt'
    contant= read_template(path_file)
    stripped , word = parse_template(contant)
    input_value=[]
    for i in word :
        input_words=input(f'plz inter {i} =>')
        input_value.append(input_words)
    new_txt= merge(stripped,input_value)    
    print(new_txt)
    path = 'assets/madlib.txt'
    with open(path, 'w') as f:
       f.write(new_txt)
       print('Your txt has been saved')
   
    return new_txt

    
   

if __name__ == '__main__':

 wellcome = '''
**************************************
**    Welcome to the MadLib game!   **
**   Madlib is a game where you     **
**  decide the parts of the story   **
**   
**    Add your  words to            **
**    create a funny story by       **
**    answering the question        **
**    and press enter...            **
**************************************
'''
 print(wellcome)
 main_madllib()
