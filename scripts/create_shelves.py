#!/usr/bin/env python

import sys

material = '  <material name="brown_transparent"/>\n'
def set_filename(a, b, c, d, e):
	filename = "W_%s_h1_%s_d1_%s_h2_%s_d2_%s.xacro" %(str(a),str(b),str(c),str(d),str(e))
	return filename

def create_shelf_base():
	name = '<link name = "shelf_base">\n'
	inertial = '<inertial> \n <origin xyz = "0 0 0" /> \n <mass value = "1.0" /> \n'
	inertia = ' <inertia ixx = "1.0" ixy="0.0"  ixz="0.0"  iyy="100.0"  iyz="0.0"  izz="1.0" />\n'
	inertial_end = ' </inertial>\n'
	visual = "<visual>\n"
	geometry = '  <geometry>\n \t<box size="${shelf_base_width} ${shelf_thickness} ${shelf_base_height}"/>\n'
	geometry_end = '  </geometry>\n'
	visual_end = "</visual>\n"
	collision = "<collision>\n"
	collision_end = "</collision>"
	name_end = '\n</link>'
	shelf_name = name+inertial+inertia+inertial_end+visual+geometry+geometry_end+material+visual_end+collision+geometry+geometry_end+material+collision_end+name_end
	return shelf_name

def create_joint(num):
	name = '<joint name="base_to_shelf%s" type="fixed"> \n'%(num)
	parent = '  <parent link="shelf_base"/>\n'
	child = '  <child link="shelf_%s"/> \n'%(num)
	axis = '  <axis xyz="0 0 0"/>\n'
	origin = '  <origin rpy="0.0 0.0 0.0" xyz="0.0 ${-shelf%s_depth/2} ${-shelf_base_height/2 + shelf%s_height}"/>\n' %(num, num)
	name_end = '</joint>'
	joint = name+parent+child+axis+origin+name_end
	return joint

def create_shelf(num):
	name = '<link name = "shelf_%s">\n' %(num)
	visual = "<visual>\n"
	geometry = '  <geometry>\n \t<box size="${shelf_base_width} ${shelf%s_depth} ${shelf_thickness}"/>\n' %(num)
	geometry_end = '  </geometry>\n'
	visual_end = "</visual>\n"
	collision = "<collision>\n"
	collision_end = "</collision>"
	name_end = '\n</link>'
	shelf_name = name+visual+geometry+geometry_end+material+visual_end+collision+geometry+geometry_end+material+collision_end+name_end
	return shelf_name

def create_material(num):
	ref = '<gazebo reference="shelf_%s">\n' %(str(num))
	mat = '   <material>Gazebo/Wood</material>\n'
	ref_end = '</gazebo>\n'
	material = ref+mat+ref_end
	return material


print("The height of the wall is 1.5 and the thickness is 0.05")
shelf_base_width = input('What is the shelf base length? ')
shelf1_height = input("What is the height of the first shelf? ")
shelf1_depth = input("What is the depth of the first shelf? ")
shelf2_height = input("What is the height of the second shelf? ")
shelf2_depth = input("What is the depth of the secon shelf? ")

#shelf_base_width = 4.1
#shelf1_height = 0.3
#shelf1_depth = 0.1
#shelf2_height = 0.7
#shelf2_depth = 0.4

shelf_base_height = 1.5
shelf_thickness = 0.05


filename = set_filename(shelf_base_width, shelf1_height, shelf1_depth, shelf2_height,
	shelf2_depth)

shelf_base = create_shelf_base()
joint1 = create_joint(1)
shelf1 = create_shelf(1)
joint2 = create_joint(2)
shelf2 = create_shelf(2)

mat_base = create_material("base")
mat_1 = create_material(1)
mat_2 = create_material(2)

with open(filename,"w") as text_file:
	text_file.write('<?xml version="1.0" ?> \n')
	text_file.write('<robot name="shelf_%s_%s_%s_%s_%s" ' % (str(shelf_base_width), str(shelf1_height),
		str(shelf1_depth), str(shelf2_height), str(shelf1_depth)))
	text_file.write('xmlns:xacro="http://ros.org/wiki/xacro"> \n')
	text_file.write("\n"*2)
	text_file.write("<!-- Property List --> \n")
	text_file.write('<xacro:property name="pi" value="3.1415926535897931" />\n')
	text_file.write('<xacro:property name="shelf_base_height" value="%s" />\n' %(str(shelf_base_height)))
	text_file.write('<xacro:property name="shelf_thickness" value="%s" />\n' %(str(shelf_thickness)))
	text_file.write('<xacro:property name="shelf_base_width" value="%s" />\n' %(str(shelf_base_width)))
	text_file.write("\n"*2)
	text_file.write('<xacro:property name="shelf1_height" value="%s" />\n' %(str(shelf1_height)))
	text_file.write('<xacro:property name="shelf1_depth" value="%s" />\n' %(str(shelf1_depth)))
	text_file.write("\n"*2)
	text_file.write('<xacro:property name="shelf2_height" value="%s" />\n' %(str(shelf2_height)))
	text_file.write('<xacro:property name="shelf2_depth" value="%s" />\n' %(str(shelf2_depth)))
	text_file.write("\n"*2)
	text_file.write("<!-- Color macros --> \n")
	text_file.write('<xacro:macro name="material_brown_transparent"> \n ')
	text_file.write('\t<material name="brown_transparent">\n')
	text_file.write('\t\t<color rgba="${139/255} ${69/255} ${19/255} 0.4" />\n')
	text_file.write('\t</material>\n')
	text_file.write('</xacro:macro> ')
	text_file.write("\n"*2)
	text_file.write("<!-- Base Link --> \n")
	text_file.write(shelf_base)
	text_file.write("\n"*2)
	text_file.write("<!-- Base To First shelf link Joint--> \n")
	text_file.write(joint1)
	text_file.write("\n"*2)
	text_file.write("<!-- First shelf Link--> \n")
	text_file.write(shelf1)
	text_file.write("\n"*2)
	text_file.write("<!-- Base To Second shelf link Joint--> \n")
	text_file.write(joint2)
	text_file.write("\n"*2)
	text_file.write("<!-- Second shelf Link--> \n")
	text_file.write(shelf2)
	text_file.write("\n"*2)
	text_file.write(mat_base+"\n"+mat_1+"\n"+mat_2)
	text_file.write("\n"*3)
	text_file.write("</robot>")





print "Created URDF: W_"+str(shelf_base_width)+"_h1_"+str(shelf1_height)+"_d1_"+str(shelf1_depth)+"_h2_"+str(shelf2_height)+"_d2_"+str(shelf2_depth)+".xacro"



