import os
import subprocess
import donwloader

folders = []
sync_dic = donwloader.load_data()

for u, n in sync_dic.items():
    folders.append(n)

import os

current_folder = os.path.dirname(os.path.abspath(__file__))
print(f"\nRunning on {current_folder}...\n\n")

default_paths = ["E:\\musica\\", "E:\\spotdl\\", "F:\\musica\\", "F:\\spotdl\\"]
default_paths.append("Phone (via ADB)")
default_paths.append("Custom...")

c = donwloader.mult_choice("Select an output path:", default_paths)

use_adb = False

if c == len(default_paths) - 2:
    use_adb = True
    destination_folder = "/storage/9EEE3192EE3163A5/musica/"
    os.system(f'adb shell ls {destination_folder}')
    input("press any to continue")
elif c == len(default_paths) - 1:
    destination_folder = input("Enter output path: ")
else:
    destination_folder = default_paths[c]

for fld in folders:
    print(f"\nUpdating files in: {fld} ...")

    if use_adb:
        # Listar archivos actuales en el destino del móvil
        try:
            result = subprocess.check_output(['adb', 'shell', 'ls', f'{destination_folder}{fld}'], stderr=subprocess.DEVNULL, encoding='utf-8')
            destination_files = result.strip().split('\n')
        except subprocess.CalledProcessError:
            # Si no existe la carpeta, la creamos
            subprocess.run(['adb', 'shell', 'mkdir', '-p', f'{destination_folder}{fld}'])
            destination_files = []
        original_files = os.listdir(f'{current_folder}{fld}')
        destination_ok = []
        operations = 0

        for f in original_files:
            if f not in destination_files:
                print(f'Pushing {f} to {destination_folder}{fld}')
                subprocess.run(['adb', 'push', f'{current_folder}{fld}\\{f}', f'{destination_folder}{fld}/'])
                operations += 1
            else:
                destination_ok.append(f)

        for f in destination_files:
            if f not in destination_ok:
                print(f'Deleting {f} from phone')
                subprocess.run(['adb', 'shell', 'rm', f'{destination_folder}{fld}/{f}'])
                operations += 1

        if operations == 0:
            print("Everything ok!")

    else:
        if not os.path.exists(f'{destination_folder}{fld}'):
            os.makedirs(f'{destination_folder}{fld}')
        original_files = os.listdir(f'{current_folder}{fld}')
        destination_files = os.listdir(f'{destination_folder}{fld}')
        destination_ok = []
        operations = 0

        for f in original_files:
            if f not in destination_files:
                print(f'Copying {f} to {destination_folder}{fld}\\{f}')
                command = f'copy "{current_folder}{fld}\\{f}" "{destination_folder}{fld}"'
                os.system(command)
                operations += 1
            else:
                destination_ok.append(f)

        for f in destination_files:
            if not f in destination_ok:
                print(f"Deleting {f} from {destination_folder}{fld}")
                os.system(f'del "{destination_folder}{fld}\\{f}"')
                operations += 1

        if operations == 0:
            print("Everything ok!")
