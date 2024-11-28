import os

source_folder = input("Source Directory: ")

# Define extensions
compressed_ext = [".zip", ".rar", ".7z", ".tar", ".tar.gz", ".tar.bz2", ".tar.xz", ".gz", ".bz2", ".xz", ".tgz", ".tbz2", ".txz", ".z"]

video_ext = [".mp4", ".avi", ".wmv", ".mov", ".mkv", ".flv", ".webm", ".m4v", ".mpg", ".mpeg", ".3gp", ".m2ts", ".mts", ".vob", ".ts", ".asf", ".m2t", ".divx", ".ogv", ".rmvb", ".xvid", ".f4v", ".h264", ".hevc", ".avi", ".webm", ".qt", ".mpv", ".mxf"]

image_ext = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".ico", ".heic", ".jfif", ".jpe", ".raw", ".eps", ".ai", ".psd", ".indd", ".cdr", ".cr2", ".orf", ".nef", ".sr2", ".arw", ".rw2", ".pef"]

documents_ext = [".doc", ".docx", ".pdf", ".txt", ".rtf", ".odt", ".odp", ".ods", ".xlsx", ".pptx", ".csv", ".json", ".xml"]

music_ext = [".mp3", ".wav", ".wma", ".aac", ".flac", ".alac", ".ogg", ".m4a", ".opus", ".webm", ".mid", ".midi", ".amr", ".aif", ".aiff", ".au", ".raw", ".mka", ".ac3", ".dts", ".ape", ".mac", ".mp2", ".mp1", ".mpa", ".mpc", ".ofr", ".ofs", ".rmi", ".tta", ".wv", ".xm", ".mod", ".s3m", ".it", ".mtm", ".umx"]

programs_ext = [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm", ".app", ".bat", ".sh", ".AppImage"]

fonts_ext = [".ttf", ".otf", ".woff", ".woff2", ".eot"]



for file_name in os.listdir(source_folder):
    
    # Get the file extension
    extension = os.path.splitext(file_name)[1]
    print(file_name)
    
    # For compressed files
    if extension in compressed_ext:
    
        if not os.path.exists(os.path.join(source_folder, "Compressed")):
            os.mkdir(os.path.join(source_folder, "Compressed"))
            
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(source_folder, "Compressed", file_name)

        # Move the file to the Compressed folder
        os.rename(source_path, destination_path)
        
    # For video files
    if extension in video_ext:
    
        if not os.path.exists(os.path.join(source_folder, "Videos")):
            os.mkdir(os.path.join(source_folder, "Videos"))
            
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(source_folder, "Videos", file_name)

        # Move the file to the Videos folder
        os.rename(source_path, destination_path)
        
    # For image files
    if extension in image_ext:
    
        if not os.path.exists(os.path.join(source_folder, "Images")):
            os.mkdir(os.path.join(source_folder, "Images"))
            
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(source_folder, "Images", file_name)

        # Move the file to the Images folder
        os.rename(source_path, destination_path)
        
    # For docs files
    if extension in documents_ext:
    
        if not os.path.exists(os.path.join(source_folder, "Documents")):
            os.mkdir(os.path.join(source_folder, "Documents"))
            
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(source_folder, "Documents", file_name)

        # Move the file to the Documents folder
        os.rename(source_path, destination_path)
        
    # For music files
    if extension in music_ext:
    
        if not os.path.exists(os.path.join(source_folder, "Music")):
            os.mkdir(os.path.join(source_folder, "Music"))
            
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(source_folder, "Music", file_name)

        # Move the file to the Music folder
        os.rename(source_path, destination_path)
        
    # For programs files
    if extension in programs_ext:
    
        if not os.path.exists(os.path.join(source_folder, "Programs")):
            os.mkdir(os.path.join(source_folder, "Programs"))
            
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(source_folder, "Programs", file_name)

        # Move the file to the Programs folder
        os.rename(source_path, destination_path)
        
    # For fonts files
    if extension in fonts_ext:
    
        if not os.path.exists(os.path.join(source_folder, "Fonts")):
            os.mkdir(os.path.join(source_folder, "Fonts"))
            
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(source_folder, "Fonts", file_name)

        # Move the file to the Fonts folder
        os.rename(source_path, destination_path)
        
    
