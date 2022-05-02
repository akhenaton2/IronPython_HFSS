# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2022.1.0
# 12:05:51  Mar 17, 2022

#Describe the Unit, Substract, Undo last operation, assign material
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Modified Seneca Design Ameer")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")

oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Box1,Box1_1"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "Box1_2",
		"Tool Parts:="		, "Box1"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])

oDesign.Undo()

oEditor.AssignMaterial(
	[
		"NAME:Selections",
		"AllowRegionDependentPartSelectionForPMLCreation:=", True,
		"AllowRegionSelectionForPMLCreation:=", True,
		"Selections:="		, "Box1_1"
	], 
	[
		"NAME:Attributes",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "nan ",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

