# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2018.2.0
# 15:54:02  Mar 03, 2022
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Modified Seneca Design Ameer")
oDesign = oProject.SetActiveDesign("HFSSDesign1")

#Create a NEW variable "gap2" and assign an initial value. Do not use that
#if you want to CHANGE the value of "gap2"
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
					"NAME:gap2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "5mm"
				]
			]
		]
	])

#Create a NEW variable "n" and assign an initial value. Do not use that
#if you want to CHANGE the value of "n"
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
#Import/creation of the spiral geometry AFTER the declaration of variables
#that are used in that geometry
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateUserDefinedPart(
	[
		"NAME:UserDefinedPrimitiveParameters",
		"DllName:="		, "Examples/RectangularSpiral.py",
		"Version:="		, "2.0",
		"NoOfParameters:="	, "6",
		"Library:="		, "syslib",
		[
			"NAME:ParamVector",
			[
				"NAME:Pair",
				"Name:="		, "Xpos",
				"Value:="		, "0mm"
			],
			[
				"NAME:Pair",
				"Name:="		, "Ypos",
				"Value:="		, "0mm"
			],
			[
				"NAME:Pair",
				"Name:="		, "Dist",
				"Value:="		, "gap2"
			],
			[
				"NAME:Pair",
				"Name:="		, "Turns",
				"Value:="		, "n",
				"ParamType:="		, "IntParam"
			],
			[
				"NAME:Pair",
				"Name:="		, "Width",
				"Value:="		, "2mm"
			],
			[
				"NAME:Pair",
				"Name:="		, "Thickness",
				"Value:="		, "1mm"
			]
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "RectangularSpiral2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "RelativeCS1",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
#Change property of the turn number of the imported geometry (spiral)   
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
					"Value:="		, "6"
				]
			]
		]
	])
