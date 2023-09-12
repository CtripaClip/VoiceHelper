import os
import random
import speech_recognition
from customtkinter import *

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

app = CTk()
app.geometry("600x800")

commands_dict = {
    'commands': {
        'greeting': ['привет', 'приветствую'],
        'create_task': ['добавить задачу', 'создать задачу', 'заметка'],
    }
}

# class UnknownValueError:
#     """Create Error class"""
#     speech_recognition.UnknownValueError

def listen_command():
    """The function will return the recognized command"""

    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            
        return query
    except speech_recognition.UnknownValueError:
        return 'не понял что ты сказал :/'                                                                                                  


def greeting():
    """Greeting function"""
    
    return 'Привет!'


def create_task():
    """Create a todo task"""
    
    print('Что добавим в список дел?')
    
    query = listen_command()
        
    with open('todo-list.txt', 'a') as file:
        file.write(f'{query}\n')
        
    return f'Задача {query} добавлена в todo-list!'


class Main:

    def main():
        query = listen_command()
        
        for k, v in commands_dict['commands'].items():
            if query in v:
                print(globals()[k]())

    b_voice = CTkButton(master=app, text="Voice", command=main).place(relx= 0.5, rely= 0.5, anchor=CENTER)

    app.mainloop()

if __name__ == '__main__':
    import message
    Main