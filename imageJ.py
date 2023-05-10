import imagej
# ij = imagej.init("2.5.0")
ij = imagej.init()
print(f"ImageJ version: {ij.getVersion()}")

# Load an image.
# image_url = 'https://imagej.net/images/clown.jpg'
image_url = 'test.jpg'
jimage = ij.io().open(image_url)

# Convert the image from ImageJ2 to xarray, a package that adds
# labeled datasets to numpy (http://xarray.pydata.org/en/stable/).
# image = ij.py.from_java(jimage)

# Display the image (backed by matplotlib).
# ij.py.show(image, cmap='gray')

    # run("Raw...", "open="+dir1+list[i]+" image=[32-bit Real] width=640 height=512 offset=0 number=1 gap=0 little-endian");
# dir1 = "F:\\IanDennis\\Other\\Thermal\\Images\\Radiometric\\"
# file="test_f.raw"
# out="test_out2"
# image = ij.IJ.run("Raw...", "open="+ file +" image=[32-bit Real] width=640 height=512 offset=0 number=1 gap=0 little-endian")
# ij.io().save(image, filepath)
# ij.io().saveAsTiff(out)

macro = """
#@ String inDir
#@ String outDir

#@output Object greeting
list = getFileList(inDir);
setBatchMode(true); 

greeting="Start";

for (i=0; i<list.length; i++) {
    image_url = inDir+list[i];
    out_url = outDir+list[i];
    run("Raw...", "open="+image_url+" image=[32-bit Real] width=640 height=512 offset=0 number=1 gap=0 little-endian");
    saveAs("Tiff", out_url);
    close();



}

"""
args = {
    'inDir': 'F:\\IanDennis\\Other\\Thermal\\Images\\Radiometric\\Test_raw\\',
    'outDir': 'F:\\IanDennis\\Other\\Thermal\\Images\\Radiometric\\Test_Out\\'
}
result = ij.py.run_macro(macro, args)
print(result.getOutput('greeting'))


