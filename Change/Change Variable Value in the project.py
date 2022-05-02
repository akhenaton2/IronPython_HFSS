# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2018.2.0
# 10:14:07  Mar 04, 2022
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Modified Seneca Design Ameer")
oDesign = oProject.SetActiveDesign("HFSSDesign1")

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
    
#CREATION of GAP2 variable**************************
# oDesign.ChangeProperty(
	# [
		# "NAME:AllTabs",
		# [
			# "NAME:LocalVariableTab",
			# [
				# "NAME:PropServers", 
				# "LocalVariables"
			# ],
			# [
				# "NAME:NewProps",
				# [
					# "NAME:gap2",
					# "PropType:="		, "VariableProp",
					# "UserDef:="		, True,
					# "Value:="		, "5mm"
				# ]
			# ]
		# ]
	# ])
