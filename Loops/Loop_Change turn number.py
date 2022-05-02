# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2018.2.0
# 17:51:41  Mar 03, 2022
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Modified Seneca Design Ameer")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:n",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "3"
				]
			]
		]
	])
    
# for n in range(3,12):
oEditor.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:Geometry3DCmdTab",
            [
                "NAME:PropServers", 
                "RectangularSpiral2:CreateUserDefinedPart:1"
            ],
            [
                "NAME:ChangedProps",
                [
                    "NAME:Turns",
                    "Value:="		, n
                ]
            ]
        ]
    ])
