from PIL import Image

def create_instagram_avatar():
    try:
        # Open the original logo
        original_logo = Image.open('social-media/logo/logo-maestro-preta.jpg')
        
        # Convert to RGB just in case
        original_logo = original_logo.convert('RGB')
        
        # Define the Instagram avatar size
        avatar_size = 1080
        
        # Create a new completely black image
        avatar = Image.new('RGB', (avatar_size, avatar_size), (0, 0, 0))
        
        # We want the logo to occupy about 55% of the canvas to give plenty of safe zone
        # The Instagram circle crops corners, and we want it to breathe.
        target_logo_size = int(avatar_size * 0.55)
        
        # Resize the original logo (maintaining aspect ratio)
        # We will fit it inside a target_logo_size box
        aspect_ratio = original_logo.width / original_logo.height
        if aspect_ratio > 1:
            # Wider than tall
            new_w = target_logo_size
            new_h = int(target_logo_size / aspect_ratio)
        else:
            # Taller than wide
            new_h = target_logo_size
            new_w = int(target_logo_size * aspect_ratio)
            
        resized_logo = original_logo.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        # Calculate position to center it
        x_pos = (avatar_size - new_w) // 2
        y_pos = (avatar_size - new_h) // 2
        
        # Paste the logo onto the black background
        avatar.paste(resized_logo, (x_pos, y_pos))
        
        # Save it
        avatar.save('social-media/instagram_avatar.jpg', quality=95)
        print("Avatar successfully generated at social-media/instagram_avatar.jpg")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_instagram_avatar()
