from google.cloud import vision
import os

# Set your Google Cloud project ID (replace with your actual project ID)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "savvy-bonito-440904-q7-2bd81c617b43.json"  # Replace with your credentials file path

def analyze_image(image_path):
    """Detects objects and text in an image using the Google Cloud Vision API."""

    client = vision.ImageAnnotatorClient()

    with open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.object_localization(image=image)

    objects = response.localized_object_annotations
    text_annotations = response.text_annotations

    # Process objects (optional, you can customize this)
    object_descriptions = [obj.name for obj in objects]
    print("Detected Objects:", object_descriptions)

    # Process text (optional, you can customize this)
    if text_annotations:
        text = text_annotations[0].description
        print("Detected Text:", text)

    #print(object_descriptions)
    return object_descriptions, text


# Example usage:
image_path = "C:\\Users\\lucky\\Documents\\coding\\cathay\\img\\paper.png"  # Replace with your image path
#objects, text = analyze_image(image_path)

print(analyze_image(image_path))

#Further processing of objects and text can be done here.  For example, you could combine the information into a descriptive sentence.
