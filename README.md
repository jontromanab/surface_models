surface_models
=====
urdf models of various surfaces. Tables and whiteboards for cleaning and shelves for robot factor.

### Tables(HCR lab) ###
1. lab_center_table (middle table with all the systems)
2. lab_conf_table 
3. lab_phone_table
4. lab_wood_table (small table for Fetch experiments)

### Whiteboards(HCR lab) ###
1. Lab_main_whiteboard (on the wall)
2. lab_side_whiteboard (near Herb)

### shelves ###
Shelves can be automatically created from the script ```create_shelves.py```
Some of the automatically generated shelves are in the urdf folder

To view individual models, you can do one of them:

```
roslaunch surface_models table.launch file:=lab_center_table.xacro'
roslaunch surface_models shelves.launch
```

