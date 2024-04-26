import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import main  # Assuming main.py is in the same directory and the functions are imported correctly

# class Plugin_type():
#     def __init__(self, folder_path) -> None:
#         self.folder_path = folder_path
#         self.folder_name = folder_path.name

#     def __repr__(self) -> str:
#         return self.folder_name



base_path = None
type_vst_dict = None
selected_plugin_types = None
selected_plugin_types_name_mapping = {} #NOTE: current method does not allow for duplicate folder names.
selected_random_plugins = {}
selected_random_plugin_display_elements = []

def browse_folder():
    """ Open a dialog to select the base path and load subfolders into the listbox. """
    global base_path
    global type_vst_dict
    global selected_plugin_types_name_mapping
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        base_path = Path(folder_selected)
        subfolder_dict = main.load_plugin_folder(base_path)
        listbox_plugin_types.delete(0, tk.END)
        for subfolder in subfolder_dict.keys():
            # plugin_type = Plugin_type(subfolder)
            selected_plugin_types_name_mapping[subfolder.name] = subfolder
            listbox_plugin_types.insert(tk.END, subfolder.name) #was subfolder.name
        
        type_vst_dict = main.load_plugin_folder(base_path)
    btn_select_plugin_types.pack(side=tk.LEFT, padx=10)


def empty_selected_plugins():
    global selected_random_plugin_display_elements
    for element in selected_random_plugin_display_elements:
        # element.pack_forget()
        element.destroy()
    selected_random_plugin_display_elements = []

def select_random_plugin_per_type(type_vst_dict, selected_plugin_types : list[Path]):
    """ Display random plugin from each selected subfolder. """
    global selected_random_plugin_display_elements
    empty_selected_plugins()
    for plugin_type in selected_plugin_types:
        random_plugin = main.select_random_vst(type_vst_dict, selected_plugin_types_name_mapping[plugin_type])
        print(f"Random plugin from {plugin_type}: {random_plugin}") #TODO make element for each of the types
        selected_random_plugin_display_elements += [tk.Button(frame_plugins, text=f"{plugin_type}: {random_plugin.name}")] #add command/click&drag so i can drag the plugin to fl studio.
    # messagebox.showinfo("Random Plugins", result
    for element in selected_random_plugin_display_elements:
        element.pack()

def return_selected_plugin_types(listbox) -> None | list[Path]:
    global selected_plugin_types 
    empty_selected_plugins()
    if not listbox.curselection():
        messagebox.showinfo("Error", "Please select at least one folder.")
        return
    selected = []
    for i in listbox.curselection():
        selected += [listbox.get(i)]

    selected_plugin_types = selected

    btn_show_plugins.pack(side=tk.LEFT, padx=10)
    listbox_plugin_types.pack_forget()
    btn_select_plugin_types.pack_forget()
    btn_other_plugin_types.pack()
    frame_plugins.pack()

def back_to_plugin_type_selection():
    btn_select_plugin_types.pack()
    listbox_plugin_types.pack()
    btn_other_plugin_types.pack_forget()
    btn_show_plugins.pack_forget()
    frame_plugins.pack_forget()
    #TODO boxes met plugins verwijderen


# Setup the main window
root = tk.Tk()
root.title("Plugin Selector")

# Frame for folder selection
frame_folder = tk.Frame(root)
frame_folder.pack(pady=10)
btn_select_folder = tk.Button(frame_folder, text="Select Base Path", command=browse_folder)
btn_select_folder.pack(side=tk.LEFT, padx=10)

# Listbox for subfolders
listbox_plugin_types = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=15)
listbox_plugin_types.pack(pady=20)

btn_show_plugins = tk.Button(frame_folder, text="Show Random Plugins", command=lambda: select_random_plugin_per_type(type_vst_dict, selected_plugin_types))

# deze uitvoeren na selecteren types
btn_select_plugin_types = tk.Button(frame_folder, text="Select Plugin Types", command=lambda: return_selected_plugin_types(listbox_plugin_types), )
btn_other_plugin_types = tk.Button(frame_folder, text="Other Plugin Types...", command=lambda: back_to_plugin_type_selection(), )


#PLACEHOLDER: for now just show a textbox for each of the selected plugins. Make it so that when you drag it selects the plugin .fst
# Frame that displays the random plugins
frame_plugins = tk.Frame(root)


# Start the application
root.mainloop()
