# import hashlib

# def save_hash_to_file(file_path: str, log_file: str = "../static/Files/Outputs/hash_log.txt") -> str:
#     """Stores the file hash in a local log file for future integrity checks."""
#     try:
#         with open(file_path, "rb") as f:
#             file_hash = hashlib.md5(f.read()).hexdigest()

#         with open(log_file, "a") as log:
#             log.write(f"{file_path[1:]}:{file_hash}\n")

#         return f"✅ Hash stored for '{file_path}' in {log_file}."
#     except Exception as e:
#         return f"⚠️ Error storing hash: {e}"
    
# file_to_check = "../static/Files/modelTest.pkl"  # Path to model file

# result = save_hash_to_file(file_to_check, log_file="../static/Files/Outputs/hash_log.txt")
# print(result)  # Print result to confirm successful storage


import os

def unlockWeightTamperingFunction(file_path: str) -> str:
    """Unlocks a model file by restoring write permissions."""
    try:
        os.chmod(file_path, 0o644)  # Restore write permissions for the owner
        return f"✅ Model file '{file_path}' unlocked successfully."
    except Exception as e:
        return f"⚠️ Error unlocking model file '{file_path}': {e}"

file_to_unlock = "../Workspace/slope.expedition@gmail.com/AccountWorkspace/Models/DataCoSupplyChain/DataCoSupplyChain.csv-Clustering-Dec06-23-10-31-00.pkl"  # Path to model file

result = unlockWeightTamperingFunction(file_to_unlock)
print(result)  # Confirm successful unlock


import os
import stat

def isModelLocked(file_path: str) -> str:
    """Checks if a model file is locked (read-only)."""
    try:
        file_status = os.stat(file_path)
        if not file_status.st_mode & stat.S_IWUSR:
            return f"🔒 The model file '{file_path}' is locked (read-only)."
        else:
            return f"🔓 The model file '{file_path}' is not locked (write permissions enabled)."
    except Exception as e:
        return f"⚠️ Error checking file permissions: {e}"

def allowModelDeletionFunction(file_path: str) -> str:
    """Restores delete permissions on a file (undo preventModelDeletionFunction)."""
    try:
        os.system(f'icacls "{file_path}" /remove:d Everyone')
        return f"🔓 Deletion permission restored: {file_path}"
    except Exception as e:
        return f"⚠️ Failed to restore deletion permission: {e}"
    
def isModelDeletionPrevented(file_path: str) -> str:
    """Checks if delete permissions are denied for the file."""
    try:
        result = os.popen(f'icacls "{file_path}"').read()
        if "(D)" in result or "DENY" in result:
            return f"🔒 Delete prevention is active on: {file_path}"
        else:
            return f"🔓 File '{file_path}' is not deletion-protected."
    except Exception as e:
        return f"⚠️ Error checking deletion status: {e}"


# Example usage
if __name__ == "__main__":
    file_to_unlock = "../Workspace/slope.expedition@gmail.com/AccountWorkspace/DeepFenceOutputs/DataCoSupplyChain.csv-Clustering-Dec17-23-13-40-49_locked.pkl"  # Update if needed
    file_to_delete = "../Workspace/slope.expedition@gmail.com/AccountWorkspace/Models/DataCoSupplyChain/DataCoSupplyChain.csv-Clustering-Dec05-23-16-24-58.pkl"  # Update if needed
    # result = isModelDeletionPrevented(file_to_delete)
    # result = allowModelDeletionFunction(file_to_delete)
    # print(result)

# import os

# abs_path = os.path.abspath("../Workspace/slope.expedition@gmail.com/AccountWorkspace/Models/DataCoSupplyChain/DataCoSupplyChain.csv-Clustering-Dec05-23-16-19-19.pkl")
# print(f"🔎 Absolute path resolved: {abs_path}")

# import os
# print("📂 File exists:", os.path.exists("../Workspace/slope.expedition@gmail.com/AccountWorkspace/Models/DataCoSupplyChain/DataCoSupplyChain.csv-Clustering-Dec06-23-10-31-00.pkl"))
# print("📂 File exists:", os.path.exists(r"C:\Users\v-nregalla\Desktop\Google-ADK\WorkflowADK\Workspace\slope.expedition@gmail.com\AccountWorkspace\Models\DataCoSupplyChain\DataCoSupplyChain.csv-Clustering-Dec05-23-16-19-19.pkl"))

# print(f"📌 Current Working Directory: {os.getcwd()}")




