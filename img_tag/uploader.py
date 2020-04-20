from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


def upload_image(img_path):
    gauth = get_auth()
    return upload_get_id(gauth, img_path)


def upload_get_id(gauth, file_path):
    drive = GoogleDrive(gauth)
    folder_id = '1nh8EI6SgTijcmplATn91J8iJ5fxkupOQ'
    upload_file = drive.CreateFile(
        {"parents": [{"kind": "drive#fileLink", "id": folder_id}]})
    upload_file.SetContentFile(file_path)
    upload_file.Upload()
    upload_file.InsertPermission({
        'type': 'anyone',
        'value': 'anyone',
        'role': 'reader'})
    os.unlink(file_path)
    return upload_file['id']


def list_folder(drive, id):
    folder_list = drive.ListFile({
        'q': "'{}' in parents and trashed=false and mimeType='application/vnd.google-apps.folder'".format(
            id)}).GetList()
    return folder_list


def get_auth():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(os.path.join(
        "/Users/hoetaekpro/Desktop/python/img_tag/img_tag", "creds", "580916113" + "creds.txt"))
    return gauth


if __name__ == "__main__":
    upload_image('../../짙어져.mp3')
