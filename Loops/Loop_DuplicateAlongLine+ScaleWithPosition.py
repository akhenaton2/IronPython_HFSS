# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2022.1.0
# 15:22:01  Mar 16, 2022
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Modified Seneca Design Ameer")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")

for n in range(1,4):
    oEditor.DuplicateAlongLine(
        [
            "NAME:Selections",
            "Selections:="		, "Box1",
            "NewPartsModelFlag:="	, "Model"
        ], 
        [
            "NAME:DuplicateToAlongLineParameters",
            "CreateNewObjects:="	, True,
            "XComponent:="		, "0mm",
            "YComponent:="		, str(0.4*n)+"mm",
            "ZComponent:="		, "0mm",
            "NumClones:="		, "2"
        ], 
        [
            "NAME:Options",
            "DuplicateAssignments:=", True
        ], 
        [
            "CreateGroupsForNewObjects:=", False
        ])
        
    oEditor.Scale(
        [
            "NAME:Selections",
            "Selections:="		, "Box1_"+str(n),
            "NewPartsModelFlag:="	, "Model"
        ], 
        [
            "NAME:ScaleParameters",
            "ScaleX:="		, str(n+1),
            "ScaleY:="		, "1",
            "ScaleZ:="		, "1"
        ])

#Change the coordinate system of the scale

# oEditor.ChangeProperty(
	# [
		# "NAME:AllTabs",
		# [
			# "NAME:Geometry3DCmdTab",
			# [
				# "NAME:PropServers", 
				# "Box2:Scale:1"
			# ],
			# [
				# "NAME:ChangedProps",
				# [
					# "NAME:Coordinate System",
					# "Value:="		, "RelativeCS1"
				# ]
			# ]
		# ]
	# ])