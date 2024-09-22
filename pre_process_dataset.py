import os
from PIL import Image
import re

# inspired by https://github.com/Rajasekaran85/Python-TIFF-to-JPEG

dataset_dir = "dataset/"
output_name_prefix = dataset_dir + "__generated__"

print("Tiff->JPG conversion starting...")

for fname in os.listdir(dataset_dir):
    print(fname)

    if not fname.endswith(".tif"):
        continue
    test = os.path.splitext(fname)[0]

    # open the tif image
    image = Image.open(dataset_dir + fname)

    # define jpg file name as same tif image name
    name = output_name_prefix + test + ".jpg"

    # get the tif image resolution value
    img_dpi = str(image.info["dpi"])
    patn = re.sub(r"[\(\)]", "", img_dpi)
    sp = patn.split(",")[0]
    dpi_val = round(float(sp))

    # convert to jpeg image, resolution value assigned from tiff image
    image.save(name, "jpeg", dpi=(dpi_val, dpi_val), quality=90)

print("Tiff->JPG conversion completed")
