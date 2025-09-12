import os
import shutil

def manager():
    choice = input("1. Import .py file from internal storage\n2. Run existing .py file in Termux\nChoose option: ")
    home = os.path.expanduser("~/")
    if choice == "1":
        fname = input("Enter .py file name: ")
        path = "/storage/emulated/0"
        target = None
        for root, dirs, files in os.walk(path):
            if fname in files:
                target = os.path.join(root, fname)
                break
        if not target:
            print("File not found")
            return
        DST = os.path.join(home, fname)
        shutil.copy(target, DST)
        if input("Rename file? (y/n): ").lower() == "y":
            rename = input("Enter new name: ")
            newDST = os.path.join(home, rename)
            os.rename(DST, newDST)
            DST = newDST
        if input("Run file now? (y/n): ").lower() == "y":
            os.system(f"python {DST}")
    elif choice == "2":
        files = [f for f in os.listdir(home) if f.endswith(".py")]
        for i, f in enumerate(files, 1):
            print(f"{i}. {f}")
        sel = input("Select file number to run: ")
        if sel.isdigit() and 1 <= int(sel) <= len(files):
            os.system(f"python {files[int(sel)-1]}")

if __name__ == "__main__":
    manager()