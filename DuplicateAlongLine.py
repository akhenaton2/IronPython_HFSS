# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2022.1.0
# 15:53:17  Mar 09, 2022
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Modified Seneca Design Ameer")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")


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
		"YComponent:="		, str(2*0.1)+"mm" ,
		"ZComponent:="		, "0mm",
		"NumClones:="		, "3"
	],
	[
		"NAME:Options",
		"DuplicateAssignments:=", True
	],
	[
		"CreateGroupsForNewObjects:=", False
	])
