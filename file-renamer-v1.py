import os

def batch_rename_files(folder_path, base_name):
    try:
        # Izveido masīvu ar visiem failu nosaukumiem un sakārto alfabētiski
        files = sorted(os.listdir(folder_path))

        files_amount_in_folder = len(files)

        # Iesāk kaunteri
        counter = 1

        # Iziet cauri katram faila nosaukumam masīvā
        for filename in files:

            # Sadala faila nosaukumu un paplašinājumu, name mainīgais netiks izmantots, bet tas jāpaņem no funkcijas
            name, ext = os.path.splitext(filename)

            # Uztaisa pilnu path vecajam faila nosaukumam
            old_path = os.path.join(folder_path, filename)

            # Uztaisa jaunu faila nosaukumu ar kaunteri un paplašinājumu
            new_name = f"{base_name}-{counter}{ext}"

            # Uztaisa pilnu path jaunajam faila nosaukumam
            new_path = os.path.join(folder_path, new_name)

            # Palielina kaunteri par 1
            counter += 1

            # Pārsauc failu
            os.rename(old_path, new_path)
            print(f"File {filename} renamed to {new_name} successfully.")

        return counter -1, files_amount_in_folder # funkcija atgriež vērtības par to cik faili bija folderī un cik ir nomainīti
    
    except FileNotFoundError:
        print(f"Folder {folder_path} not found.")
    
    except PermissionError:
        print(f"You don't have permissions to rename files in {folder_path}")

# User input
def get_user_inputs():
    folder_path = input("Enter the folder path: ")
    base_name = input("Enter the base name for filenames: ")
    print(f"All the files in {folder_path} will be renamed to <{base_name}-#>")

    approved = input("Do you want to proceed? Y/N?")
    if approved == "Y" or approved == "y":
        return folder_path, base_name
    else:
        print("Batch renaming cancelled!")
        exit()


# global scope

if __name__ == "__main__": # kods zem šīs rindas izpildīsies tikai no šī dokumenta, bet ne tad, ja to importēs citā dokumentā kā moduli

    print("This is a script for batch renaming all files in a folder!")

    # nodefinē global scope mainīgos no user input funkcijas atgrieztajām vērtībām
    folder_path, base_name = get_user_inputs()

    # izsauc galveno funkciju un paņem funkcijas atgrieztās vērtības uz global scope
    files_renamed, total_files = batch_rename_files(folder_path, base_name) 
    
    print(f"Renamed {files_renamed} out of {total_files} files successfully!")
