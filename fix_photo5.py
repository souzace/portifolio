from PIL import Image, ExifTags

def fix_orientation(image_path):
    try:
        image = Image.open(image_path)
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        
        exif = image._getexif()
        if exif is not None:
            orientation_val = exif.get(orientation, None)
            if orientation_val == 3:
                image = image.rotate(180, expand=True)
            elif orientation_val == 6:
                image = image.rotate(270, expand=True)
            elif orientation_val == 8:
                image = image.rotate(90, expand=True)
        
        image.save(image_path)
        print("Fixed orientation for", image_path)
    except Exception as e:
        print("Error fixing orientation:", e)

fix_orientation("nilson-vieira/photo5.jpg")
