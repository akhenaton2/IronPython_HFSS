# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2018.2.0
# 15:54:02  Mar 03, 2022
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Modified Seneca Design Ameer")
oDesign = oProject.SetActiveDesign("HFSSDesign1")

#CREATE a NEW variable "gap" and assign an initial value. Do not use that
#if you want to CHANGE the value of "gap"
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
					"NAME:gap",
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
				"Value:="		, "gap"
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
    
# Change the value of the local variable "n" in the project. It is defined as 
# "LocalVariables" instead of "RectangularSpiral2:CreateUserDefinedPart:1"
# in case of change of variables in the imported geometry
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
				"NAME:ChangedProps",
				[
					"NAME:n",
					"Value:="		, "6"
				]
			]
		]
	])


