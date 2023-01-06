import os
import zipfile


def create_gskz(gsk_filename, folder_path):
  """
  Creates a zip archive includes
    - comment with the name of the macro file (gsk file)
    - the macro file (gsk file)
    - additional files from the directory
  """
  with zipfile.ZipFile(f"{gsk_filename}z", 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(f"{gsk_filename}")
    zipf.comment = f"{gsk_filename}".encode('windows-1250') + b"\xfeUnknown\xfeUnknown\xfe\xfe"

    len_dir_path = len(folder_path)
    for root, _, files in os.walk(folder_path):
      for file in files:
        file_path = os.path.join(root, file)
        zipf.write(file_path, file_path[len_dir_path:])


if __name__ == "__main__":
  create_gskz("NuernbergCityChallenge.gsk", "./assets")
