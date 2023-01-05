import zipfile

def create_gskz( gsk_filename ):
  with zipfile.ZipFile(f"{gsk_filename}z", 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.comment = f"{gsk_filename}".encode('windows-1250')+ b"\xfeUnknown\xfeUnknown\xfe\xfe"


if __name__ == "__main__":
  create_gskz("NuernbergCityChallenge.gsk")
  
