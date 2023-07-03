import pickle

# user_data = {
#     'save_path': '123'
# } 

def save_user_settings(data): 
    with open('data.pickle', 'wb') as f: 
        pickle.dump(data, f)
        print('Сохранил!')


def load_user_settings(): 
    with open('data.pickle', 'rb') as f: 
        data_new = pickle.load(f)
        print('Загрузил!')
        
        return data_new
    
# save_user_settings(user_data)
# data = load_user_settings()

# print(data)