import os

client_id = ''
client_secret = ''

sync_dic = {}

def load_data():
    global client_id
    global client_secret
    global sync_dic

    #load spotify api keys
    try:
        with open("keys.txt", 'r') as file:
            lines = file.readlines()
            client_id = lines[0].strip()
            client_secret = lines[1].strip()
        
        if client_id == "[CLIENT-ID]":
            client_id = ''
        else:
            print(f"Loaded client_id: ...{client_id[-5:]}\nLoaded client_secret: ...{client_secret[-5:]}\n ")
    except:
        print("Failed to load keys")

    #load playlists
    try:
        with open("lists.txt", 'r') as file:
            lines = file.readlines()
            for l in lines:
                l = l.strip()
                link, name = l.split(' - ')
                print(f"Loaded {name}")
                sync_dic[link] = name

        print(f'\nLoaded {len(sync_dic)} lists.')
    except:
        print("Error loading lists")

    return sync_dic
    

def make_sync():
    for link, folder in sync_dic.items():

        #check if created sync. We do this checking if the folder exist.
        if not os.path.exists(folder):
            os.makedirs(folder)  # Creates the directory if it doesn't exist
            print(f"Sync for '{folder}' created. Created folder.")

            #create sync command
            make_tmplt = 'spotdl sync [link] --save-file "[folder].spotdl" --output "[folder]/0{list-position} - {title}, {artist}"'
            if client_id != "":
                make_tmplt +=f' --client-id {client_id} --client-secret {client_secret}'
            make_tmplt = make_tmplt.replace('[link]', link)
            make_tmplt = make_tmplt.replace('[folder]', folder)

            os.system(make_tmplt)
        else:
            print(f"Sync for '{folder}' already exists.")

def update_sync():
    for link, folder in sync_dic.items():
        one_sync(link, folder)

def one_sync(link, folder):
    #call the update sync command, after checking that is here.

    path = f"{folder}.spotdl"
    Found = False
    try:
        with open(path, 'r') as path:
            print(f"Found {folder} sync file, starting sync")
            Found = True
    except:
        print(f"Can't find {folder} sync file. Please use make sync")
    
    if Found:
        #create sync command
        sync_tmplt = 'spotdl sync [link] --save-file "[folder].spotdl" --output "[folder]/0{list-position} - {title}, {artist}"'
        if client_id != "":
            sync_tmplt +=f' --client-id {client_id} --client-secret {client_secret}'
        sync_tmplt = sync_tmplt.replace('[folder]', folder)
        os.system(sync_tmplt)
            
def mult_choice(quest, choices):
    print(f'>>> {quest}\n')
    for i in range(len(choices)):
        print(f'[{i + 1}] - {choices[i]}')
    
    r = input("\n>>> ")
    try:
        return int(r) - 1
    except:
        return None


def test_spotdl():
    os.system("spotdl")

if __name__ == '__main__':
    load_data()
    print('\n...\n')
    main_options = ["Full - Make + Sync", "Make Remaing", "Sync All", "Sync Specific"]

    main = mult_choice("Welcome to the Lucho Tech SpotDL automation! Please select an option", main_options)

    if main == None:
        exit(0)  

    if main == 0:
        make_sync()
        update_sync()

    if main == 1:
        make_sync()

    if main == 2:
        update_sync()

    if main == 3:
        names = []
        for u, n in sync_dic.items():
            names.append(n)
        
        p = mult_choice("Select a playlist to update: ", names)

        one_sync(list(sync_dic.items())[p][0], list(sync_dic.items())[p][1])
        
