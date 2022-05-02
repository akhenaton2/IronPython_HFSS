# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2022.1.0
# 16:50:36  Mar 21, 2022
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Modified Seneca Design Ameer")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")

oEditor.Scale(
    [
        "NAME:Selections",
        "Selections:="		, "Box2",
        "NewPartsModelFlag:="	, "Model"
    ], 
    [
        "NAME:ScaleParameters",
        "ScaleX:="		, "2",
        "ScaleY:="		, "1",
        "ScaleZ:="		, "1"
    ])
        
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Box2:Scale:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Coordinate System",
					"Value:="		, "RelativeCS1"
				]
			]
		]
	])
