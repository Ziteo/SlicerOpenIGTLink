# Run this Python Script As soon as we start receiving data

# ./Slicer --python-script "/git/ziteo/open_source/SlicerOpenIGTLink/OpenIGTLinkIF/OpenIGTLinkIFTasks.py"

# Display Pose Scan Time in Slice Views
import time

# Put it into a Python class becomes 
view=slicer.app.layoutManager().sliceWidget("Red").sliceView()
view2=slicer.app.layoutManager().sliceWidget("Green").sliceView()
view3=slicer.app.layoutManager().sliceWidget("Yellow").sliceView()

# TODO: IGTLConnector Node established, turns on, receiving images, start counting
# TODO: Look at PerklabsBootcamp for Python's DataFlow for 3D Slicer


for it in range(30):
    # Set text to "Pose Scan Time: {it}"
    view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperRight,"Pose Scan Time {}".format(it))
    view2.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperRight,"Pose Scan Time {}".format(it))
    view3.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperRight,"Pose Scan Time {}".format(it))
    # Set color to red
    view.cornerAnnotation().GetTextProperty().SetColor(0,1,0)
    view2.cornerAnnotation().GetTextProperty().SetColor(0,1,0)
    view3.cornerAnnotation().GetTextProperty().SetColor(0,1,0)
    # Update the view
    view.forceRender()
    view2.forceRender()
    view3.forceRender()
    slicer.app.processEvents()
    time.sleep(0.1)
