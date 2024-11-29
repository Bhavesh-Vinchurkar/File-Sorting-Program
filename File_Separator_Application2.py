import os,shutil

dict_extension={
    'video_extensions':('.mp4','.mkv','.mov','.MP4','.MKV','.MOV'),
    'audio_extensions':('.mp3','.MP3','.wav','.WAV','.mpa','.MPA'),
    'document_extensions':('.pdf','.PDF','.docx','.DOCX','.epub','.EPUB'),
    'image_extensions':('.jpeg','jpg','.png','.JPEG','.JPG','.PNG'),
    'code_extensions':('.py','.java','.cpp','.PY','.CPP','.JAVA')
}

folder_path=input("Enter the folder path : ")

def file_finder(f_path,file_extension):
    files_name=[]
    for files in os.listdir(f_path):
        for extensions in file_extension:
            if files.endswith(extensions):
                files_name.append(files)
    return files_name

for extension_type, extension_name in dict_extension.items():
    newfolder_name=extension_type.split('_')[0]+" Files" 
    newfolder_path=os.path.join(folder_path, newfolder_name)
    for item in file_finder(folder_path, extension_name):
        file_path=os.path.join(folder_path, item)
        new_filepath=os.path.join(newfolder_path,item)
        if not os.path.exists(newfolder_path):
            os.mkdir(newfolder_path)
        if os.path.exists(newfolder_path):
            shutil.move(file_path,new_filepath)
